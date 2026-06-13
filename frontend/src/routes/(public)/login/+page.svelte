<script>
    import { goto } from "$app/navigation";

	let username = $state("");
	let password = $state("");
	let loginSuccess = $state(false);
	let submitClicked = $state(false);

	function onSubmit() {
		submitClicked = true;
		if (username === "pengajar" && password === "pengajar") {
			goto("/pengajar");
			loginSuccess = true;
		} else if (username === "bendahara" && password === "bendahara") {
			goto("/bendahara");
			loginSuccess = true;
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
		<form class="mb-3">
			<div class="mb-3">
				<label for="username" class="form-label">Username</label>
				<input 
					type="text" 
					bind:value={username}
					class="form-control"
					placeholder="Masukkan Username">
			</div>
			<div class="mb-3">
				<label for="message" class="form-label">Password</label>
				<input
					type="password"
					bind:value={password}
					class="form-control"
					placeholder="Masukkan Password">
			</div>
			<div class="form-check">
				<input id="checkDefault" class="form-check-input" type="checkbox">
				<label class="form-check-label" for="checkDefault">Ingat Saya</label>
			</div>
		</form>
		<button 
			onclick={onSubmit}
			type="submit" 
			class="container btn btn-primary">
			Login
		</button>
		{#if !loginSuccess && submitClicked}
			<p style="color: red">Gagal login, username atau password salah.</p>
		{/if}
	</div>
</section>
