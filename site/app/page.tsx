import CatalogExplorer from './catalog-explorer';
import payload from './catalog-data.json';
import ThemeToggle from './theme-toggle';
import ReasoningTimeline from './reasoning-timeline';

const tracks = [
  { number: '01', label: 'Supervised reasoning', count: 6, tone: 'mint' },
  { number: '02', label: 'Reinforcement reasoning', count: 14, tone: 'amber' },
  { number: '03', label: 'Agentic & tool use', count: 7, tone: 'rose' },
];

export default function Home() {
  return (
    <main>
      <header className="site-top shell" id="top">
        <nav className="nav">
          <a className="brand" href="#top" aria-label="Awesome RS Reasoning home"><span className="brand-mark" aria-hidden="true"><i /></span><span><b>Awesome RS</b><small>Reasoning</small></span></a>
          <div className="nav-links"><a href="#systems">Systems</a><a href="#timeline">Timeline</a><a href="#catalog">Catalog</a><a href="#foundations">Foundations</a></div>
          <div className="nav-actions"><ThemeToggle /><a className="repo-link" href="https://github.com/ML4Sustain/Awesome-RS-Reasoning-Models">GitHub ↗</a></div>
        </nav>
        <section className="hero">
          <div className="hero-content">
            <div className="eyebrow"><span /> Living survey companion</div>
            <h1>Awesome RS<br /><em>Reasoning</em></h1>
            <p className="hero-subline">Models · Datasets · Benchmarks · Agents</p>
            <p className="hero-copy">From perception outputs to traceable geospatial decisions.</p>
            <div className="hero-badges"><span>Living index</span><span>Star tracked</span><span>Evidence first</span></div>
            <div className="hero-actions"><a className="primary-action" href="#catalog">Explore {payload.stats.resources} resources</a><a className="text-action" href="https://www.preprints.org/frontend/manuscript/046ed51d5cc524d60bc9281a57caf963/download_pub" target="_blank" rel="noreferrer">Read survey preprint ↗</a></div>
          </div>
          <div className="orbital-scene" aria-hidden="true">
            <span className="orbit orbit-one" /><span className="orbit orbit-two" />
            <span className="planet"><i className="land land-one" /><i className="land land-two" /></span>
            <span className="satellite"><i /><b /><i /></span>
            <span className="signal" />
          </div>
        </section>
      </header>
      <nav className="jump-nav shell" aria-label="Quick navigation"><span>Jump to</span><a href="#systems">Reasoning paradigms</a><a href="#timeline">Reasoning wave</a><a href="#catalog">Resource catalog</a><a href="#foundations">Model foundations</a><a href="https://github.com/ML4Sustain/Awesome-RS-Reasoning-Models" target="_blank" rel="noreferrer">Contribute ↗</a></nav>
      <section className="pulse shell" aria-label="Index statistics">
        <div><strong>{payload.stats.resources}</strong><span>methods & models</span></div><div><strong>{payload.stats.reasoning}</strong><span>reasoning systems</span></div><div><strong>{payload.stats.datasets}</strong><span>datasets & benches</span></div><div><strong>{payload.stats.repositories}</strong><span>official repositories</span></div>
      </section>
      <section className="taxonomy shell" id="systems">
        <div className="section-heading"><p>Acquisition & execution</p><h2>Three non-exclusive<br />reasoning paradigms</h2><span>Classified by the dominant mechanism through which reasoning is learned or executed.</span></div>
        <div className="track-grid">
          {tracks.map((track) => <article className={`track ${track.tone}`} key={track.number}><span className="track-number">{track.number}</span><div><h3>{track.label}</h3><p>{track.count} systems</p></div><span className="arrow">↗</span></article>)}
        </div>
      </section>
      <section className="timeline-section shell" id="timeline">
        <div className="timeline-heading"><div><p>The reasoning wave</p><h2>From first release<br />to a growing field</h2></div><div><p>Methods are arranged by first public release and dominant reasoning mechanism. Node size reflects the stored repository Star snapshot.</p><a href="./timeline.svg" target="_blank" rel="noreferrer">Open full timeline ↗</a></div></div>
        <ReasoningTimeline />
      </section>
      <CatalogExplorer />
      <section className="preview shell" id="foundations"><p>Built on multimodal foundations</p><div className="preview-line"><span>Contrastive VLMs</span><b>07</b></div><div className="preview-line"><span>Generative large VLMs</span><b>14</b></div><div className="preview-line"><span>Task-specific VLMs</span><b>15</b></div></section>
      <footer className="shell" id="data"><a className="footer-brand" href="#top"><span className="brand-mark" aria-hidden="true"><i /></span><span><b>Awesome RS</b><small>Reasoning</small></span></a><span className="footer-meta"><span>Curated from the survey · Updated daily</span><img src="https://hits.sh/github.com/ML4Sustain/Awesome-RS-Reasoning-Models.svg?style=flat-square&amp;label=project%20views&amp;color=16858a&amp;labelColor=24292f" alt="Project view count" width="104" height="20" /></span></footer>
    </main>
  );
}
