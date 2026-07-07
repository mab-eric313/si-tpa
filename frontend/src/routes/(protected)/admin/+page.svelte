<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	
	let daftarUser = $state([]);
	let daftarSiswa = $state([]);
	let errorMessage = $state("");

	onMount(async () => {
		try {
			// TODO: change hardcoded url. Make URL variable placed in $lib dir
			const response = await fetch("http://localhost:8000/auth/", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			daftarUser = await response.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	onMount(async () => {
		try {
			// TODO: change hardcoded url. Make URL variable placed in $lib dir
			const response = await fetch("http://localhost:8000/siswa/", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			daftarSiswa = await response.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	let countAdmin = $derived(daftarUser.filter(user => user.role === 'Admin').length);
	let countPengajar = $derived(daftarUser.filter(user => user.role === 'Pengajar').length);
    let countBendahara = $derived(daftarUser.filter(user => user.role === 'Bendahara').length);
    let countSiswa = $derived(daftarSiswa.length);

</script>

<section class="sidebar-gap">
	<div class="container">
		<h1 class="py-5">Ringkasan Role Pengguna</h1>
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

<style>
	.sidebar-gap {
		padding-left: 240px; 
		position: relative; 
		min-height: 100vh;
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
