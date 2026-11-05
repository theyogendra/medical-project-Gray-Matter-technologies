import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
    title: 'Medical Web Application',
    description: 'Healthcare application scaffold with Next.js, Supabase, Prisma and AI services.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    );
}
