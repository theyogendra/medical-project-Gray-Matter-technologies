import { FormEvent, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export function LoginPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const { login } = useAuth();
  const [email, setEmail] = useState('admin@medical.local');
  const [password, setPassword] = useState('Password123!');

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const user = {
      id: 'user-1',
      email,
      firstName: 'Admin',
      lastName: 'User',
      role: 'ADMIN',
    };

    login(user, 'access-token-placeholder', 'refresh-token-placeholder');
    const next = (location.state as { from?: { pathname?: string } } | null)?.from?.pathname ?? '/dashboard';
    navigate(next, { replace: true });
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-950 px-4">
      <div className="w-full max-w-md rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-2xl">
        <div className="mb-8 text-center">
          <p className="text-xs uppercase tracking-[0.2em] text-cyan-400">Secure Access</p>
          <h1 className="mt-3 text-3xl font-semibold text-white">Medical Portal</h1>
        </div>

        <form className="space-y-5" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="email" className="mb-2 block text-sm font-medium text-slate-200">
              Email
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              className="w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 focus:border-cyan-500 focus:outline-none"
              placeholder="name@medical.local"
            />
          </div>

          <div>
            <label htmlFor="password" className="mb-2 block text-sm font-medium text-slate-200">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              className="w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 focus:border-cyan-500 focus:outline-none"
              placeholder="Password123!"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-xl bg-cyan-600 px-4 py-3 font-medium text-white transition hover:bg-cyan-500"
          >
            Sign in
          </button>
        </form>
      </div>
    </div>
  );
}
