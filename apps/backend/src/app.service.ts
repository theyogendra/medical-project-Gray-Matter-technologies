import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getWelcomeMessage(): string {
    return 'Medical Web Application API is running.';
  }
}
