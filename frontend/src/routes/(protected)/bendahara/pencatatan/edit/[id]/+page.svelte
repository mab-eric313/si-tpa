<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";
	import { handleInput, formatRibuan } from '$lib/utils';

	let bendahara = $state({});
	let inputBendahara = $state({});
	let errorMessage = $state("");

	let selectPemasukan = $state("");
	let selectPengeluaran = $state("");

	let nominalValue = $state(0);
	let nominalDisplay = $state("");

	let daftarSiswa = $state([]);
	let daftarKaryawan = $state([]);

	let id = $derived(Number($page.params.id));
	const endpoint = `${PUBLIC_API_BASE_URL}/trg-transaksi/`;

	onMount(async () => {
		try {
			const [resTransaksi, resSiswa, resKaryawan] = await Promise.all([
				fetch(endpoint + id, { credentials: "include" }),
				fetch(`${PUBLIC_API_BASE_URL}/siswa/`, { credentials: "include" }),
				fetch(`${PUBLIC_API_BASE_URL}/biodata-user/`, { credentials: "include" }),
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
				nominal: bendahara.nominal ?? 0,
				spp_siswa_id: bendahara.spp_siswa?.siswa?.id ?? "",
				gaji_pengajar_id: bendahara.gaji_pengajar?.biodata_user?.id ?? "",
				spp_siswa_nama: bendahara.spp_siswa?.siswa?.nama ?? "",
				gaji_pengajar_nama: bendahara.gaji_pengajar?.biodata_user?.nama_lengkap ?? "",
			};
			nominalValue = bendahara.nominal ?? 0;
			nominalDisplay = formatRibuan(nominalValue);

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
			goto(`/bendahara/pencatatan`);
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="content-section">
	<a href="/bendahara/pencatatan/" class="btn bg-white bi bi-arrow-left mb-2">
		Kembali
	</a>
	<form action="">
		<div class="container bg-white border rounded py-4 mb-3">
			<h1 class="mb-3 text-center">Pencatatan Kas</h1>
			<div class="mb-3">
				<label for="selectKategori" class="form-label">
					Pilih Kategori
				</label>
				<select name="" id="selectKategori" class="form-select"
					bind:value={kategori}>
					<option value="" disabled>Pilih Kategori</option>
					<option value="Pemasukan">Pemasukan</option>
					<option value="Pengeluaran">Pengeluaran</option>
				</select>
			</div>
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
					<div class="d-flex align-items-center">
						<span style="margin-right: 5px;">Rp</span>
						<input 
							type="text" 
							class="form-control" 
							id="inputNominal"
							placeholder="Masukkan nominal"
							bind:value={nominalDisplay}
							oninput={(e) => handleInput(e, inputBendahara)}
						/>
						<span style="margin-left: 5px;">,00</span>
					</div>
				</div>
			</div>
		<div class="container d-flex justify-content-end">
			<a href="/bendahara/pencatatan/" 
				class="btn btn-secondary border rounded w-50 mx-2">
				Batal
			</a>
			<button 
				class="btn border rounded w-50 mx-2 bg-green text-white"
				onclick={handleSubmit}>
				Simpan
			</button>
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

