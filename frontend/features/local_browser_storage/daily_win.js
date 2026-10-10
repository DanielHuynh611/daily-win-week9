/* Connect the original generated screen to real, account-owned records. */
document.addEventListener('DOMContentLoaded', () => {
  'use strict';
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
  function today() {
    const now = new Date();
    return [now.getFullYear(), String(now.getMonth() + 1).padStart(2, '0'), String(now.getDate()).padStart(2, '0')].join('-');
  }
  let currentDay = today();
  const form = document.querySelector('form[data-action-id$=".save_achievement"]');
  const check = document.querySelector('[data-action-id$=".check_today_entry"]');
  const listing = document.querySelector('[data-action-id$=".load_today_win"]');
  const confirmation = location.pathname === '/confirmation';
  const dateFields = [...document.querySelectorAll('input[type="date"]')];
  dateFields.forEach(field => {
    field.value = currentDay;
    field.max = currentDay;
  });
  const entryDate = form?.querySelector('[name="date"]');
  if (entryDate) entryDate.readOnly = true;

  function lock(recorded) {
    if (!form) return;
    form.dataset.winRecorded = String(recorded);
    const text = form.querySelector('[name="achievement_text"]');
    const submit = form.querySelector('[type="submit"]');
    if (text) text.disabled = recorded;
    if (submit) submit.disabled = recorded;
  }
  function showRecords(root, records, emptyMessage) {
    const content = root?.querySelector('[data-response-content]');
    if (!content) return;
    const paragraphs = records.map(win => {
      const node = document.createElement('p');
      node.className = 'z-result-state';
      node.textContent = `${win.date ? win.date + ' · ' : ''}${win.achievement_text || win.text}`;
      return node;
    });
    if (!paragraphs.length) {
      const node = document.createElement('p');
      node.className = 'z-result-state';
      node.textContent = emptyMessage;
      paragraphs.push(node);
    }
    content.replaceChildren(...paragraphs);
  }
  function refresh() {
    [check, listing].forEach(root => root?.querySelector('[data-reload]')?.click());
  }
  document.addEventListener('dailywin:response', event => {
    const { root, payload, action } = event.detail;
    if (root === check) {
      const selected = check.querySelector('[name="date"]').value;
      showRecords(check, payload.win ? [payload.win] : [], 'No win recorded for this date.');
      if (selected === currentDay) {
        lock(payload.exists);
        if (payload.win && form) form.querySelector('[name="achievement_text"]').value = payload.win.achievement_text;
      }
    } else if (root === listing) {
      showRecords(listing, payload.wins || [], 'No saved wins for this date.');
    } else if (root === form && action.method === 'POST') {
      lock(true);
      const success = form.querySelector('[data-success-region]');
      if (success) success.textContent = `Today's win saved! ${payload.achievement_text}`;
      refresh();
    }
  });
  document.addEventListener('dailywin:error', event => {
    if (event.detail.status === 409) {
      lock(true);
      refresh();
    }
  });
  // A tab left open across midnight advances to the new local calendar day.
  function rollover() {
    const nextDay = today();
    if (nextDay === currentDay) return;
    currentDay = nextDay;
    dateFields.forEach(field => { field.value = nextDay; field.max = nextDay; });
    lock(false);
    form?.querySelectorAll('[data-success-region],[data-error-region]').forEach(node => { node.hidden = true; });
    refresh();
  }
  setInterval(rollover, 30000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) rollover(); });
  form?.addEventListener('submit', rollover, { capture: true });

  if (confirmation) {
    fetch('/api/capability_local_browser_storage_99d93461/wins/check?date=' + currentDay, {
      credentials: 'same-origin', headers: { 'X-Time-Zone': zone },
    }).then(async response => {
      if (response.status === 401) { location.assign('/login'); return; }
      const payload = await response.json();
      if (!response.ok) throw Error(payload.message || 'Unable to load your win.');
      const panel = document.querySelector('.z-panel-body') || document.querySelector('.z-main .z-stack');
      if (panel) {
        const message = document.createElement('p');
        message.className = 'z-result-state';
        message.textContent = payload.win ? `Today's win saved! ${payload.win.achievement_text}` : 'No win recorded for today.';
        panel.append(message);
      }
    }).catch(() => {
      const panel = document.querySelector('.z-main');
      if (panel) {
        const error = document.createElement('p');
        error.className = 'z-result-state z-result-state--error';
        error.setAttribute('role', 'alert');
        error.textContent = 'Unable to load your win. Please refresh and try again.';
        panel.append(error);
      }
    });
  }
});
