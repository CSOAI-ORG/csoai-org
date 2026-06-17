/**
 * CSOAI Stripe Checkout API
 * POST /api/checkout
 *
 * Expects: tierId, email
 * Creates a Stripe Checkout session and returns the URL.
 */

import Stripe from 'stripe';
import { STRIPE_PRICES } from './prices.js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export default async function handler(req, res) {
  // CORS
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const { tierId, email } = req.body || {};

  if (!tierId) {
    return res.status(400).json({ ok: false, error: "tierId is required" });
  }

  const priceId = STRIPE_PRICES[tierId];
  if (!priceId || priceId.includes("placeholder")) {
    return res.status(400).json({ ok: false, error: `Invalid or unconfigured tierId: ${tierId}` });
  }

  try {
    const session = await stripe.checkout.sessions.create({
      customer_email: email,
      line_items: [
        {
          price: priceId,
          quantity: 1,
        },
      ],
      // All prices in STRIPE_PRICES are currently recurring subscriptions.
      // Flip to "payment" only when a one-time tier is explicitly added.
      mode: tierId === "art50_kit" || tierId === "emergency_audit" ? "payment" : "subscription",
      success_url: `${process.env.BASE_URL || 'https://csoai.org'}/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${process.env.BASE_URL || 'https://csoai.org'}/pricing`,
      metadata: {
        tierId: tierId,
      },
      allow_promotion_codes: true,
    });

    return res.status(200).json({ ok: true, url: session.url });
  } catch (error) {
    console.error("[Stripe Error]", error);
    return res.status(500).json({ ok: false, error: error.message });
  }
}
