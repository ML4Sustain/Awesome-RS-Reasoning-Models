import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';

const geistSans = Geist({ variable: '--font-geist-sans', subsets: ['latin'] });
const geistMono = Geist_Mono({ variable: '--font-geist-mono', subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Awesome RS Reasoning',
  description: 'From perception outputs to traceable geospatial decisions.',
  icons: { icon: '/favicon.svg', shortcut: '/favicon.svg' },
  openGraph: {
    title: 'Awesome RS Reasoning',
    description: 'From perception outputs to traceable geospatial decisions.',
    type: 'website',
    images: [{ url: 'https://rs-reasoning-index.jaychempan.chatgpt.site/og.png', width: 1200, height: 630, alt: 'Awesome RS Reasoning' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Awesome RS Reasoning',
    description: 'From perception outputs to traceable geospatial decisions.',
    images: ['https://rs-reasoning-index.jaychempan.chatgpt.site/og.png'],
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body className={`${geistSans.variable} ${geistMono.variable}`}>{children}</body></html>;
}
