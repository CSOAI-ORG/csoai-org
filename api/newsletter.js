/**
 * CSOAI Newsletter Signup API
 * POST /api/newsletter
 *
 * Expects: email
 * Sends email via Resend if RESEND_API_KEY is configured.
 */

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const { email, _gotcha } = req.body || {};

  if (_gotcha) {
    return res.status(200).json({ ok: true });
  }

  if (!email) {
    return res.status(400).json({ ok: false, error: "Email is required" });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ ok: false, error: "Invalid email address" });
  }

  const payload = {
    type: "newsletter",
    email: String(email).trim().toLowerCase(),
    submittedAt: new Date().toISOString(),
  };

  console.log("[CSOAI Newsletter]", JSON.stringify(payload));

  if (process.env.DISCORD_WEBHOOK_URL) {
    try {
      await fetch(process.env.DISCORD_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          content: `**New CSOAI Newsletter Signup**\n**Email:** ${payload.email}`,
        }),
      });
    } catch (e) {
      console.error("Discord webhook failed:", e);
    }
  }

  if (process.env.RESEND_API_KEY && process.env.CONTACT_TO_EMAIL) {
    try {
      await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          from: process.env.FROM_EMAIL || "CSOAI Forms <forms@csoai.org>",
          to: [process.env.CONTACT_TO_EMAIL],
          subject: "New CSOAI Newsletter Signup",
          text: `New newsletter signup: ${payload.email}`,
        }),
      });
    } catch (e) {
      console.error("Resend email failed:", e);
    }
  }

  return res.status(200).json({ ok: true });
}
