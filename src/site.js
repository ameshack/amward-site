(function () {
  var body = document.body;
  var root = body.getAttribute('data-root') || '';
  var ext = body.getAttribute('data-ext') || '';

  // Links from the old single-page site (#brand, #experience, ...) land on the new pages.
  if (body.getAttribute('data-page') === 'home') {
    var legacy = {
      'brand': 'brand/', 'product-marketing': 'product-marketing/',
      'internal-exec-comms': 'communications/', 'leadership-ops': 'leadership/',
      'experience': 'about/#experience', 'credentials': 'about/#credentials',
      'technology-ai': 'about/#technology-ai', 'applied-ai': 'about/#technology-ai'
    };
    var target = legacy[location.hash.slice(1)];
    if (target) {
      var parts = target.split('#');
      location.replace(root + parts[0] + ext + (parts[1] ? '#' + parts[1] : ''));
      return;
    }
  }

  // Review copy only: switch between the two visual directions.
  var switches = document.querySelectorAll('.variant-switch button');
  function setVariant(v) {
    if (v === 'crisp') body.setAttribute('data-variant', 'crisp'); else body.removeAttribute('data-variant');
    switches.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-variant') === v ? 'true' : 'false'); });
    try { localStorage.setItem('amward-variant', v); } catch (err) {}
  }
  if (switches.length) {
    var saved = 'warm';
    try { saved = localStorage.getItem('amward-variant') || 'warm'; } catch (err) {}
    setVariant(saved);
    switches.forEach(function (b) { b.addEventListener('click', function () { setVariant(b.getAttribute('data-variant')); }); });
  }

  // Work dropdown (desktop)
  var workBtn = document.querySelector('.nav-work-btn');
  var workMenu = document.getElementById('work-menu');
  function setWork(open) {
    if (!workBtn) return;
    workBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    workMenu.hidden = !open;
  }
  if (workBtn) {
    workBtn.addEventListener('click', function () { setWork(workMenu.hidden); });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-work')) setWork(false);
    });
    workMenu.addEventListener('focusout', function (e) {
      if (!e.relatedTarget || !e.relatedTarget.closest('.nav-work')) setWork(false);
    });
  }

  // Mobile menu
  var menuBtn = document.querySelector('.menu-btn');
  var panel = document.getElementById('mobile-panel');
  function setMenu(open) {
    if (!menuBtn) return;
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.textContent = open ? 'Close' : 'Menu';
    panel.classList.toggle('open', open);
  }
  if (menuBtn) {
    menuBtn.addEventListener('click', function () { setMenu(!panel.classList.contains('open')); });
    panel.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (workBtn && !workMenu.hidden) { setWork(false); workBtn.focus(); }
    if (menuBtn && panel.classList.contains('open')) { setMenu(false); menuBtn.focus(); }
  });

  // Open a project's details when its link is followed (brand/#reuse-sf).
  function openFromHash() {
    var el = location.hash && document.getElementById(location.hash.slice(1));
    var details = el && el.querySelector('details.more');
    if (details) details.open = true;
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);

  // Email: the address is assembled only when a visitor asks for it.
  var reveal = document.getElementById('reveal');
  if (reveal) {
    var addr = document.getElementById('email');
    var copy = document.getElementById('copy');
    var status = document.getElementById('status');
    reveal.addEventListener('click', function () {
      var t = [109,111,99,46,108,105,97,109,103,64,107,99,97,104,115,101,109,46,97,105,115,97]
        .reverse().map(function (c) { return String.fromCharCode(c); }).join('');
      addr.textContent = t; addr.hidden = false; copy.hidden = false; reveal.hidden = true;
      status.textContent = 'Opening your email app. If nothing opens, copy the address.';
      try { var a = document.createElement('a'); a.href = 'mai' + 'lto:' + t; a.click(); } catch (err) {}
    });
    copy.addEventListener('click', function () {
      var t = addr.textContent;
      function select() {
        var r = document.createRange(); r.selectNodeContents(addr);
        var s = getSelection(); s.removeAllRanges(); s.addRange(r);
        status.textContent = 'Address selected';
      }
      try { navigator.clipboard.writeText(t).then(function () { status.textContent = 'Copied'; }, select); }
      catch (err) { select(); }
    });
  }
})();
