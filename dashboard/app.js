const data = window.SAKA_DATA || {};

function text(value, fallback = '') {
  if (value === undefined || value === null || value === '') return fallback;
  return String(value);
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = String(value);
}

function card(item, options = {}) {
  const article = document.createElement('article');
  article.className = 'card';

  const tag = document.createElement('div');
  tag.className = 'tag';
  tag.textContent = text(item.priority || item.status || item.type, 'item');

  const title = document.createElement('h3');
  title.textContent = text(item.name || item.title || item.hook, 'Untitled');

  const body = document.createElement('p');
  body.textContent = text(item.next_action || item.cta || item.hook || item.description, 'No next action yet.');

  article.append(tag, title, body);

  if (options.meta) {
    const meta = document.createElement('p');
    meta.className = 'meta';
    meta.textContent = options.meta(item);
    article.appendChild(meta);
  }

  return article;
}

function renderList(id, rows, cardFactory) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerHTML = '';
  if (!Array.isArray(rows) || rows.length === 0) {
    const empty = document.createElement('div');
    empty.className = 'empty';
    empty.textContent = 'No items yet. Add demo data and run scripts/sync_dashboard_data.py.';
    el.appendChild(empty);
    return;
  }
  rows.forEach((row) => el.appendChild(cardFactory(row)));
}

const projects = Array.isArray(data.projects) ? data.projects : [];
const content = Array.isArray(data.content_pipeline) ? data.content_pipeline : [];
const opportunities = Array.isArray(data.opportunities) ? data.opportunities : [];

setText('projectCount', projects.length);
setText('contentCount', content.length);
setText('opportunityCount', opportunities.length);

renderList('projects', projects, (item) => card(item, { meta: (x) => `Owner: ${text(x.owner, 'operator')} · Status: ${text(x.status, 'unknown')}` }));
renderList('content', content, (item) => card(item, { meta: (x) => `${text(x.brand, 'Demo')} · ${text(x.channel, 'channel')} · ${text(x.status, 'draft')}` }));
renderList('opportunities', opportunities, (item) => card(item, { meta: (x) => `Status: ${text(x.status, 'watch')}` }));
