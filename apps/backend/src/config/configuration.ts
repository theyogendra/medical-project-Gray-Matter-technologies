export default () => ({
  port: Number(process.env.PORT) || 4000,
  jwt: {
    secret: process.env.JWT_SECRET || 'development-secret',
    expiresIn: Number(process.env.JWT_EXPIRES_IN) || 3600,
    refreshSecret: process.env.JWT_REFRESH_SECRET || 'development-refresh-secret',
    refreshExpiresIn: Number(process.env.JWT_REFRESH_EXPIRES_IN) || 604800,
  },
  database: {
    url: process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/medical_app?schema=public',
  },
});
