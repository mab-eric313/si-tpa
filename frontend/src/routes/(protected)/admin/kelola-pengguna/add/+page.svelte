<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let user = $state({});
	// TODO: add kelas_id when user select role "Pengajar"
	// let kelas = $state({});

	let inputUser = $state({});
	let inputBiodata = $state({});
	onMount(async () => {
		try {
			const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include"
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);

			/*
			const resKelas = await fetch(`${PUBLIC_API_BASE_URL}/kelas/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include"
			});
			if (!resKelas.ok) throw new Error(`Error: ${resKelas.statusText}`);
			kelas = await resKelas.json();
			*/

			user = await response.json();
			inputUser = {
				username: user.username ?? "",
				password: user.password ?? "",
				confirmPassword: user.confirmPassword ?? "",
				role: user.role ?? "",
			};
			inputBiodata = {
				nama_lengkap: user.biodata?.nama_lengkap ?? "",
				nama_panggilan: user.biodata?.nama_panggilan ?? "",
				jenis_kelamin: user.biodata?.jenis_kelamin ?? "",
				alamat: user.biodata?.alamat ?? "",
				no_hp: user.biodata?.no_hp ?? "",
				status: user.biodata?.status ?? "",
				// kelas_id: kelas.kelas_id ?? "",
			};
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});

	const daftarRole = ["Admin", "Pengajar", "Bendahara"];
	function selectRole(daftarRole, role) {
		if (!daftarRole?.length || !role) return daftarRole;

		const result = [...daftarRole];
		const pos = result.indexOf(role);
		if (pos > -1) {
			[result[0], result[pos]] = [result[pos], result[0]];
		}
		return result;
	}
	let selectDaftarRole = $derived(selectRole(daftarRole, user.role));

	let add = $state([]);
	let payloadUser = $derived(
		(inputUser.password === inputUser.confirmPassword) ? { ...inputUser } : {}
	);

	async function handleSubmit() {
		try {
			const resUser = await fetch(`${PUBLIC_API_BASE_URL}/auth/register/`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payloadUser)
			});
			if (!resUser.ok) throw new Error(`Error: ${resUser.statusText}`);
			add = await resUser.json();

			let payloadBiodata = $derived(
				{ ...inputBiodata, user_id: add.id }
			);

			const resBiodata = await fetch(
				`${PUBLIC_API_BASE_URL}/biodata-user/`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payloadBiodata)
			});
			if (!resBiodata.ok) throw new Error(`Error: ${resBiodata.statusText}`);

			goto(`${PUBLIC_API_BASE_URL}/admin/kelola-pengguna/`);
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="content-section">
	<a href="/admin/kelola-pengguna" class="btn bg-white bi bi-arrow-left mb-2">
		Kembali
	</a>
	<form action="">
		<div class="container border rounded p-4 mb-3 bg-white">
			<h1 class="mb-3 text-center">Tambah Biodata</h1>
			<div class="row g-3">
				<div class="col-md-6 mb-3">
					<label 
						for="inputNamaLengkap" 
						class="form-label">
						Nama Lengkap
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaLengkap"
						bind:value={inputBiodata.nama_lengkap}
						placeholder="Masukkan nama lengkap">
				</div>
				<div class="col-md-6 mb-3">
					<label 
						for="inputNamaPanggilan" 
						class="form-label">
						Nama Panggilan
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaPanggilan"
						bind:value={inputBiodata.nama_panggilan}
						placeholder="Masukkan nama panggilan">
				</div>
			</div>
			<div class="row g-3">
				<div class="col-md-6 mb-3">
					<label 
						for="selectJenisKelamin"
						class="form-label">
						Jenis Kelamin
					</label>
					<select name="" id="selectJenisKelamin" class="form-select"
						bind:value={inputBiodata.jenis_kelamin}>
						<option value="" disabled>Pilih Jenis Kelamin</option>
						<option value="L">Laki-laki</option>
						<option value="P">Perempuan</option>
					</select>
				</div>
				<div class="col-md-6 mb-3">
					<label 
						for="inputNoHp" 
						class="form-label">
						Nomor Hp
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaPanggilan"
						bind:value={inputBiodata.no_hp}
						placeholder="Masukkan Nomor Hp">
				</div>
			</div>
			<div class="mb-3">
				<label 
					for="inputAlamat" 
					class="form-label">
					Alamat
				</label>
				<textarea 
					type="text" rows="4"
					class="form-control" 
					id="inputNamaPanggilan"
					bind:value={inputBiodata.alamat}
					placeholder="Masukkan Alamat"></textarea>
			</div>
			<div class="mb-3">
				<label 
					for="selectStatus" 
					class="form-label">
					Status
				</label>
				<select name="" id="selectStatus" class="form-select"
					bind:value={inputBiodata.status}>
					<option value="" disabled>Pilih Status</option>
					<option value="Aktif">Aktif</option>
					<option value="Tidak Aktif">Tidak Aktif</option>
				</select>
			</div>
		</div>
		<div class="container border rounded p-4 mb-3 bg-white">
			<h1 class="mb-3 text-center">Tambah Pengguna</h1>
			<div class="mb-3">
				<label 
					for="inputUsername" 
					class="form-label">
					Username
				</label>
				<input 
					type="text" 
					class="form-control" 
					id="inputUsername"
					placeholder="Masukkan Username"
					bind:value={inputUser.username}>
			</div>
			<div class="mb-3">
				<label 
					for="inputPassword" 
					class="form-label">
					Kata Sandi
				</label>
				<input 
					type="password" 
					class="form-control" 
					id="inputPassword"
					placeholder="Masukkan Kata Sandi"
					bind:value={inputUser.password}>
			</div>
			<div class="mb-3">
				<label 
					for="inputConfirmPassword" 
					class="form-label">
					Konfirmasi Kata Sandi
				</label>
				<input 
					type="password" 
					class="form-control" 
					id="inputConfirmPassword"
					placeholder="Masukkan Konfirmasi Kata Sandi"
					bind:value={inputUser.confirmPassword}>
			</div>
			<div class="mb-3">
				<label 
					for="inputRole" 
					class="form-label">
					Role
				</label>
				<select name="" id="inputRole" class="form-select"
					bind:value={inputUser.role}>
					<option value="" disabled>Pilih Role</option>
					{#each selectDaftarRole as role}
						<option value={role}>{role}</option>
					{/each}
				</select>
			</div>
		</div>
		<div class="container d-flex justify-content-end">
			<a href="/admin/kelola-pengguna"class="btn btn-secondary border rounded w-50 mx-2">
				Batal
			</a>
			<button 
				class="btn border rounded w-50 mx-2 bg-green text-white"
				onclick={handleSubmit}>Simpan</button>
		</div>
	</form>
</section>

<style>
	.content-section {
		padding: 0;
	}

	h1 {
		font-size: 25px;
		font-weight: 700;
		color: #1a3a2e;
	}

	.bg-white {
		background-color: white;
	}

	.bg-green {
		background-color: #338136;
	}
</style>
