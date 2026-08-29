'use client';

import { useMemo, useState, type CSSProperties } from 'react';
import payload from './catalog-data.json';

const lanes = [
  { name: 'Supervised', color: '#55d1b9' },
  { name: 'Reinforcement', color: '#ffc447' },
  { name: 'Agentic / tools', color: '#e47691' },
] as const;

type Lane = typeof lanes[number]['name'];
type Filter = 'All' | Lane;

const releaseDates = payload.timeline.map((item) => new Date(`${item.date}T00:00:00Z`));
const firstRelease = new Date(Math.min(...releaseDates.map((date) => date.getTime())));
const lastRelease = new Date(Math.max(...releaseDates.map((date) => date.getTime())));
const startDate = new Date(Date.UTC(firstRelease.getUTCFullYear(), firstRelease.getUTCMonth(), 1));
const endDate = new Date(Date.UTC(lastRelease.getUTCFullYear(), lastRelease.getUTCMonth() + 1, 1));
const start = startDate.getTime();
const end = endDate.getTime();
const monthCount = (endDate.getUTCFullYear() - startDate.getUTCFullYear()) * 12 + endDate.getUTCMonth() - startDate.getUTCMonth();
const months = Array.from({ length: monthCount }, (_, index) => new Date(Date.UTC(startDate.getUTCFullYear(), startDate.getUTCMonth() + index, 1)));

function placeLabels(items: typeof payload.timeline) {
  const rowEnds = [-Infinity, -Infinity, -Infinity, -Infinity];

  return [...items].sort((a, b) => a.date.localeCompare(b.date)).map((item) => {
    const x = 4 + ((new Date(`${item.date}T00:00:00Z`).getTime() - start) / (end - start)) * 92;
    const labelWidth = Math.min(11, Math.max(4.2, item.name.length * .53));
    const labelLeft = x > 84;
    const intervalStart = labelLeft ? x - labelWidth : x;
    const intervalEnd = labelLeft ? x : x + labelWidth;
    let row = rowEnds.findIndex((endAt) => intervalStart > endAt + .8);

    if (row < 0) row = rowEnds.indexOf(Math.min(...rowEnds));
    rowEnds[row] = intervalEnd;
    return { ...item, x, row, labelLeft };
  });
}

export default function ReasoningTimeline() {
  const [filter, setFilter] = useState<Filter>('All');
  const [selected, setSelected] = useState<string | null>(null);

  const entries = useMemo(() => lanes.flatMap((lane) => placeLabels(payload.timeline.filter((item) => item.mechanism === lane.name))), []);

  return (
    <div className="interactive-timeline">
      <div className="timeline-controls" aria-label="Filter timeline">
        {(['All', ...lanes.map((lane) => lane.name)] as Filter[]).map((item) => <button key={item} className={`${filter === item ? 'active' : ''} filter-${item.toLowerCase().replace(/[^a-z]+/g, '-')}`} onClick={() => setFilter(item)}>{item}</button>)}
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
              return <button className={`timeline-node ${item.labelLeft ? 'label-left' : ''} ${open ? 'selected' : ''}`} key={`${item.name}-${item.date}`} style={{ left: `${item.x}%`, top: `${46 + item.row * 25}px`, width: size, height: size }} onClick={() => setSelected(open ? null : `${item.name}-${item.date}`)} aria-label={`${item.name}, ${item.date}, ${item.stars} stars`}>
                <span className="node-label" title={item.name}>{item.name}</span>
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
