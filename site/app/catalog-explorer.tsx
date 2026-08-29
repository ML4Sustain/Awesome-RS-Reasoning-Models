'use client';

import { useEffect, useMemo, useRef, useState } from 'react';
import payload from './catalog-data.json';

type Tab = 'all' | 'reasoning' | 'foundations' | 'data';
const tabs: { key: Tab; label: string }[] = [
  { key: 'all', label: 'All resources' },
  { key: 'reasoning', label: 'Reasoning systems' },
  { key: 'foundations', label: 'Enabling foundations' },
  { key: 'data', label: 'Data & benchmarks' },
];

export default function CatalogExplorer() {
  const [tab, setTab] = useState<Tab>('all');
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('All categories');
  const [sort, setSort] = useState<'stars' | 'newest' | 'name'>('stars');
  const [limit, setLimit] = useState(18);
  const searchRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    function focusSearch(event: KeyboardEvent) {
      if (event.key === '/' && document.activeElement?.tagName !== 'INPUT') {
        event.preventDefault();
        searchRef.current?.focus();
      }
    }
    window.addEventListener('keydown', focusSearch);
    return () => window.removeEventListener('keydown', focusSearch);
  }, []);

  const categories = useMemo(() => {
    const values = tab === 'data'
      ? payload.datasets.map((item) => item.kind)
      : payload.methods.filter((item) => tab !== 'reasoning' || item.family === 'Reasoning Models').map((item) => item.category);
    return ['All categories', ...Array.from(new Set(values)).sort()];
  }, [tab]);

  const items = useMemo(() => {
    const needle = query.trim().toLowerCase();
    if (tab === 'data') {
      return payload.datasets.filter((item) =>
        (category === 'All categories' || item.kind === category) &&
        (!needle || `${item.name} ${item.kind} ${item.model} ${item.focus}`.toLowerCase().includes(needle))
      ).sort((a, b) => sort === 'name' ? a.name.localeCompare(b.name) : Number(b.year) - Number(a.year)).map((item) => ({ ...item, type: 'data' as const }));
    }
    return payload.methods.filter((item) => {
      const familyMatch = tab === 'all' || (tab === 'reasoning' ? item.family === 'Reasoning Models' : item.family !== 'Reasoning Models');
      return familyMatch && (category === 'All categories' || item.category === category) && (!needle || `${item.name} ${item.family} ${item.category} ${item.venue}`.toLowerCase().includes(needle));
    }).sort((a, b) => sort === 'name' ? a.name.localeCompare(b.name) : sort === 'newest' ? Number(b.year) - Number(a.year) || b.stars - a.stars : b.stars - a.stars || Number(b.year) - Number(a.year)).map((item) => ({ ...item, type: 'method' as const }));
  }, [tab, query, category, sort]);

  const orderNote = sort === 'stars'
    ? 'Order: stored Stars · newest first on ties'
    : sort === 'newest'
      ? 'Order: newest release year first'
      : 'Order: resource name A–Z';

  function changeTab(next: Tab) { setTab(next); setCategory('All categories'); if (next === 'data' && sort === 'stars') setSort('newest'); setLimit(18); }

  return (
    <section className="catalog shell" id="catalog">
      <div className="catalog-head">
        <div><p className="kicker">Curated catalog</p><h2>Explore the landscape</h2></div>
        <p>Search methods, models, agents, datasets, and benchmarks. Every record links to a paper, official repository, or release page.</p>
      </div>
      <div className="catalog-tools">
        <div className="tabs" role="tablist" aria-label="Resource type">
          {tabs.map((item) => <button className={tab === item.key ? 'active' : ''} key={item.key} onClick={() => changeTab(item.key)}>{item.label}</button>)}
        </div>
        <div className="filters">
          <label className="search"><span>⌕</span><input ref={searchRef} value={query} onChange={(event) => { setQuery(event.target.value); setLimit(18); }} placeholder="Search models, datasets, tasks…" aria-label="Search resources" /><kbd>/</kbd></label>
          <select value={category} onChange={(event) => { setCategory(event.target.value); setLimit(18); }} aria-label="Filter by category">
            {categories.map((item) => <option key={item}>{item}</option>)}
          </select>
          <select value={sort} onChange={(event) => setSort(event.target.value as 'stars' | 'newest' | 'name')} aria-label="Sort resources">
            {tab !== 'data' && <option value="stars">Most starred</option>}
            <option value="newest">Newest first</option>
            <option value="name">Name A–Z</option>
          </select>
        </div>
      </div>
      <div className="result-meta"><span>{items.length} results</span>{(query || category !== 'All categories') && <button onClick={() => { setQuery(''); setCategory('All categories'); }}>Clear filters</button>}<span className="sort-note">{orderNote}</span><span>Stars snapshot · {payload.updated}</span></div>
      <div className="resource-grid">
        {items.slice(0, limit).map((item, index) => item.type === 'method' ? (
          <article className="resource-card" key={`${item.name}-${item.year}`}>
            <div className="card-meta"><span title={item.category}><b className="card-sequence">{String(index + 1).padStart(2, '0')}</b>{item.category}</span><span title={`${item.year} · ${item.venue}`}>{item.year} · {item.venue}</span></div>
            <h3>{item.name}</h3>
            <p>{item.family === 'Reasoning Models' ? 'Reasoning-specific system' : item.family}</p>
            <div className="card-links">
              {item.paper && <a href={item.paper} target="_blank" rel="noreferrer">Paper ↗</a>}
              {item.repo && <a href={item.repo} target="_blank" rel="noreferrer">Code ↗</a>}
              {item.downloads[0] && <a href={item.downloads[0].url} target="_blank" rel="noreferrer">{item.downloads[0].label} ↗</a>}
              {item.repo && <span>{item.stars.toLocaleString()} stars</span>}
            </div>
          </article>
        ) : (
          <article className="resource-card data-card" key={item.name}>
            <div className="card-meta"><span><b className="card-sequence">{String(index + 1).padStart(2, '0')}</b>{item.kind}</span><span>{item.year}</span></div>
            <h3>{item.name}</h3><p>{item.focus}</p>
            <div className="card-links"><a href={item.url} target="_blank" rel="noreferrer">{item.label} ↗</a><span>Companion · {item.model}</span></div>
          </article>
        ))}
      </div>
      {!items.length && <div className="empty">No matching resources. Try a broader term or category.</div>}
      {limit < items.length && <button className="load-more" onClick={() => setLimit((value) => value + 18)}>Show more <span>{items.length - limit}</span></button>}
    </section>
  );
}
