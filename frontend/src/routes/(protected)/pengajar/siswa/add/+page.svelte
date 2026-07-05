<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	let lulusUlang = $state("lulus");
	let penilaian = $state($page.url.searchParams.get("penilaian") ?? "surat");

	let penilaianSurat = $state([]);
	let errorMessage = $state("");

	const endpointMap = {
		jilid: `http://localhost:8000/penilaian-jilid/`,
		surat: `http://localhost:8000/penilaian-surat/`,
		doa: `http://localhost:8000/penilaian-doa/`,
	}

	let input = $state({
		jilid: { 
			materi_bacaan: "",
			tanggal_setor: "",
			nilai_tajwid: 0,
			nilai_makhraj: 0,
			nilai_kelancaran: 0,
			lulus_ulang: "",
			note: ""
		}, 
		doa: { 
			nama_doa: "",
			tanggal_setor: "",
			nilai: 0,
			lulus_ulang: "",
			note: ""
		}, 
		surat: { 
			nama_surat: "",
			tanggal_setor: "",
			kelancaran: 0,
			ketepatan_bacaan: 0,
			lulus_ulang: "",
			note: ""
		}, 
	});

	/*
	 * opsi 1
	let namaSiswa = $state("");
	let selectedSiswaId = $state("");
	let daftarSiswa = $state([]);

	let filteredSiswa = $derived(
		namaSiswa === ""
			? daftarSiswa
			: daftarSiswa.filter(siswa =>
				siswa.nama.toLowerCase().includes(namaSiswa.toLowerCase())
			)
	);

	function handlePilihSiswa() {
		const siswa = daftarSiswa.find(
			s => String(s.id) === selectedSiswaId
		);
		if (siswa) namaSiswa = siswa.nama;
	}
	*/

	let namaSiswa = $state("");
	let daftarSiswa = $state([]);

	onMount(async () => {
		try {
			const res = await fetch("http://localhost:8000/siswa/", {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			daftarSiswa = await res.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});
	
	let selectedSiswaId = $derived(
		daftarSiswa.find(s => s.nama === namaSiswa)?.id ?? null
	);

	let payload = $derived({ 
		...input[penilaian], 
		lulus_ulang: lulusUlang, 
		siswa_id: selectedSiswaId
	});
	$inspect(payload);
	async function handleSubmit() {
		try {
			const response = await fetch(endpointMap[penilaian], {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payload)
			});
			if (!response.ok) throw new Error(`${response.statusText}`);

			penilaianSurat = await response.json();
			goto("http://localhost:5173/pengajar/kelas");
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}

</script>

<section class="sidebar-gap">
	<a href="/pengajar/kelas/" class="btn btn-light bi bi-arrow-left mb-5">
		Kembali
	</a>
	<form action="">
		<div class="container border rounded py-4 mb-3">
			<h1 class="mb-5">Input Penilaian Harian</h1>

			<span class="fs-5 fw-medium">Pilih Jenis Penilaian</span>
			<div class="mb-3 row mx-0">
				<button 
				 	type="button" 
					class="fs-5 col {penilaian === 'surat' ? 'jenis-penilaian-active' : 'jenis penilaian-deactive'} fw-medium text-center align-content-center"
					onclick={() => penilaian = 'surat'}>
					Hafalan Surat
				</button>
				<button 
					type="button" 
					class="fs-5 col {penilaian === 'doa' ? 'jenis-penilaian-active' : 'jenis penilaian-deactive'} fw-medium  text-center align-content-center"
					onclick={() => penilaian = 'doa'}>
					Hafalan Doa
				</button>
				<button 
					type="button" 
					class="fs-5 col {penilaian === 'jilid' ? 'jenis-penilaian-active' : 'jenis penilaian-deactive'} fw-medium  text-center align-content-center"
					onclick={() => penilaian = 'jilid'}>
					Bacaan Jilid
				</button>
			</div>

			<div class="mb-3">
				<label 
					for="inputNama" 
					class="form-label">
					Nama Siswa
				</label>
				<input 
					type="text" 
					class="form-control" 
					id="inputNama"
					list="daftarSiswaList"
					placeholder="Masukkan nama siswa" 
					bind:value={namaSiswa}>
				<datalist id="daftarSiswaList">
					{#each daftarSiswa as siswa}
						<option value="{siswa.nama}"></option>
					{/each}
				</datalist>
				<!--
				<select 
					class="form-select mt-1" 
					bind:value={selectedSiswaId}
					aria-label="Pilih siswa">
					<option value="">Pilih siswa</option>
					{#each filteredSiswa as siswa}
						<option value={String(siswa.id)}>
							{siswa.nama}
						</option>
					{/each}
				</select>
				-->
			</div>

			{#if penilaian === "surat"}
				<div class="mb-3">
					<label 
						for="inputSurat" 
						class="form-label">
						Nama Surat
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputSurat"
						placeholder="Masukkan nama surat" 
						bind:value={input.surat.nama_surat}>
				</div>
				<div class="mb-3">
					<label 
						for="inputTanggal" 
						class="form-label">
						Tanggal Setor
					</label>
					<input 
						type="date" 
						class="form-control" 
						id="inputTanggal"
						placeholder="Masukkan tanggal"
						bind:value={input.surat.tanggal_setor}>
				</div>
				<div class="mb-3">
					<div class="d-flex justify-content-between">
						<div class="w-100 pe-3">
							<label 
								for="inputKelancaran" 
								class="form-label">
								Kelancaran
							</label>
							<input 
								type="number" 
								class="form-control" 
								id="inputKelancaran"
								placeholder="Masukkan nilai kelancaran"
								bind:value={input.surat.kelancaran}>
						</div>
						<div class="w-100">
							<label 
								for="inputKetepatanBacaan" 
								class="form-label">
								Ketepatan Bacaan
							</label>
							<input 
								type="number" 
								class="form-control" 
								id="inputKetepatanBacaan"
								placeholder="Masukkan nilai ketepatan"
								bind:value={input.surat.ketepatan_bacaan}>
						</div>
					</div>
				</div>
			{:else if penilaian === "doa"}
				<div class="mb-3">
					<label 
						for="inputNamaDoa" 
						class="form-label">
						Nama Doa
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaDoa"
						placeholder="Masukkan nama doa"
						bind:value={input.doa.nama_doa}>
				</div>
				<div class="mb-3">
					<label 
						for="inputTanggalSetor" 
						class="form-label">
						Tanggal Setor
					</label>
					<input 
						type="date" 
						class="form-control" 
						id="inputTanggalSetor"
						placeholder="Masukkan tanggal"
						bind:value={input.doa.tanggal_setor}>
				</div>
				<div class="mb-3">
					<label 
						for="inputNilai" 
						class="form-label">
						Nilai
					</label>
					<input 
						type="number" 
						class="form-control" 
						id="inputNilai"
						placeholder="Masukkan nilai"
						bind:value={input.doa.nilai}>
				</div>
			{:else if penilaian === "jilid"}
				<div class="mb-3">
					<label 
						for="inputMateriBacaan" 
						class="form-label">
						Materi Bacaan
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputMateriBacaan"
						placeholder="Masukkan materi bacaan"
						bind:value={input.jilid.materi_bacaan}>
				</div>
				<div class="mb-3">
					<label 
						for="inputTanggalSetor" 
						class="form-label">
						Tanggal Setor
					</label>
					<input 
						type="date" 
						class="form-control" 
						id="inputTanggalSetor"
						placeholder="Masukkan tanggal"
						bind:value={input.jilid.tanggal_setor}>
				</div>
				<div class="mb-3">
					<div class="d-flex justify-content-between">
						<div class="w-100 pe-3">
							<label 
								for="inputTajwid" 
								class="form-label">
								Tajwid
							</label>
							<input 
								type="number" 
								class="form-control" 
								id="inputTajwid"
								placeholder="Masukkan nilai tajwid"
								bind:value={input.jilid.nilai_tajwid}>
						</div>
						<div class="w-100">
							<label 
								for="inputMakhraj" 
								class="form-label">
								Makhraj
							</label>
							<input 
								type="number" 
								class="form-control" 
								id="inputMakhraj"
								placeholder="Masukkan nilai makhraj"
								bind:value={input.jilid.nilai_makhraj}>
						</div>
					</div>
				</div>
				<div class="mb-3">
					<label 
						for="inputKelancaran" 
						class="form-label">
						Kelancaran
					</label>
					<input 
						type="number" 
						class="form-control" 
						id="inputKelancaran"
						placeholder="Masukkan kelancaran"
						bind:value={input.jilid.nilai_kelancaran}>
				</div>
			{/if}
			<div class="d-flex">
				<button 
					type="button"
					class="btn border mx-2 w-50 {lulusUlang === 'lulus' ? 'bg-green text-white' : ''}"
					onclick={() => lulusUlang = 'lulus'}>Lulus</button>
				<button 
					type="button"
					class="btn border mx-2 w-50 {lulusUlang === 'ulang' ? 'bg-green text-white' : ''}"
					onclick={() => lulusUlang = 'ulang'}>Ulang</button>
			</div>
		</div>

		<div class="container border rounded py-4 mb-3">
			<h3 class="">Catatan Perkembangan </h3>
			<div class="mb-3">
				<label for="textAreaNote" class="form-label">
					Deskripsi Perilaku & Kendala
				</label>
				<textarea class="form-control" id="textAreaNote" rows="3"
					placeholder="Contoh: Ahmad sangat antusias hari ini, namun perlu bimbingan lebih pada penghafalan"
					bind:value={input[penilaian].note}></textarea>
			</div>
		</div>

		<div class="container d-flex justify-content-end">
			<a href="/pengajar/kelas/" class="btn border rounded w-50 mx-2">Batal</a>
			<!-- <a href="/pengajar/kelas/" class="btn border rounded w-50 mx-2 bg-green text-white">Simpan</a> -->
			<button 
				class="btn border rounded w-50 mx-2 bg-green text-white"
				onclick={handleSubmit}>
				Simpan
			</button>
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

	.jenis-penilaian-active {
		color: #338136;
		border: 2px solid;
		border-color: #338136;

		background-color: #F4F8FD;
	}

	.col {
		min-height: 150px;
		margin-right: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		padding: 20px;
	}
</style>
