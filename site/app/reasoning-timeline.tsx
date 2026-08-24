'use client';

import { useMemo, useState, type CSSProperties } from 'react';
import payload from './catalog-data.json';

const lanes = [
  { name: 'Supervised', color: '#55d6be' },
  { name: 'Reinforcement', color: '#f6bd60' },
  { name: 'Agentic / tools', color: '#e78ac3' },
] as const;

type Lane = typeof lanes[number]['name'];
type Filter = 'All' | Lane;

const start = new Date('2025-01-01T00:00:00Z').getTime();
const end = new Date('2026-02-01T00:00:00Z').getTime();
const months = Array.from({ length: 14 }, (_, index) => new Date(Date.UTC(2025, index, 1)));

export default function ReasoningTimeline() {
  const [filter, setFilter] = useState<Filter>('All');
  const [selected, setSelected] = useState<string | null>(null);

  const entries = useMemo(() => payload.timeline.map((item, index) => {
    const sameMonth = payload.timeline.filter((other) => other.mechanism === item.mechanism && other.date.slice(0, 7) === item.date.slice(0, 7));
    const slot = sameMonth.findIndex((other) => other.name === item.name);
    return { ...item, index, x: 4 + ((new Date(`${item.date}T00:00:00Z`).getTime() - start) / (end - start)) * 92, slot };
  }), []);

  return (
    <div className="interactive-timeline">
      <div className="timeline-controls" aria-label="Filter timeline">
        {(['All', ...lanes.map((lane) => lane.name)] as Filter[]).map((item) => <button key={item} className={filter === item ? 'active' : ''} onClick={() => setFilter(item)}>{item}</button>)}
        <span>Hover or tap a node</span>
      </div>
      <div className="timeline-scroll">
        <div className="timeline-canvas">
          <div className="month-axis">{months.map((month) => <span key={month.toISOString()} style={{ left: `${4 + ((month.getTime() - start) / (end - start)) * 92}%` }}>{month.getUTCMonth() === 0 ? <><b>{month.getUTCFullYear()}</b><small>Jan</small></> : <small>{month.toLocaleString('en', { month: 'short', timeZone: 'UTC' })}</small>}</span>)}</div>
          {months.map((month) => <i className="month-line" key={`line-${month.toISOString()}`} style={{ left: `${4 + ((month.getTime() - start) / (end - start)) * 92}%` }} />)}
          {lanes.map((lane, laneIndex) => <div className={`timeline-lane lane-${laneIndex} ${filter !== 'All' && filter !== lane.name ? 'muted' : ''}`} key={lane.name} style={{ '--lane-color': lane.color } as CSSProperties}>
            <strong><i />{lane.name}</strong><span className="lane-rule" />
            {entries.filter((item) => item.mechanism === lane.name).map((item) => {
              const open = selected === `${item.name}-${item.date}`;
              const size = Math.min(22, 10 + Math.sqrt(item.stars) * .55);
              return <button className={`timeline-node ${open ? 'selected' : ''}`} key={`${item.name}-${item.date}`} style={{ left: `${item.x}%`, top: `${42 + item.slot * 27}px`, width: size, height: size }} onClick={() => setSelected(open ? null : `${item.name}-${item.date}`)} aria-label={`${item.name}, ${item.date}, ${item.stars} stars`}>
                <span className="node-label">{item.name}</span>
                <span className="node-popover"><b>{item.name}</b><small>{new Date(`${item.date}T00:00:00Z`).toLocaleDateString('en', { year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC' })} · {lane.name}</small><em>{item.stars ? `${item.stars.toLocaleString()} stored Stars` : 'No repository snapshot'}</em><span><a href={item.paper} target="_blank" rel="noreferrer">Paper ↗</a>{item.repo && <a href={item.repo} target="_blank" rel="noreferrer">Code ↗</a>}</span></span>
              </button>;
            })}
          </div>)}
          <div className="timeline-legend"><span><i /> first public release</span><span>Node size = stored repository Stars</span><b>{entries.length} tracked releases</b></div>
        </div>
      </div>
    </div>
  );
}
