import { Navigate, Route, Routes } from 'react-router-dom';
import { AppLayout } from '../components/Layout/AppLayout';
import { ProtectedRoute } from '../components/common/ProtectedRoute';
import { useAuth } from '../context/AuthContext';
import { DashboardPage } from '../pages/DashboardPage';
import { LoginPage } from '../pages/LoginPage';
import { NotFoundPage } from '../pages/NotFoundPage';

function PlaceholderPage({ title }: { title: string }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">
      <p className="text-sm uppercase tracking-[0.2em] text-cyan-400">Module</p>
      <h1 className="mt-3 text-3xl font-semibold text-white">{title}</h1>
      <p className="mt-3 text-slate-400">
        Placeholder page for the corresponding business module. Add the detailed workflow after requirements are approved.
      </p>
    </div>
  );
}

export function AppRoutes() {
  const { auth } = useAuth();

  return (
    <Routes>
      <Route path="/login" element={auth.user ? <Navigate to="/dashboard" replace /> : <LoginPage />} />

      <Route element={<ProtectedRoute />}>
        <Route element={<AppLayout />}>
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/patients" element={<PlaceholderPage title="Patients" />} />
          <Route path="/appointments" element={<PlaceholderPage title="Appointments" />} />
          <Route path="/reports" element={<PlaceholderPage title="Reports" />} />
          <Route path="/settings" element={<PlaceholderPage title="Settings" />} />
          <Route index element={<Navigate to="/dashboard" replace />} />
        </Route>
      </Route>

      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
