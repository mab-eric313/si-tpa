<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let id = $derived(Number($page.params.id));

	const daftarHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"];
	let selectedStartHari = $state("");
	let selectedEndHari = $state("");

	let kelas = $state("");
	let inputKelas = $state({});
	onMount(async () => {
		try {
			const res = await fetch(`${PUBLIC_API_BASE_URL}/kelas/${id}`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include"
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			kelas = await res.json();
			inputKelas = {
				nama: kelas.nama ?? "",
				start_day: kelas.start_day ?? "",
				end_day: kelas.end_day ?? "",
				start_time: kelas.start_time ?? "",
				end_time: kelas.end_time ?? "",
			};
			selectedStartHari = inputKelas.start_day;
			selectedEndHari = inputKelas.end_day;
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	let payloadKelas = $derived({
		...inputKelas, start_day: selectedStartHari, end_day: selectedEndHari
	});

	async function handleSubmit() {
		try {
			const res = await fetch(`${PUBLIC_API_BASE_URL}/kelas/${id}`, {
				method: "PATCH",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payloadKelas),
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			goto("/admin/kelola-kelas/");
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="content-section">
	<a href="/admin/kelola-kelas" class="btn bg-white btn-light bi bi-arrow-left mb-2">
		Kembali
	</a>
	<form action="">
		<div class="container bg-white border rounded py-4 mb-3">
			<h1 class="mb-3 text-center">Edit Kelas</h1>
			<div class="mb-3">
				<label 
					for="inputNamaKelas" 
					class="form-label">
					Nama Kelas
				</label>
				<input 
					type="text" 
					class="form-control" 
					id="inputNamaKelas"
					bind:value={inputKelas.nama}
					placeholder="Masukkan nama">
			</div>
			<div class="row">
				<div class="col-md-6 mb-3">
					<label 
						for="selectStartHari"
						class="form-label">
						Dari Hari
					</label>
					<select name="" id="selectStartHari" class="form-select"
						bind:value={selectedStartHari}>
						<option value="" disabled selected>Pilih Hari</option>
						{#each daftarHari as hari}
							<option value={hari}>{hari}</option>
						{/each}
					</select>
				</div>
				<div class="col-md-6 mb-3">
					<label 
						for="selectEndHari"
						class="form-label">
						Sampai Hari
					</label>
					<select name="" id="selectEndHari" class="form-select"
						bind:value={selectedEndHari}>
						<option value="" disabled selected>Pilih Hari</option>
						{#each daftarHari as hari}
							<option value={hari}>{hari}</option>
						{/each}
					</select>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 mb-3">
					<label 
						for="inputStartWaktu"
						class="form-label">
						Dari Jam
					</label>
					<input 
						type="time" 
						class="form-control" 
						id="inputStartWaktu"
						bind:value={inputKelas.start_time}
					/>
				</div>
				<div class="col-md-6 mb-3">
					<label 
						for="inputStartWaktu"
						class="form-label">
						Sampai Jam
					</label>
					<input 
						type="time" 
						class="form-control" 
						id="inputEndWaktu"
						bind:value={inputKelas.end_time}
					/>
				</div>
			</div>
		</div>
		<div class="container d-flex justify-content-end">
			<a href="/admin/kelola-kelas/"
				class="btn btn-secondary border rounded w-50 mx-2">
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
		font-size: 30px;
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



