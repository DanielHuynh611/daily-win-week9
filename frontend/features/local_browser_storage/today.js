/* One page, one account-owned win for the current local calendar day. */
document.addEventListener('DOMContentLoaded', () => {
  'use strict';
  const panel = document.getElementById('daily-win');
  const form = document.getElementById('win-form');
  const input = document.getElementById('achievement');
  const button = document.getElementById('save-win');
  const status = document.getElementById('win-status');
  const error = document.getElementById('win-error');
  const retry = document.getElementById('retry-load');
  const saved = document.getElementById('saved-win');
  const endpoint = '/api/capability_local_browser_storage_99d93461/wins';
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
  let currentDay = '', busy = false, recorded = false, loaded = false;
  function localDay() {
    const now = new Date();
    return [now.getFullYear(), String(now.getMonth() + 1).padStart(2, '0'), String(now.getDate()).padStart(2, '0')].join('-');
  }
  function showStatus(message) { status.textContent = message; status.hidden = !message; }
  function setBusy(value) {
    busy = value;
    panel.setAttribute('aria-busy', String(value));
    button.disabled = value || recorded || !loaded;
    input.disabled = value;
    retry.disabled = value;
    button.textContent = value && !form.hidden ? 'Saving…' : "Save today's win";
  }
  function count() { document.getElementById('win-count').textContent = `${input.value.length} / 150`; }
  function showWin(win, justSaved = false) {
    recorded = Boolean(win);
    form.hidden = recorded;
    saved.hidden = !recorded;
    document.getElementById('saved-text').textContent = win?.achievement_text || '';
    showStatus(recorded ? (justSaved ? "Today's win saved." : "You've recorded today's win.") : '');
  }
  async function request(url, options = {}) {
    const response = await fetch(url, {
      credentials: 'same-origin', ...options,
      headers: { 'X-Time-Zone': zone, 'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').content, ...options.headers },
    });
    if (response.status === 401) { location.assign('/login'); throw Error('Please sign in to continue.'); }
    const payload = await response.json();
    if (!response.ok) {
      const failure = new Error(payload.message || 'Unable to save. Please try again.');
      failure.status = response.status;
      throw failure;
    }
    return payload;
  }
  function updateDate() {
    currentDay = localDay();
    const label = document.getElementById('today-date');
    label.dateTime = currentDay;
    label.textContent = new Intl.DateTimeFormat(undefined, { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }).format(new Date());
  }
  async function load() {
    if (busy) return;
    updateDate();
    loaded = false;
    form.hidden = true;
    saved.hidden = true;
    retry.hidden = true;
    error.hidden = true;
    showStatus("Loading today's win…");
    setBusy(true);
    try {
      const payload = await request(`${endpoint}/check?date=${currentDay}`);
      loaded = true;
      showWin(payload.win);
    } catch (failure) {
      showStatus('');
      error.textContent = 'Unable to load your win. Check your connection and try again.';
      error.hidden = false;
      retry.hidden = false;
    } finally { setBusy(false); }
    if (loaded && localDay() !== currentDay) await load();
  }
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (busy || recorded || !loaded) return;
    if (localDay() !== currentDay) {
      await load();
      if (loaded && !recorded) showStatus('A new day has started. Review your win before saving it for today.');
      return;
    }
    const text = input.value.trim();
    error.hidden = true;
    if (!text) {
      error.textContent = 'Write a short win before saving.';
      error.hidden = false;
      input.focus();
      return;
    }
    setBusy(true);
    let duplicate = false;
    try {
      const win = await request(endpoint, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ achievement_text: text, date: currentDay }),
      });
      showWin(win, true);
    } catch (failure) {
      duplicate = failure.status === 409;
      if (!duplicate) {
        error.textContent = failure.status ? failure.message : 'Unable to save. Your text is still here. Check your connection and try again.';
        error.hidden = false;
      }
    } finally { setBusy(false); }
    if (duplicate || localDay() !== currentDay) await load();
  });
  input.addEventListener('input', count);
  retry.addEventListener('click', load);
  function rollover() { if (!busy && localDay() !== currentDay) load(); }
  setInterval(rollover, 30000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) rollover(); });
  load();
});
