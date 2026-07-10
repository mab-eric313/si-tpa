<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	let errorMessage = $state("");
	let siswa = $state({});
	let daftarKelas = $state({});
	let siswa_id = $derived(Number($page.params.id));
	let wali_id = $state(0);

	let inputSiswa = $state({});
	let inputWali = $state({});
	onMount(async () => {
		try {
			const [resSiswa, resKelas] = await Promise.all([
				fetch(`http://localhost:8000/siswa/${siswa_id}`, {
					credentials: "include"
				}),
				fetch(`http://localhost:8000/kelas/`, {
					credentials: "include"
				}),
			]);
			if (!resSiswa.ok) throw new Error(`Error: ${resSiswa.statusText}`);
			if (!resKelas.ok) throw new Error(`Error: ${resKelas.statusText}`);

			siswa = await resSiswa.json();
			daftarKelas = await resKelas.json();

			inputSiswa = {
				nama: siswa.nama ?? "",
				jenis_kelamin: siswa.jenis_kelamin ?? "",
				tanggal_lahir: siswa.tanggal_lahir ?? "",
				alamat: siswa.alamat ?? "",
				kelas_id: siswa.kelas?.id ?? "",
				kelas: siswa.kelas ?? "",
				status: siswa.status ?? "",
			};
			inputWali = {
				nama: siswa.wali?.nama ?? "",
				alamat: siswa.wali?.alamat ?? "",
				no_hp: siswa.wali?.no_hp ?? "",
			};
			wali_id = siswa.wali_id ?? null;
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function selectKelas(daftarKelas, kelas) {
		if (!daftarKelas?.length || !kelas) return daftarKelas;

		const result = [...daftarKelas];
		const pos = result.indexOf(kelas);
		if (pos > -1) {
			[result[0], result[pos]] = [result[pos], result[0]];
		}
		return result;
	}
	let selectDaftarKelas = $derived(selectKelas(daftarKelas, siswa.kelas));
	$inspect(selectDaftarKelas);

	let edit = $state([]);
	let payloadSiswa = $derived({...inputSiswa});
	let payloadWali = $derived({...inputWali});

	async function handleSubmit() {
		try {
			const [resSiswa, resWali] = await Promise.all([
				fetch(`http://localhost:8000/siswa/${siswa_id}`, {
					method: "PATCH",
					headers: { "Content-Type": "application/json" },
					credentials: "include",
					body: JSON.stringify(payloadSiswa)
				}),
				fetch(`http://localhost:8000/wali/${wali_id}`, {
					method: "PATCH",
					headers: { "Content-Type": "application/json" },
					credentials: "include",
					body: JSON.stringify(payloadWali)
				}),
			]);

			goto("http://localhost:5173/admin/kelola-siswa/");
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="sidebar-gap">
	<a href="/admin/kelola-siswa" class="btn btn-light bi bi-arrow-left mb-5">
		Kembali
	</a>
	<form action="">
			<div class="container border rounded py-4 mb-3">
				<h1 class="mb-5">Edit Siswa</h1>
				<div class="mb-3">
					<label 
						for="inputNama" 
						class="form-label">
						Nama
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNama"
						bind:value={inputSiswa.nama}
						placeholder="Masukkan nama">
				</div>
				<div class="mb-3">
					<label 
						for="selectJenisKelamin"
						class="form-label">
						Jenis Kelamin
					</label>
					<select name="" id="selectJenisKelamin" class="form-select"
						bind:value={inputSiswa.jenis_kelamin}>
						<option value="L">Laki-laki</option>
						<option value="P">Perempuan</option>
					</select>
				</div>
				<div class="mb-3">
					<label 
						for="inputTanggalLahir"
						class="form-label">
						Tanggal Lahir
					</label>
					<input 
						type="date" 
						class="form-control" 
						id="inputTanggalLahir"
						bind:value={inputSiswa.tanggal_lahir}
						placeholder="Masukkan tanggal lahir">
				</div>
				<div class="mb-3">
					<label 
						for="inputAlamatSiswa"
						class="form-label">
						Alamat
					</label>
					<textarea 
						type="text" rows="4"
						class="form-control" 
						id="inputAlamatSiswa"
						bind:value={inputSiswa.alamat}
						placeholder="Masukkan alamat"></textarea>
				</div>
				<div class="mb-3">
					<label 
						for="selectKelas"
						class="form-label">
						Kelas
					</label>
					<select name="" id="selectKelas" class="form-select"
						bind:value={inputSiswa.kelas_id}>
						{#each selectDaftarKelas as kelas}
							<option value={kelas.id}>{kelas.nama}</option>
						{/each}
					</select>
				</div>
			</div>
			<div class="container border rounded py-4 mb-3">
				<h1 class="mb-5">Edit Wali</h1>
				<div class="mb-3">
					<label 
						for="inputNamaWali"
						class="form-label">
						Nama
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaWali"
						bind:value={inputWali.nama}
						placeholder="Masukkan nama">
				</div>
				<div class="mb-3">
					<label 
						for="inputAlamatWali"
						class="form-label">
						Alamat
					</label>
					<textarea 
						rows="4"
						class="form-control" 
						id="inputAlamatWali"
						bind:value={inputWali.alamat}
						placeholder="Masukkan alamat"></textarea>
				</div>
				<div class="mb-3">
					<label 
						for="inputNoHp" 
						class="form-label">
						Nomor Hp
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNoHp"
						bind:value={inputWali.no_hp}
						placeholder="Masukkan Nomor Hp">
				</div>
			</div>
			<div class="container border rounded py-4 mb-3">
				<div class="mb-3">
					<label 
						for="selectStatus" 
						class="form-label">
						Status Siswa
					</label>
					<select name="" id="selectStatus" class="form-select"
						bind:value={inputSiswa.status}>
						<option value="Aktif">Aktif</option>
						<option value="Tidak Aktif">Tidak Aktif</option>
					</select>
				</div>
			</div>
		<div class="container d-flex justify-content-end">
			<a href="/admin/kelola-siswa/"class="btn border rounded w-50 mx-2">
				Batal
			</a>
			<button 
				class="btn border rounded w-50 mx-2 bg-green text-white"
				onclick={handleSubmit}>Simpan</button>
		</div>
	</form>
</section>

<style>
	.sidebar-gap {
		padding-left: 240px; 
		position: relative; 
		min-height: 100vh;
	}

	.bg-green {
		background-color: #338136;
	}
</style>


