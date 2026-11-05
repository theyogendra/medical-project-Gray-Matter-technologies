export async function GET() {
    return Response.json({
        status: 'ok',
        service: 'medical-web-app',
        environment: process.env.NODE_ENV ?? 'development',
    });
}
