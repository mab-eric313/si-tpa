<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	let bendahara = $state({});
	let inputBendahara = $state({});
	let errorMessage = $state("");

	let selectPemasukan = $state("");
	let selectPengeluaran = $state("");

	let daftarSiswa = $state([]);
	let daftarKaryawan = $state([]);

	let id = $derived(Number($page.params.id));
	const endpoint = `http://localhost:8000/trg-transaksi/`;

	onMount(async () => {
		try {
			const [resTransaksi, resSiswa, resKaryawan] = await Promise.all([
				fetch(endpoint + id, { credentials: "include" }),
				fetch("http://localhost:8000/siswa/", { credentials: "include" }),
				fetch("http://localhost:8000/biodata-user/", { credentials: "include" }),
			]);

			if (!resTransaksi.ok) throw new Error(`Error transaksi: ${resTransaksi.statusText}`);
			if (!resSiswa.ok) throw new Error(`Error siswa: ${resSiswa.statusText}`);
			if (!resKaryawan.ok) throw new Error(`Error karyawan: ${resKaryawan.statusText}`);

			bendahara = await resTransaksi.json();
			daftarSiswa = await resSiswa.json();
			daftarKaryawan = await resKaryawan.json();

			inputBendahara = {
				nama: bendahara.nama ?? "",
				tanggal: bendahara.tanggal ?? "",
				kategori: bendahara.kategori ?? "",
				catatan: bendahara.note ?? "",
				nominal: bendahara.nominal ?? "",
				spp_siswa_id: bendahara.spp_siswa?.siswa?.id ?? "",
				gaji_pengajar_id: bendahara.gaji_pengajar?.biodata_user?.id ?? "",
				spp_siswa_nama: bendahara.spp_siswa?.siswa?.nama ?? "",
				gaji_pengajar_nama: bendahara.gaji_pengajar?.biodata_user?.nama_lengkap ?? "",
			};

			selectPemasukan = bendahara.spp_siswa ? "spp" : "";
			selectPengeluaran = bendahara.gaji_pengajar ? "gaji" : "";
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});

	let kategori = $derived(inputBendahara.kategori);

	let payload = $derived({
		kategori,
		tanggal: inputBendahara.tanggal,
		nama: inputBendahara.nama,
		nominal: Number(inputBendahara.nominal),
		note: inputBendahara.catatan,
		spp_siswa_id: kategori === "Pemasukan" && selectPemasukan === "spp"
			? daftarSiswa.find(s => s.id === inputBendahara.spp_siswa_id)?.id ?? null
			: null,
		gaji_pengajar_id: kategori === "Pengeluaran" && selectPengeluaran === "gaji"
			? daftarKaryawan.find(k => k.id === inputBendahara.gaji_pengajar_id)?.id ?? null
			: null,
	});
	$inspect(payload);

	async function handleSubmit() {
		if (!kategori) {
			errorMessage = "Pilih kategori Pemasukan atau Pengeluaran terlebih dahulu"
			return;
		}

		try {
			const response = await fetch(endpoint + id, {
				method: "PATCH",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payload)
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);

			const resJSON = await response.json();
			console.log(resJSON);
			goto("http://localhost:5173/bendahara/pemasukan");
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="sidebar-gap">
	<a href="/bendahara/pencatatan/" class="btn btn-light bi bi-arrow-left mb-5">
		Kembali
	</a>
	<form action="">
		<h1 class="mt-3">Pencatatan Kas</h1>
		<p class="mb-5">Dokumentasikan setiap sumber dana dengan detail untuk menjaga transparansi dan akuntabilitas keuangan lembaga.</p>
		<span class="fs-5 fw-medium">Pilih Kategori</span>
		<div class="mb-3 row mx-0">
			<button 
				type="button" 
				class="fs-5 col {kategori === 'Pemasukan' ? 'jenis-penilaian-active' : 'jenis penilaian-deactive'} fw-medium text-center align-content-center"
				onclick={() => kategori = 'Pemasukan'}>
				Pemasukan
			</button>
			<button 
				type="button" 
				class="fs-5 col {kategori === 'Pengeluaran' ? 'jenis-penilaian-active' : 'jenis penilaian-deactive'} fw-medium  text-center align-content-center"
				onclick={() => kategori = 'Pengeluaran'}>
				Pengeluaran
			</button>
		</div>
		<div class="container border rounded py-4 mb-3">
			{#if kategori === "Pemasukan"}
				<h2 class="mb-4">Formulir Pencatatan Pemasukan</h2>
			{:else if kategori === "Pengeluaran"}
				<h2 class="mb-4">Formulir Pencatatan Pengeluaran</h2>
			{/if}
			<div class="mb-3">
				{#if kategori === "Pemasukan"}
					<label 
				 		for="selectPemasukan"
						class="form-label">
						Pemasukan dari
					</label>
					<select id="selectPemasukan" class="form-select"
						 bind:value={selectPemasukan}>
						<option value="spp">SPP siswa</option>
						<option value="lainnya">Lainnya</option>
					</select>
					{#if selectPemasukan === "spp"}
						<div class="my-3">
							<label 
								for="inputNamaSiswa"
								class="form-label">
								Nama Siswa
							</label>
							<input 
								type="text" 
								class="form-control" 
								id="inputNamaSiswa"
								list="daftarSiswaList"
								placeholder="Masukkan nama siswa"
								bind:value={inputBendahara.spp_siswa_nama}>
							<datalist id="daftarSiswaList">
								{#each daftarSiswa as siswa}
									<option value="{siswa.nama}"></option>
								{/each}
							</datalist>
						</div>
					{/if}
				{:else if kategori === "Pengeluaran"}
					<label 
				 		for="selectPengeluaran"
						class="form-label">
						Pengeluaran untuk
					</label>
					<select name="" id="selectPengeluaran" class="form-select"
					   bind:value={selectPengeluaran}>
						<option value="gaji">Gaji karyawan</option>
						<option value="lainnya">Lainnya</option>
					</select>
					{#if selectPengeluaran === "gaji"}
						<div class="my-3">
							<label 
								for="inputNamaKaryawan"
								class="form-label">
								Nama Karyawan
							</label>
							<input 
								type="text" 
								class="form-control" 
								id="inputNamaKaryawan"
								list="daftarKaryawanList"
								placeholder="Masukkan nama karyawan"
								bind:value={inputBendahara.gaji_pengajar_nama}>
							<datalist id="daftarKaryawanList">
								{#each daftarKaryawan as karyawan}
									<option value={karyawan.nama_lengkap}></option>
									{/each}
							</datalist>
						</div>
					{/if}
				{/if}
			</div>
				<div class="mb-3">
					<label 
						for="inputNamaPencatatan"
						class="form-label">
						Nama Pencatatan
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputNamaPencatatan"
						placeholder="Masukkan nama pemasukan"
						bind:value={inputBendahara.nama}>
				</div>
				<div class="mb-3">
					<label 
						for="inputTanggal" 
						class="form-label">
						Tanggal Transaksi
					</label>
					<input 
						type="date" 
						class="form-control" 
						id="inputTanggal"
						placeholder="Masukkan tanggal transaksi"
						bind:value={inputBendahara.tanggal}>
				</div>
				<div class="mb-3">
					<label 
						for="inputCatatan" 
						class="form-label">
						Catatan
					</label>
					<input 
						type="text" 
						class="form-control" 
						id="inputCatatan"
						placeholder="Masukkan catatan"
						bind:value={inputBendahara.catatan}>
				</div>
				<div class="mb-3">
					<label 
						for="inputNominal" 
						class="form-label">
						Nominal
					</label>
					<input 
						type="number" 
						class="form-control" 
						id="inputNominal"
						placeholder="Masukkan nominal"
						bind:value={inputBendahara.nominal}>
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

