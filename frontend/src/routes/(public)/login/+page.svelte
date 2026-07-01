<script>
    import { goto } from "$app/navigation";
	import { authState } from "$lib/authStore";

	let username = $state("");
	let password = $state("");
	let loginSuccess = $state(true);
	let errorMessage = $state("");

	async function handleSubmit(event) {
		event.preventDefault();

		try {
			const response = await fetch("http://localhost:8000/auth/login/", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				credentials: "include",
				body: JSON.stringify({
					"username": username,
					"password": password
				}),
			});

			if (!response.ok) {
				loginSuccess = false;

				const errorData = await response.json();
				errorMessage = errorData.detail || "Terjadi kesalahan saat login";
				return;
			}

			const data = await response.json();

			authState.set({
				isLoggedIn: true,
				username: data.username,
				role: data.role,
			})

			if (data.role === "pengajar") goto("/pengajar");
			else if (data.role === "bendahara") goto("/bendahara");
			else if (data.role === "admin") goto("/admin");
			else goto("/")

		} catch {
			loginSuccess = false;
			errorMessage = "Tidak dapat terhubung ke server";
			console.error(errorMessage);
		}
	}
</script>

<svelte:head>
	<title>Login - TPA Ar-Rahmah</title>
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<section id="login-section">
	<!-- TODO: Login form is not same with the design -->
	<div class="contact-form container my-5">
		<h3 class="mb-4">Login</h3>
		<form class="mb-3" onsubmit={handleSubmit}>
			<div class="mb-3">
				<label for="username" class="form-label">Username</label>
				<input 
					id="username"
					type="text" 
					bind:value={username}
					class="form-control"
					placeholder="Masukkan Username">
			</div>
			<div class="mb-3">
				<label for="password" class="form-label">Password</label>
				<input
					id="password"
					type="password"
					bind:value={password}
					class="form-control"
					placeholder="Masukkan Password">
			</div>
			<div class="form-check">
				<input id="checkDefault" class="form-check-input" type="checkbox">
				<!-- TODO: "Ingat Saya" is not working -->
				<label class="form-check-label" for="checkDefault">Ingat Saya</label>
			</div>
			<button 
				type="submit" 
				class="container btn btn-primary mt-3">
				Login
			</button>
			{#if !loginSuccess && errorMessage}
				<p class="mt-3" style="color : red">Error: {errorMessage}</p>
			{/if}
		</form>
	</div>
</section>
