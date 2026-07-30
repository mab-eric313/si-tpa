<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	
	import LoadingOverlay from "$lib/components/LoadingOverlay.svelte";
	import { authState } from '$lib/authStore.svelte';
	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	$effect(() => {
        if (!authState.isLoggedIn && authState.role !== 'Admin') {
            goto('/login');
        }
    });
	
	let daftarUser = $state([]);
	let daftarSiswa = $state([]);
	let errorMessage = $state("");

	let isFetchAuth = $state(false);
	let isFetchSiswa = $state(false);

	$effect(async () => {
		try {
			isFetchAuth = true;
			const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(response.statusText);
			daftarUser = await response.json();
			if (daftarSiswa) isFetchAuth = false;
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	onMount(async () => {
		try {
			isFetchSiswa = true;
			const response = await fetch(`${PUBLIC_API_BASE_URL}/siswa/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(response.statusText);
			daftarSiswa = await response.json();
			if (daftarSiswa) isFetchSiswa = false;
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	let countAdmin = $derived(daftarUser.filter(user => user.role === 'Admin').length);
	let countPengajar = $derived(daftarUser.filter(user => user.role === 'Pengajar').length);
    let countBendahara = $derived(daftarUser.filter(user => user.role === 'Bendahara').length);
    let countSiswa = $derived(daftarSiswa.length);

	// $inspect(authState);
</script>

<!-- TODO: Auth checking not is actually checking -->
{#if authState.isLoggedIn && authState.role === 'Admin'}
<section class="content-section">
	{#if isFetchAuth && isFetchSiswa}
		<LoadingOverlay visible={true} color="primary" />
	{/if}
	<div class="container">
		<h1 class="py-5 text-center">Ringkasan Role Pengguna</h1>
		<div class="row">
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-person-fill-gear rounded-circle rounded-icon-admin"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Admin</span>
					<span>{countAdmin} Admin</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-person-fill rounded-circle rounded-icon-izin-sakit"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Pengajar</span>
					<span>{countPengajar} Pengajar</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-currency-dollar rounded-circle rounded-icon-alpha"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Bendahara</span>
					<span>{countBendahara} Bendahara</span>
				</div>
			</div>
		</div>
	</div>
	<div class="container pb-5">
		<div class="row mb-5">
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-mortarboard-fill rounded-circle rounded-icon-admin"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Siswa</span>
					<span>{countSiswa} Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-person-fill rounded-circle rounded-icon-izin-sakit"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Viewer</span>
					<span>1 Viewer</span>
				</div>
			</div>
		</div>
	</div>
</section>
{:else}
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <p>Memverifikasi akses...</p>
    </div>
{/if}

<style>
	.content-section {
		padding: 0;
	}

	h1 {
		font-size: 1.75rem;
		font-weight: 700;
		color: #1a3a2e;
	}
	
	span {
		font-size: 15px;
	}

	.rounded-icon-admin {
		font-size: 25px;
		width: 40px;
		height: 40px;

		color: white;
		background-color: green;
	}

	.rounded-icon-izin-sakit {
		font-size: 25px;
		width: 40px;
		height: 40px;

		color: white;
		background-color: orange;
	}

	.rounded-icon-alpha {
		font-size: 25px;
		width: 40px;
		height: 40px;

		color: white;
		background-color: red;
	}

	.rounded-icon-outer-tanggal {
		padding-top: 4px;
		width: 40px;
		height: 40px;
		background-color: green;
	}

	.rounded-icon-tanggal {
		font-size: 20px;
		color: white;
	}

	.col {
		min-height: 150px;
		margin-right: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		padding: 20px;
	}
</style>
