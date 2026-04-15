#!/usr/bin/env python3
"""Update all fake alert() forms to use Formspree endpoints."""
import re, glob, os

# Local Vercel API endpoints
CONTACT_ENDPOINT = "/api/contact"
NEWSLETTER_ENDPOINT = "/api/newsletter"

def replace_contact_form(text):
    """Replace contact form with Formspree POST form."""
    old = r'<form action="https://formspree\.io/f/xjkyvepj" method="POST" class="csoai-form" data-form-type="contact">'
    new = f'<form action="{CONTACT_ENDPOINT}" method="POST" class="csoai-form" data-form-type="contact">'
    text = re.sub(old, new, text)
    # Also catch any remaining alert-based contact forms
    old_alert = r'<form onsubmit="event\.preventDefault\(\); alert\(\'Thank you for your inquiry\. We will be in touch shortly\.\'\);">'
    new_alert = f'<form action="{CONTACT_ENDPOINT}" method="POST" class="csoai-form" data-form-type="contact">'
    text = re.sub(old_alert, new_alert, text)
    text = re.sub(old, new, text)
    return text

def replace_newsletter_form(text):
    """Replace newsletter forms with Formspree POST forms."""
    # Match various newsletter form patterns
    old1 = r'<form action="https://formspree\.io/f/xjkyvepk" method="POST" class="newsletter-form csoai-form" data-form-type="newsletter">'
    new1 = f'<form action="{NEWSLETTER_ENDPOINT}" method="POST" class="newsletter-form csoai-form" data-form-type="newsletter">'
    text = re.sub(old1, new1, text)

    old2 = r'<form class="newsletter-form" onsubmit="event\.preventDefault\(\); alert\(\'Thank you for subscribing!\'\);">'
    new2 = f'<form action="{NEWSLETTER_ENDPOINT}" method="POST" class="newsletter-form csoai-form" data-form-type="newsletter">'
    text = re.sub(old2, new2, text)
    
    old3 = r'<form onsubmit="event\.preventDefault\(\); alert\(\'Thank you for subscribing!\'\);">'
    new3 = f'<form action="{NEWSLETTER_ENDPOINT}" method="POST" class="csoai-form" data-form-type="newsletter">'
    text = re.sub(old3, new3, text)
    
    return text

def add_form_handler_script(text):
    """Add client-side form handling script before closing </body> if not present."""
    if 'id="form-success"' in text or 'csoai-form-handler' in text:
        return text
    
    script = '''
<script>
/* CSOAI Form Handler — intercepts Formspree submissions for smoother UX */
document.querySelectorAll('.csoai-form').forEach(function(form){
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    var originalText = btn ? btn.textContent : 'Submit';
    if(btn){ btn.disabled = true; btn.textContent = 'Sending…'; }
    var formType = form.dataset.formType || 'contact';
    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    }).then(function(r){ return r.json(); }).then(function(data){
      if(data && data.ok){
        form.innerHTML = '<div style="padding:1.5rem;background:rgba(212,168,67,0.08);border:1px solid rgba(212,168,67,0.2);border-radius:12px;text-align:center;"><p style="color:#D4A843;font-weight:600;margin-bottom:0.5rem;">' + (formType === 'newsletter' ? 'You\'re subscribed!' : 'Message sent!') + '</p><p style="color:rgba(232,228,240,0.7);font-size:0.9rem;">' + (formType === 'newsletter' ? 'Thanks for joining the CSOAI community.' : 'We\'ll be in touch within 24 hours.') + '</p></div>';
      } else {
        throw new Error('Formspree error');
      }
    }).catch(function(){
      if(btn){ btn.disabled = false; btn.textContent = originalText; }
      var err = form.querySelector('.form-error');
      if(!err){
        err = document.createElement('p');
        err.className = 'form-error';
        err.style.cssText = 'color:#ff6b6b;margin-top:0.75rem;font-size:0.9rem;';
        err.textContent = 'Something went wrong. Please try again or email us directly at support@csoai.org';
        form.appendChild(err);
      }
    });
  });
});
</script>
'''
    text = text.replace('</body>', script + '</body>')
    return text

# Process all HTML files
files = sorted(glob.glob('*.html'))
for fname in files:
    with open(fname) as f:
        text = f.read()
    
    original = text
    text = replace_contact_form(text)
    text = replace_newsletter_form(text)
    
    # Only add script if we actually changed a form
    if text != original:
        text = add_form_handler_script(text)
    
    if text != original:
        with open(fname, 'w') as f:
            f.write(text)
        print(f'Updated {fname}')
    else:
        print(f'No changes {fname}')
