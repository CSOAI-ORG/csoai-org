# CSOAI Form Configuration

## Current Setup

Forms submit to custom Vercel API routes:

- **Contact form** (`contact.html`) → `POST /api/contact`
- **Newsletter signup** (`index.html`, `blog.html`, article pages) → `POST /api/newsletter`

## How It Works

The API routes (`api/contact.js` and `api/newsletter.js`) are serverless functions that run on Vercel. They:

1. Validate the submitted data
2. Log submissions to the Vercel function logs
3. Optionally notify via Discord webhook
4. Optionally send email notifications via **Resend**

## To Enable Email Notifications

1. Sign up for a free Resend account at https://resend.com
2. Verify your domain (or use the onboarding domain for testing)
3. Create an API key
4. In your Vercel project settings, add these environment variables:
   - `RESEND_API_KEY` — your Resend API key
   - `CONTACT_TO_EMAIL` — the email address that receives form submissions
   - `FROM_EMAIL` — optional sender address (defaults to `forms@csoai.org`)
5. Redeploy the project

## To Enable Discord Notifications

1. Create a Discord webhook URL for your channel
2. Add it as a Vercel environment variable:
   - `DISCORD_WEBHOOK_URL` — your Discord webhook URL
3. Redeploy the project

## Spam Protection

All forms include a hidden honeypot field (`_gotcha`). If a bot fills it in, the submission is silently ignored.

## Updating Form Endpoints

If you ever need to switch back to a third-party service (e.g., Formspree, Basin, Web3Forms), update the `action` attributes in the HTML files or edit `update_forms.py` and re-run it.
