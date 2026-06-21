import { get } from 'svelte/store';
import { authState } from '$lib/authStore';
import { redirect } from '@sveltejs/kit';

export function load() {
    const auth = get(authState);
    
    if (!auth.isLoggedIn) {
        throw redirect(307, '/login');
    }
    
    if (auth.role !== 'pengajar' && auth.role !== 'admin') {
        throw redirect(307, '/unauthorized');
    }
}
