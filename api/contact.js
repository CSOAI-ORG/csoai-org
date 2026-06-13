/**
 * CSOAI Contact Form API
 * POST /api/contact
 *
 * Expects: name, email, company, topic, message
 * Sends email via Resend if RESEND_API_KEY is configured.
 * Posts to Discord webhook if DISCORD_WEBHOOK_URL is configured.
 */

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

  const { name, email, company, topic, message, _gotcha } = req.body || {};

  // Honeypot
  if (_gotcha) {
    return res.status(200).json({ ok: true });
  }

  // Validation
  if (!name || !email || !topic || !message) {
    return res.status(400).json({ ok: false, error: "Missing required fields" });
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ ok: false, error: "Invalid email address" });
  }

  const payload = {
    type: "contact",
    name: String(name).trim(),
    email: String(email).trim().toLowerCase(),
    company: String(company || "").trim(),
    topic: String(topic).trim(),
    message: String(message).trim(),
    submittedAt: new Date().toISOString(),
  };

  // Log submission (visible in Vercel function logs)
  console.log("[CSOAI Contact]", JSON.stringify(payload));

  // Optional: Discord webhook
  if (process.env.DISCORD_WEBHOOK_URL) {
    try {
      await fetch(process.env.DISCORD_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          content: `**New CSOAI Contact Inquiry**\n**Name:** ${payload.name}\n**Email:** ${payload.email}\n**Company:** ${payload.company || "N/A"}\n**Topic:** ${payload.topic}\n**Message:** ${payload.message.slice(0, 1500)}`,
        }),
      });
    } catch (e) {
      console.error("Discord webhook failed:", e);
    }
  }

  // Optional: Resend email notification
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
          reply_to: payload.email,
          subject: `CSOAI Contact: ${payload.topic}`,
          text: `Name: ${payload.name}\nEmail: ${payload.email}\nCompany: ${payload.company || "N/A"}\nTopic: ${payload.topic}\n\nMessage:\n${payload.message}`,
        }),
      });
    } catch (e) {
      console.error("Resend email failed:", e);
    }
  }

  return res.status(200).json({ ok: true });
}
