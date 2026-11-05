import { NavLink, Outlet } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const navItems = [
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/patients', label: 'Patients' },
  { to: '/appointments', label: 'Appointments' },
  { to: '/reports', label: 'Reports' },
  { to: '/settings', label: 'Settings' },
];

export function AppLayout() {
  const { auth, logout } = useAuth();

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <aside className="fixed inset-y-0 left-0 w-72 border-r border-slate-800 bg-slate-900/90 p-6">
        <div className="mb-8">
          <p className="text-xs uppercase tracking-[0.2em] text-cyan-400">Medical Suite</p>
          <h1 className="mt-2 text-2xl font-semibold">Care Portal</h1>
        </div>

        <nav className="space-y-2">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `block rounded-xl px-4 py-3 text-sm font-medium transition ${isActive ? 'bg-cyan-600 text-white' : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="ml-72 min-h-screen">
        <header className="border-b border-slate-800 bg-slate-900/70 px-8 py-5 backdrop-blur">
          <div className="flex items-center justify-between gap-4">
            <div>
              <p className="text-sm text-slate-400">Welcome back</p>
              <h2 className="text-lg font-semibold text-white">
                {auth.user ? `${auth.user.firstName} ${auth.user.lastName}` : 'Healthcare team'}
              </h2>
            </div>

            <button
              type="button"
              onClick={logout}
              className="rounded-xl border border-slate-700 bg-slate-800 px-4 py-2 text-sm font-medium text-slate-100 transition hover:bg-slate-700"
            >
              Logout
            </button>
          </div>
        </header>

        <div className="p-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
