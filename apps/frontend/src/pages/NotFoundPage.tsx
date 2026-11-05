import { Link } from 'react-router-dom';

export function NotFoundPage() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-950 px-6">
      <div className="max-w-md text-center">
        <p className="text-sm uppercase tracking-[0.2em] text-cyan-400">404</p>
        <h1 className="mt-3 text-4xl font-bold text-white">Page not found</h1>
        <p className="mt-4 text-slate-400">The requested route does not exist in the current application foundation.</p>
        <Link to="/dashboard" className="mt-6 inline-block rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white hover:bg-cyan-500">
          Return to dashboard
        </Link>
      </div>
    </div>
  );
}
