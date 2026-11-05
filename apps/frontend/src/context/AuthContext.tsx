import { createContext, useContext, useMemo, useState } from 'react';
import { AuthState, User } from '../types/auth';

type AuthContextValue = {
  auth: AuthState;
  login: (user: User, accessToken: string, refreshToken: string) => void;
  logout: () => void;
};

const initialState: AuthState = {
  user: null,
  accessToken: null,
  refreshToken: null,
};

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [auth, setAuth] = useState<AuthState>(initialState);

  const login = (user: User, accessToken: string, refreshToken: string) => {
    setAuth({ user, accessToken, refreshToken });
  };

  const logout = () => {
    setAuth(initialState);
  };

  const value = useMemo<AuthContextValue>(() => ({ auth, login, logout }), [auth]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error('useAuth must be used inside AuthProvider');
  }

  return context;
}
