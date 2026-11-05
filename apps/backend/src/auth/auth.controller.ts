import { Body, Controller, Post } from '@nestjs/common';
import { ApiBody, ApiOperation, ApiResponse, ApiTags } from '@nestjs/swagger';
import { AuthService } from './auth.service';
import { LoginDto } from './dto/login.dto';

@ApiTags('Authentication')
@Controller('auth')
export class AuthController {
  constructor(private readonly authService: AuthService) { }

  @Post('login')
  @ApiOperation({ summary: 'Authenticate a user and return JWT tokens' })
  @ApiBody({ type: LoginDto })
  @ApiResponse({ status: 201, description: 'Successful login' })
  login(@Body() loginDto: LoginDto) {
    return this.authService.login(loginDto);
  }
}
