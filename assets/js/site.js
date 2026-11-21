(function () {
  var root = document.documentElement;

  // Theme (light/dark), remembered per visitor
  try { var t = localStorage.getItem('fp-theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  document.querySelectorAll('.theme-toggle').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('fp-theme', next); } catch (e) {}
    });
  });

  // Mobile nav + mega menus
  var nav = document.querySelector('.nav'), burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
  document.querySelectorAll('.has-mega > button').forEach(function (b) {
    b.addEventListener('click', function () {
      var li = b.parentElement, open = li.classList.toggle('open');
      b.setAttribute('aria-expanded', open);
      document.querySelectorAll('.has-mega').forEach(function (o) { if (o !== li) o.classList.remove('open'); });
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') document.querySelectorAll('.has-mega.open').forEach(function (o) { o.classList.remove('open'); });
  });

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });

  // Team filter
  document.querySelectorAll('.filters').forEach(function (f) {
    var target = document.querySelector(f.dataset.target);
    f.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      f.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); });
      target.querySelectorAll('[data-office]').forEach(function (m) {
        m.hidden = !(b.dataset.f === 'all' || m.dataset.office.indexOf(b.dataset.f) > -1);
      });
    });
  });

  // Pre-select service / office from query string (e.g. devenir-client.html?service=paie)
  var qs = new URLSearchParams(location.search);
  ['service', 'bureau', 'secteur'].forEach(function (k) {
    var v = qs.get(k); if (!v) return;
    document.querySelectorAll('[name="' + k + '"]').forEach(function (el) {
      if (el.type === 'checkbox' || el.type === 'radio') { if (el.value === v) el.checked = true; }
      else el.value = v;
    });
  });

  // Forms
  var cfg = window.FIRMA_CONFIG || { endpoints: {}, offices: {}, defaultEmail: 'cpa@firmaplus.ca' };
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      if (form.querySelector('.hp input') && form.querySelector('.hp input').value) return; // honeypot
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var key = form.dataset.form, fd = new FormData(form);
      fd.append('source_page', location.pathname);
      var endpoint = cfg.endpoints[key];
      if (endpoint) {
        if (msg) msg.textContent = 'Envoi en cours…';
        fetch(endpoint, { method: 'POST', body: fd, mode: 'no-cors' })
          .then(function () { location.href = (document.body.dataset.root || '') + 'merci/'; })
          .catch(function () { if (msg) msg.textContent = 'Une erreur est survenue. Écrivez-nous à ' + cfg.defaultEmail + '.'; });
        return;
      }
      // Fallback: pre-filled email
      var office = cfg.offices[fd.get('bureau')], to = office ? office.email : cfg.defaultEmail;
      var lines = [], subject = form.dataset.subject || 'Demande — site Web';
      fd.forEach(function (v, k) {
        if (k === 'cv' || k === 'website' || v === '') return;
        lines.push(k.replace(/_/g, ' ') + ' : ' + v);
      });
      if (fd.get('entreprise')) subject += ' — ' + fd.get('entreprise');
      location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      if (msg) msg.textContent = 'Votre logiciel de courriel s’ouvre avec votre demande. Il ne reste qu’à l’envoyer.';
    });
  });

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
