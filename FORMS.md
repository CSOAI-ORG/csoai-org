# CSOAI Form Configuration

## Current Setup

Forms are configured to submit via [Formspree](https://formspree.io/):

- **Contact form** (`contact.html`) → `https://formspree.io/f/xjkyvepj`
- **Newsletter signup** (`index.html`, `blog.html`, article pages) → `https://formspree.io/f/xjkyvepk`

## To Connect Real Endpoints

1. Sign up for a free Formspree account at https://formspree.io/register
2. Create two new forms:
   - One for contact inquiries
   - One for newsletter subscriptions
3. Copy your form endpoints (they look like `https://formspree.io/f/XXXXXXXX`)
4. Update the endpoints in the following files:
   - `contact.html` (search for `xjkyvepj`)
   - `index.html` (search for `xjkyvepk`)
   - `blog.html` (search for `xjkyvepk`)
   - All `blog-*.html` article pages (search for `xjkyvepk`)
5. Alternatively, update `update_forms.py` and re-run it to bulk-update all pages

## Form Behavior

- Submissions are handled via AJAX for a smooth UX
- Success: the form is replaced with a confirmation message
- Error: an inline error message appears with a fallback email address
- No page reload required
