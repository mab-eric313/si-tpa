import { redirect } from '@sveltejs/kit';

/*
export function load({ cookies }) {
	const token = cookies.get('access_token');
	if (!token) {
		console.error("Error: there is no token named 'access_token'");
		throw redirect(307, '/login');
	}

	try {
		const base64Url = token.split('.')[1];
		const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
		const payload = JSON.parse(atob(base64));

		const userRole = payload.role;
		if (userRole !== 'Admin')
			throw redirect(307, '/unauthorized');
		return { username: payload.sub, role: userRole }
	} catch (error) {
		console.error(error.message);
		console.error("catch error");
		throw redirect(307, '/login');
	}
}
*/

export function load() {
	return {};
}
