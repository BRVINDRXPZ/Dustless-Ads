(() => {
  'use strict';
  window.prototypeDataLayer = window.prototypeDataLayer || [];
  const push = (event, extra = {}) => window.prototypeDataLayer.push({
    event,
    event_id: crypto.randomUUID?.() || String(Date.now()),
    page_path: location.pathname,
    prototype_only: true,
    ...extra
  });

  document.addEventListener('click', (e) => {
    const element = e.target.closest('[data-track]');
    if (element) push(element.dataset.track, { element_label: element.dataset.trackLabel || '' });
  });

  document.querySelectorAll('form').forEach((form) => {
    let started = false;
    form.addEventListener('input', () => {
      if (!started) {
        push('form_start', { form_id: form.id });
        started = true;
      }
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const status = form.querySelector('.status');
      if (form.elements.website?.value) {
        status.textContent = 'This prototype request was not accepted.';
        push('form_error', { form_id: form.id, error_code: 'honeypot' });
        return;
      }
      if (!form.checkValidity()) {
        form.reportValidity();
        status.textContent = 'Review the highlighted required fields. Nothing was sent.';
        push('form_error', { form_id: form.id, error_code: 'client_validation' });
        return;
      }
      status.textContent = 'Prototype validation passed. Nothing was sent or uploaded. A production system must securely validate and accept the request before recording a submission.';
      status.tabIndex = -1;
      status.focus();
      push('form_step_complete', { form_id: form.id, form_step: 'prototype_validation' });
    });
  });

  document.querySelectorAll('.tabs button').forEach((button) => button.addEventListener('click', () => {
    document.querySelectorAll('.tabs button').forEach((item) => item.setAttribute('aria-selected', 'false'));
    document.querySelectorAll('.inquiry').forEach((item) => { item.hidden = true; });
    button.setAttribute('aria-selected', 'true');
    document.getElementById(button.getAttribute('aria-controls')).hidden = false;
  }));
})();
