/*
import { writable } from "svelte/store";

export const authState = writable({
	isLoggedIn: false,
	username: "",
	role: "",
})
*/

const storedUser = typeof window !== 'undefined' ? JSON.parse(localStorage.getItem('user_session') || 'null') : null;

export let authState = $state({
    isLoggedIn: storedUser ? storedUser.isLoggedIn : false,
    username: storedUser ? storedUser.username : '',
    role: storedUser ? storedUser.role : ''
});

export function setAuth(user) {
    authState.isLoggedIn = true;
    authState.username = user.username;
    authState.role = user.role;
    localStorage.setItem('user_session', JSON.stringify(authState));
}

export function clearAuth() {
    authState.isLoggedIn = false;
    authState.username = '';
    authState.role = '';
    localStorage.removeItem('user_session');
}
