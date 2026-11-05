export default function HomePage() {
    return (
        <main className="min-h-screen bg-slate-950 text-slate-50">
            <div className="mx-auto flex max-w-5xl flex-col gap-8 px-6 py-20">
                <div className="inline-flex w-fit rounded-full border border-brand-500/40 bg-brand-500/10 px-4 py-2 text-sm font-medium text-brand-100">
                    Medical Web Application
                </div>

                <section className="grid gap-8 lg:grid-cols-[1.3fr_0.7fr]">
                    <div className="space-y-6">
                        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
                            Healthcare platform foundation powered by Next.js and Supabase.
                        </h1>
                        <p className="max-w-2xl text-lg text-slate-300">
                            This scaffold is prepared for a medical application using Supabase PostgreSQL,
                            Prisma, Supabase Auth, Supabase Storage, and an AI service built with FastAPI and
                            Gemini API.
                        </p>

                        <div className="flex flex-wrap gap-4 text-sm text-slate-200">
                            <span className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2">Next.js</span>
                            <span className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2">Supabase</span>
                            <span className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2">Prisma</span>
                            <span className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2">FastAPI</span>
                        </div>
                    </div>

                    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-xl shadow-slate-950/30">
                        <h2 className="mb-4 text-xl font-semibold">Project foundation</h2>
                        <ul className="space-y-3 text-sm text-slate-300">
                            <li>• Single Supabase PostgreSQL database</li>
                            <li>• Prisma model layer ready for connection</li>
                            <li>• Supabase Auth integration scaffold</li>
                            <li>• Storage hooks prepared for documents and files</li>
                            <li>• AI service separated from the main app</li>
                        </ul>
                    </div>
                </section>
            </div>
        </main>
    );
}
