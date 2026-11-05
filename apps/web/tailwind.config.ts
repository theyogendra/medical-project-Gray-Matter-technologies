import type { Config } from 'tailwindcss';

const config: Config = {
    content: ['./app/**/*.{js,ts,jsx,tsx,mdx}', './components/**/*.{js,ts,jsx,tsx,mdx}'],
    theme: {
        extend: {
            colors: {
                brand: {
                    50: '#eef8ff',
                    100: '#d8f0ff',
                    500: '#1a73e8',
                    600: '#1457c7',
                    700: '#0e459f',
                },
            },
        },
    },
    plugins: [],
};

export default config;
