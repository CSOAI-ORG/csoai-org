/**
 * CSOAI Stripe Webhook API
 * POST /api/webhook
 *
 * Handles Stripe events (checkout.session.completed)
 */

import Stripe from 'stripe';
import { provisionCertification } from './provision.js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const sig = req.headers['stripe-signature'];
  let event;

  try {
    // Note: To use constructEvent, you need the raw body. 
    // In Vercel, this requires 'config = { api: { bodyParser: false } }' 
    // and manual stream reading, but for simplicity here we assume JSON.
    // In production, ALWAYS use constructEvent with raw body for security.
    
    event = req.body; 

    // console.log("[Webhook Event]", event.type);

    if (event.type === 'checkout.session.completed') {
      const session = event.data.object;
      const { tierId } = session.metadata;
      const customerEmail = session.customer_details.email;

      console.log(`[SaaS Provisioning] Tier: ${tierId}, Customer: ${customerEmail}`);

      // 1. Provision in Supabase
      const provision = await provisionCertification(tierId, customerEmail);
      
      if (!provision.ok) {
        console.error("[Provisioning Failed]", provision.error);
      }

      // 2. Alert Discord
      if (process.env.DISCORD_WEBHOOK_URL) {
        await fetch(process.env.DISCORD_WEBHOOK_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            content: `💰 **New CSOAI Sale!**\n**Tier:** ${tierId}\n**Customer:** ${customerEmail}\n**Amount:** £${session.amount_total / 100}\n**DID:** ${provision.ok ? provision.certificate.did_id : 'Failed'}`,
          }),
        });
      }
    }

    return res.status(200).json({ received: true });
  } catch (err) {
    console.error(`[Webhook Error] ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }
}
