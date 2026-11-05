export type UserRole = 'ADMIN' | 'DOCTOR' | 'NURSE' | 'PATIENT' | 'RECEPTIONIST';

export type User = {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  role: UserRole;
};

export type AuthState = {
  user: User | null;
  accessToken: string | null;
  refreshToken: string | null;
};
