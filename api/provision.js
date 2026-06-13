/**
 * CSOAI Supabase Provisioning Logic (2026)
 * Handles database persistence for certificates and users.
 */

import { createClient } from '@supabase/supabase-js';
import crypto from 'crypto';

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

/**
 * Provision a new Certification
 * 1. Generate unique did:csoai ID
 * 2. Create certificate record in Supabase
 * 3. Update user subscription status
 */
export async function provisionCertification(tierId, email) {
  try {
    const didId = `did:csoai:${crypto.randomBytes(4).toString('hex')}-${crypto.randomBytes(2).toString('hex')}`;
    const expiresAt = new Date();
    expiresAt.setFullYear(expiresAt.getFullYear() + 1); // 1 year validity

    const { data, error } = await supabase
      .from('certificates')
      .insert([
        {
          did_id: didId,
          user_email: email,
          tier_id: tierId,
          status: 'active',
          issued_at: new Date().toISOString(),
          expires_at: expiresAt.toISOString(),
          metadata: {
            source: 'stripe_checkout',
            frameworks: tierId === 'art50' ? ['EU AI Act'] : ['CASA Standard', 'OWASP Agentic Top 10']
          }
        }
      ])
      .select();

    if (error) throw error;

    console.log(`[Provisioning Success] ${didId} for ${email}`);
    return { ok: true, certificate: data[0] };
  } catch (error) {
    console.error("[Provisioning Error]", error);
    return { ok: false, error: error.message };
  }
}

/**
 * Get User Dashboard Data
 */
export async function getUserData(email) {
  const { data: profile } = await supabase
    .from('profiles')
    .select('*')
    .eq('email', email)
    .single();

  const { data: certs } = await supabase
    .from('certificates')
    .select('*')
    .eq('user_email', email);

  return { profile, certs };
}
