import { Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcryptjs';
import { UsersService } from '../users/users.service';
import { LoginDto } from './dto/login.dto';

@Injectable()
export class AuthService {
  constructor(
    private readonly jwtService: JwtService,
    private readonly usersService: UsersService,
  ) { }

  async validateUser(loginDto: LoginDto) {
    const user = await this.usersService.findByEmail(loginDto.email);

    if (!user) {
      throw new UnauthorizedException('Invalid credentials');
    }

    const isPasswordValid = await bcrypt.compare(loginDto.password, user.passwordHash);

    if (!isPasswordValid) {
      throw new UnauthorizedException('Invalid credentials');
    }

    const { passwordHash, ...userWithoutPassword } = user;
    return userWithoutPassword;
  }

  async login(loginDto: LoginDto) {
    const user = await this.validateUser(loginDto);
    const payload = { sub: user.id, email: user.email, role: user.role };
    const refreshExpiresIn = (process.env.JWT_REFRESH_EXPIRES_IN as any) || '7d';

    return {
      accessToken: this.jwtService.sign(payload, {
        expiresIn: Number(process.env.JWT_EXPIRES_IN ?? '3600') || 3600,
      }),
      refreshToken: this.jwtService.sign(payload, {
        secret: process.env.JWT_REFRESH_SECRET || 'development-refresh-secret',
        expiresIn: refreshExpiresIn,
      }),
      user,
    };
  }
}
