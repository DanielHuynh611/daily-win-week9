/* Read-only history reuses the existing account-scoped records API. */
document.addEventListener('DOMContentLoaded', () => {
  'use strict';
  const section = document.getElementById('win-history');
  const list = document.getElementById('history-list');
  const summary = document.getElementById('history-summary');
  const error = document.getElementById('history-error');
  const retry = document.getElementById('history-retry');
  const more = document.getElementById('history-more');
  const empty = document.getElementById('history-empty');
  let records = [], shown = 0, busy = false;
  function appendBatch() {
    const batch = records.slice(shown, shown + 10);
    for (const win of batch) {
      const item = document.createElement('li');
      item.className = 'z-panel';
      const body = document.createElement('div');
      body.className = 'z-panel-body';
      const date = document.createElement('time');
      date.className = 'daily-date';
      date.dateTime = win.date;
      // Calendar dates are not timestamps: avoid shifting them across time zones.
      const [year, month, day] = win.date.split('-').map(Number);
      date.textContent = new Intl.DateTimeFormat(undefined, { day: 'numeric', month: 'long', year: 'numeric' }).format(new Date(year, month - 1, day, 12));
      const text = document.createElement('p');
      text.textContent = win.achievement_text;
      body.append(date, text);
      item.append(body);
      list.append(item);
    }
    shown += batch.length;
    more.hidden = shown >= records.length;
  }
  async function load() {
    if (busy) return;
    busy = true;
    section.setAttribute('aria-busy', 'true');
    retry.disabled = true;
    retry.hidden = true;
    error.hidden = true;
    empty.hidden = true;
    more.hidden = true;
    summary.textContent = 'Loading your wins…';
    try {
      const response = await fetch('/api/capability_local_browser_storage_99d93461/wins', { credentials: 'same-origin' });
      if (response.status === 401) { location.assign('/login'); return; }
      if (!response.ok) throw Error('Unable to load history.');
      const payload = await response.json();
      records = payload.wins.sort((a, b) => b.date.localeCompare(a.date));
      shown = 0;
      list.replaceChildren();
      summary.textContent = `${records.length} ${records.length === 1 ? 'win' : 'wins'} recorded · Newest first`;
      empty.hidden = records.length > 0;
      appendBatch();
    } catch (_) {
      summary.textContent = '';
      error.textContent = 'Unable to load your wins. Check your connection and try again.';
      error.hidden = false;
      retry.hidden = false;
    } finally {
      busy = false;
      retry.disabled = false;
      section.setAttribute('aria-busy', 'false');
    }
  }
  more.addEventListener('click', appendBatch);
  retry.addEventListener('click', load);
  load();
});
