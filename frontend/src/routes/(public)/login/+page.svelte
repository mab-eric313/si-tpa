<script>
    import { goto } from "$app/navigation";
	import { setAuth } from '$lib/authStore.svelte';
	import LoadingOverlay from "$lib/components/LoadingOverlay.svelte";
	import { onMount } from "svelte";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let username = $state("");
	let password = $state("");
	let showPassword = $state(false);
	let rememberMe = $state(false);
	let loginSuccess = $state(true);
	let errorMessage = $state("");
	let isLoading = $state(false);
	let loadingMessage = $state('Sedang memuat data...');

	onMount(() => {
		const savedRemember = localStorage.getItem('rememberMe');
		if (savedRemember === 'true') {
			rememberMe = true;
			const savedUser = localStorage.getItem('savedUsername');
			if (savedUser) {
				username = savedUser;
			}
		}
	});

	async function handleSubmit(event) {
		event.preventDefault();

		try {
			isLoading = true;
			loadingMessage = "Sedang memuat data...";
			const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/login/`, {
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
			} else {
				const data = await response.json();
				setAuth({
					username: data.username,
					role: data.role
				});

				if (rememberMe) {
					localStorage.setItem('savedUsername', username);
					localStorage.setItem('rememberMe', 'true');
				} else {
					localStorage.removeItem('savedUsername');
					localStorage.removeItem('rememberMe');
				}

				if 		(data.role === "Pengajar") 	goto("/pengajar");
				else if (data.role === "Bendahara") goto("/bendahara/pencatatan");
				else if (data.role === "Admin") 	goto("/admin");
				else goto("/login")
			}
		} catch {
			loginSuccess = false;
			errorMessage = "Tidak dapat terhubung ke server";
			console.error(errorMessage);
		} finally {
			isLoading = false;
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

<section id="login-section" class="d-flex container">

	{#if isLoading}
		<LoadingOverlay visible={isLoading} color="primary" />
	{/if}

	<div class="login-card">

		<!-- Panel Kiri -->
		<div class="left-panel">

			<div class="logo">
				<div class="logo-icon">📖</div>
				<span>Taman Pendidikan Al-Qur'an</span>
			</div>

			<h1>Digitalisasi TPA <br>untuk Masa Depan Santri</h1>

			<p>
				Sistem administrasi terpadu untuk pengelolaan santri,
				kurikulum, dan perkembangan hafalan yang lebih tertata
				dan profesional.
			</p>

			<div class="image-card">
				<img
					src="https://images.unsplash.com/photo-1519817650390-64a93db51149?w=500"
					alt="Masjid"
				/>
			</div>

		</div>

		<!-- Panel Kanan -->
		<div class="right-panel">
			<h2 class="text-center mb-3">Login</h2>
			<form onsubmit={handleSubmit}>
				<div class="form-group">
					<label for="username">Username</label>
					<input
						id="username"
						type="text"
						bind:value={username}
						placeholder="Masukkan username anda"
					/>
				</div>

				<div class="form-group">
					<label for="password">Kata Sandi</label>
					<div class="password-input-wrapper">
						<input
							id="password"
							type={showPassword ? "text" : "password"}
							bind:value={password}
							placeholder="Masukkan kata sandi anda"
						/>
						<button 
							type="button" 
							class="toggle-password" 
							onclick={() => showPassword = !showPassword} 
							aria-label="Toggle password visibility"
						>
							{#if showPassword}
								<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
							{:else}
								<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
							{/if}
						</button>
					</div>
				</div>

				<div class="form-check">
					<input id="checkDefault" class="form-check-input" type="checkbox" bind:checked={rememberMe}>
					<label class="form-check-label" for="checkDefault">Ingat Saya</label>
				</div>

				<button type="submit">
					Masuk
				</button>

				{#if !loginSuccess && errorMessage}
					<p class="mt-3" style="color : red">Error: {errorMessage}</p>
				{/if}

			</form>

		</div>

	</div>

</section>

<style>
	section {
		background:#f7f5ef;
	}
	
	.container {
		width:100%;
		min-height:100vh;
		display:flex;
		justify-content:center;
		align-items:center;
		padding:30px;
		background:#f7f5ef;
	}

	.login-card{
		width:900px;
		background:white;
		border-radius:20px;
		overflow:hidden;
		display:flex;
		box-shadow:0 10px 30px rgba(0,0,0,.1);
	}

	.left-panel{
		width:50%;
		background:#2e6b2f;
		padding:40px;
		color:white;
	}

	.logo{
		display:flex;
		align-items:center;
		gap:12px;
		margin-bottom:40px;
	}

	.logo-icon{
		width:42px;
		height:42px;
		background:white;
		color:#2e6b2f;
		display:flex;
		align-items:center;
		justify-content:center;
		border-radius:8px;
		font-size:22px;
	}

	.logo span{
		font-weight:600;
		font-size:18px;
	}

	h1{
		font-size:38px;
		line-height:1.3;
		margin-bottom:18px;
	}

	.left-panel p{
		line-height:1.7;
		color:#e6e6e6;
	}

	.image-card{
		margin-top:35px;
		display:flex;
		justify-content:center;
	}

	.image-card img{
		width:230px;
		height:230px;
		object-fit:cover;
		border-radius:15px;
	}

	.right-panel{
		width:50%;
		padding:70px 50px;
		display:flex;
		flex-direction:column;
		justify-content:center;
	}

	h2{
		font-size:36px;
		margin-bottom:5px;
	}

	.form-group{
		margin-bottom:20px;
	}

	label{
		display:block;
		margin-bottom:8px;
		font-weight:500;
	}

	input{
		width:100%;
		padding:14px;
		border:1px solid #ccc;
		border-radius:8px;
		font-size:15px;
		outline:none;
	}

	input:focus{
		border-color:#2e6b2f;
	}

	.password-input-wrapper {
		position: relative;
		display: flex;
		align-items: center;
	}

	.password-input-wrapper input {
		padding-right: 45px;
	}

	.toggle-password {
		position: absolute;
		right: 12px;
		background: transparent;
		border: none;
		cursor: pointer;
		color: #666;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 4px;
		width: auto;
		margin-top: 0;
		transition: color 0.3s;
	}

	.toggle-password:hover {
		color: #2e6b2f;
		background: transparent;
	}

	.form-check {
		display: flex;
		align-items: center;
		gap: 8px;
		margin-bottom: 20px;
	}

	.form-check-input {
		width: 18px;
		height: 18px;
		accent-color: #2e6b2f; /* Warna hijau sesuai tema */
		cursor: pointer;
	}

	.form-check-label {
		font-size: 14px;
		color: #555;
		cursor: pointer;
		user-select: none;
	}

	button[type="submit"] {
		width:100%;
		padding:14px;
		background:#3c8a39;
		color:white;
		border:none;
		border-radius:8px;
		font-size:16px;
		font-weight:bold;
		cursor:pointer;
		margin-top:10px;
		transition:.3s;
	}

	button[type="submit"]:hover{
		background:#2e6b2f;
	}

	@media(max-width:900px){
		.login-card{
			flex-direction:column;
			width:100%;
		}

		.left-panel,
		.right-panel{
			width:100%;
		}

		.right-panel{
			padding:40px 30px;
		}

		h1{
			font-size:30px;
		}

		h2{
			font-size:30px;
		}
	}
</style>
