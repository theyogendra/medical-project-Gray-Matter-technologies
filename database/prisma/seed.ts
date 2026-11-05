import 'dotenv/config';
import { PrismaClient } from '@prisma/client';
import * as bcrypt from 'bcryptjs';

const prisma = new PrismaClient();

async function main() {
  const adminPasswordHash = await bcrypt.hash('Password123!', 10);

  await prisma.user.upsert({
    where: { email: 'admin@medical.local' },
    update: {},
    create: {
      email: 'admin@medical.local',
      firstName: 'Admin',
      lastName: 'User',
      passwordHash: adminPasswordHash,
      role: 'ADMIN',
      status: 'ACTIVE',
    },
  });
}

main()
  .catch((error) => {
    console.error(error);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
