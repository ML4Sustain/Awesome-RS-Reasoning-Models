'use client';

import { useEffect, useState } from 'react';

type Theme = 'light' | 'dark';

function preferredTheme(): Theme {
  const saved = window.localStorage.getItem('rs-theme');
  if (saved === 'light' || saved === 'dark') return saved;
  return 'light';
}

export default function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>('dark');

  useEffect(() => {
    const next = preferredTheme();
    document.documentElement.dataset.theme = next;
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', next === 'light' ? '#edf6f3' : '#031522');
    setTheme(next);
  }, []);

  const toggle = () => {
    const next = theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content', next === 'light' ? '#edf6f3' : '#031522');
    window.localStorage.setItem('rs-theme', next);
    setTheme(next);
  };

  return <button className="theme-toggle" type="button" onClick={toggle} aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`} title={`Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`}><span aria-hidden="true">{theme === 'dark' ? '☼' : '◐'}</span><b>{theme === 'dark' ? 'Light' : 'Dark'}</b></button>;
}
