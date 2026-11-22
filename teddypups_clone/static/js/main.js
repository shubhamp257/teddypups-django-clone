// Small progressive enhancement: smooth in-page navigation and button feedback.
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', event => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) { event.preventDefault(); target.scrollIntoView({behavior:'smooth'}); }
    });
  });
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', () => {
      const button = form.querySelector('button[type="submit"]');
      if (button) { button.disabled = true; button.textContent = 'Sending…'; }
    });
  });
});
