<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let selectedTabelPenilaian = $state("jilid");
	const endpointMap = {
		jilid: `${PUBLIC_API_BASE_URL}/penilaian-jilid/`,
		surat: `${PUBLIC_API_BASE_URL}/penilaian-surat/`,
		doa: `${PUBLIC_API_BASE_URL}/penilaian-doa/`,
	}

	let daftarPenilaian = $state([]);
	let errorDaftarPenilaian = $state("");

	/*
	onMount(async () => {
		try {
			const res = await fetch(endpointMap[selectedTabelPenilaian], {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			daftarPenilaian = await res.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorDaftarPenilaian = error.message;
		}
	});
	*/

	const kolomMap = {
		jilid: [
			{ key: "materi_bacaan", label: "Materi Bacaan" },
			{ key: "nilai_tajwid", label: "Nilai Tajwid" },
			{ key: "nilai_makhraj", label: "Nilai Makhraj" },
			{ key: "nilai_kelancaran", label: "Nilai Kelancaran" },
		],
		surat: [
			{ key: "nama_surat", label: "Nama Surat" },
			{ key: "kelancaran", label: "Kelancaran" },
			{ key: "ketepatan_bacaan", label: "Ketepatan Bacaan" },
		],
		doa: [
			{ key: "nama_doa", label: "Nama Doa" },
			{ key: "nilai", label: "Nilai" },
		],
	};
	let kolomAktif = $derived(kolomMap[selectedTabelPenilaian]);

	$effect(() => {
		const endpoint = endpointMap[selectedTabelPenilaian];
		fetch(endpoint, {
			method: "GET",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
		})
			.then(res => {
				if (!res.ok) throw new Error(`Error: ${res.statusText}`);
				return res.json();
			})
			.then(data => daftarPenilaian = data)
			.catch(err => errorDaftarPenilaian = err.message);
	});

	function handleAdd() {
		goto(`siswa/add`);
	}

	function handleEdit(id, siswa_id) {
		goto(`siswa/edit/${id}?penilaian=${selectedTabelPenilaian}&siswa_id=${siswa_id}`);
	}

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const endpoint = `${endpointMap[selectedTabelPenilaian]}${id}`;
			const res = await fetch(endpoint, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			})
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			daftarPenilaian = daftarPenilaian.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorDaftarPenilaian = error.message;
		}
	}

	let selectedKelasId = $state("");
	let filteredSiswa = $derived(
		selectedKelasId === ""
			? daftarSiswa
			: daftarSiswa.filter(siswa => siswa.kelas_id === Number(selectedKelasId))
	)
</script>

<section class="sidebar-gap">
	<div class="my-4">
		<h1>Kelola Data Kelas</h1>
		<span>Kelola informasi kelas dan pantau perkembangan mereka</span>
	</div>

	<div class="container border rounded">
		<div class="d-flex justify-content-between">
			<div class="ms-2 my-3 select-width">
				<span class="mb-2">Pilih Penilaian</span>
				<select 
					class="form-select text-center" 
					bind:value={selectedTabelPenilaian}
					aria-label="Pilih tabel penilian">
					<option value="jilid">Bacaan Jilid</option>
					<option value="surat">Hafalan Surat</option>
					<option value="doa">Hafalan Doa</option>
				</select>
			</div>
			<div class="me-2 mt-5">
				<button 
					class="btn btn-primary"
					onclick={handleAdd}>
					Tambah Data
				</button>
			</div>
		</div>

		<div>
			{#if errorDaftarPenilaian}
				<p class="text-danger">{errorDaftarPenilaian}</p>
			{:else if daftarPenilaian.length === 0}
				<p>Sedang memuat data...</p>
			{:else}
				<table class="table table-bordered text-center">
					<thead>
						<tr>
							<th class="fs-small">No</th>
							<th class="fs-small">Nama</th>
							{#each kolomAktif as kolom}
								<th class="fs-small">{kolom.label}</th>
							{/each}
							<th class="fs-small">Status</th>
							<th class="fs-small">Note</th>
							<th class="fs-small">Tanggal Setor</th>
							<th class="fs-small">Aksi</th>
						</tr>
					</thead>
					<tbody>
						{#each daftarPenilaian as item, i (item.id)}
							<tr>
								<td class="fs-small">{i + 1}</td>
								<td class="fs-small">{item.siswa.nama}</td>
								{#each kolomAktif as kolom}
									<td class="fs-small">{item[kolom.key]}</td>
								{/each}
								<td class="fs-small">{item.lulus_ulang}</td>
								<td class="fs-small">{item.note}</td>
								<td class="fs-small">{item.tanggal_setor}</td>
								<td>
									<button 
										class="btn btn-sm btn-primary fs-small" 
										onclick={() => handleEdit(item.id, item.siswa_id)}>
										<i class='bi bi-pencil-fill'></i>
										Edit
									</button>
									<button 
										class="btn btn-sm btn-danger fs-small" 
										onclick={() => handleDelete(item.id)}>
										<i class='bi bi-trash-fill'></i>
										Hapus
									</button>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			{/if}
		</div>
	</div>
</section>

<style>
	.sidebar-gap {
		padding-left: 240px; 
		position: relative; 
		min-height: 100vh;
	}

	tr:hover {
		background-color: #f1f5f9;
	}

	.select-width {
		width: 20%;
	}

	.fs-small {
		font-size: 15px;
	}
</style>
