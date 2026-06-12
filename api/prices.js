/**
 * CSOAI SaaS Price Configuration (2026)
 * Centralized mapping of Tier IDs to Stripe Price IDs.
 */

export const STRIPE_PRICES = {
  // Certification Tiers
  "smoke": process.env.STRIPE_PRICE_SMOKE || "price_smoke_placeholder", // £1
  "casa": process.env.STRIPE_PRICE_CASA || "price_casa_placeholder",   // £199/mo
  "art50": process.env.STRIPE_PRICE_ART50 || "price_art50_placeholder", // £999
  
  // MCP Pack Tiers
  "pack_eu_ai_act": process.env.STRIPE_PRICE_PACK_EU || "price_eu_placeholder",
  "pack_brand": process.env.STRIPE_PRICE_PACK_BRAND || "price_brand_placeholder",
  "pack_finance": process.env.STRIPE_PRICE_PACK_FINANCE || "price_finance_placeholder",
  "pack_legacy": process.env.STRIPE_PRICE_PACK_LEGACY || "price_legacy_placeholder",
  "pack_governance": process.env.STRIPE_PRICE_PACK_GOV || "price_gov_placeholder",
};

export default function handler(req, res) {
  return res.status(200).json(STRIPE_PRICES);
}
