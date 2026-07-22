<script>
    import { goto } from "$app/navigation";
	import { setAuth } from '$lib/authStore.svelte';

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let username = $state("");
	let password = $state("");
	let loginSuccess = $state(true);
	let errorMessage = $state("");

	async function handleSubmit(event) {
		event.preventDefault();

		try {
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

				if (data.role === "Admin") {
					goto("/admin");
				}
			}

			const data = await response.json();
			console.log(data);

			authState.set({
				isLoggedIn: true,
				username: data.username,
				role: data.role,
			})

			if (data.role === "Pengajar") {
				console.log("(data.role === 'Pengajar') TRUE");
				goto("/pengajar");
			}
			else if (data.role === "Bendahara") {
				console.log("(data.role === 'Bendahara') TRUE");
				goto("/bendahara/pencatatan");
			}
			else if (data.role === "Admin") {
				console.log("(data.role === 'Admin') TRUE");
				goto("/admin");
			}
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

<section id="login-section" class="d-flex container">
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

					<input
						id="password"
						type="password"
						bind:value={password}
						placeholder="Masukkan kata sandi anda"
					/>
				</div>

				<!-- TODO: "Ingat Saya" is not working -->
				<!--
				<div class="form-check">
					<input id="checkDefault" class="form-check-input" type="checkbox">
					<label class="form-check-label" for="checkDefault">Ingat Saya</label>
				</div>
				-->

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

	button{

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

	button:hover{

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
