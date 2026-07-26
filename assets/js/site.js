(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('open', !open);
    });
  }

  const cfg = window.ARCHIVO21_CONFIG || {};
  const panel = document.querySelector('[data-contact-panel]');
  if (panel && cfg.contactRoutingActive && cfg.contacts) {
    const entries = [
      ['General enquiries', 'general', 'Project, collaboration and institutional enquiries.'],
      ['Conduct reports', 'conduct', 'Private Code of Conduct and safeguarding reports.'],
      ['Rights and attribution', 'rights', 'Attribution, permission, provenance and rights review.']
    ];
    panel.innerHTML = entries.map(([title, key, text]) => `
      <article class="card contact-card">
        <h2>${title}</h2>
        <p>${text}</p>
        <p class="address"><a href="mailto:${cfg.contacts[key]}">${cfg.contacts[key]}</a></p>
      </article>`).join('');
  }

  document.querySelectorAll('[data-contact-kind]').forEach(slot => {
    const kind = slot.getAttribute('data-contact-kind');
    if (cfg.contactRoutingActive && cfg.contacts && cfg.contacts[kind]) {
      const address = cfg.contacts[kind];
      slot.innerHTML = `<p>Email <a href="mailto:${address}">${address}</a>.</p>`;
    }
  });
})();
