import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: true,
		proxy: {
			'/api': 'http://localhost:8000',
			'/docs': 'http://localhost:8000',
			'/redoc': 'http://localhost:8000',
			'/openapi.json': 'http://localhost:8000',
		},
	},
});
