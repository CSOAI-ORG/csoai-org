/**
 * CSOAI SaaS Price Configuration (2026)
 * Centralized mapping of Tier IDs to Stripe Price IDs.
 * Updated 2026-06-17 from live Stripe dashboard.
 */

export const STRIPE_PRICES = {
  // Certification Tiers (mapped to existing live Stripe products)
  "smoke": process.env.STRIPE_PRICE_SMOKE || "price_1TgmOmQvIueK5XpbBAmfHv8B", // openmoe Starter £29/mo
  "casa": process.env.STRIPE_PRICE_CASA || "price_1TjB68QvIueK5XpbwxEkXxSd",   // CSOAI Starter £499/mo
  "art50": process.env.STRIPE_PRICE_ART50 || "price_1TgmOnQvIueK5XpbazVFUMCk", // openmoe Enterprise £1499/mo

  // MCP Pack Tiers (mapped to existing live Stripe products)
  "pack_eu_ai_act": process.env.STRIPE_PRICE_PACK_EU || "price_1TjB8cQvIueK5XpbsOyuzR2b",      // CSOAI Professional £999/mo
  "pack_brand": process.env.STRIPE_PRICE_PACK_BRAND || "price_1TgmOlQvIueK5Xpb83CQLQ61",       // OptiMobile Practice £99/mo
  "pack_finance": process.env.STRIPE_PRICE_PACK_FINANCE || "price_1TgmOrQvIueK5Xpbji5IBy96",   // OptiMobile Provider £249/mo
  "pack_legacy": process.env.STRIPE_PRICE_PACK_LEGACY || "price_1TgmOsQvIueK5Xpb8uDu51n1",     // OptiMobile Provider annual £2490
  "pack_governance": process.env.STRIPE_PRICE_PACK_GOV || "price_1TjB8cQvIueK5Xpbu0XMj01Q",    // CSOAI Professional annual £9588
};

export default function handler(req, res) {
  return res.status(200).json(STRIPE_PRICES);
}
