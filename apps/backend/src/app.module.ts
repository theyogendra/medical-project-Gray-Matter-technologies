import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';
import { PrismaService } from './database/prisma.service';
import { HealthController } from './health/health.controller';

@Module({
  imports: [AuthModule, UsersModule],
  controllers: [AppController, HealthController],
  providers: [AppService, PrismaService],
})
export class AppModule { }
