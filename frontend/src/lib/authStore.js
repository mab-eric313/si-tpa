import { writable } from "svelte/store";

export const authState = writable({
	isLoggedIn: false,
	username: "",
	role: "",
})
