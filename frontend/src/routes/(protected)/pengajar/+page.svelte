<!-- TODO: All '...' is need to take data from database -->
<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	function handleEdit(id) {
		goto(`pengajar/edit/${id}`);
	}

	function handleDelete(id) {
		goto(`pengajar/delete/${id}`);
	}

	function getDate() {
		const now = new Date();
		const year = now.getFullYear();
		let initialMonth = now.getMonth() + 1;
		let month = $state(initialMonth < 10 ? '0' + initialMonth : String(initialMonth));
		const initialDate = now.getDate();
		let date = $state(initialDate < 10 ? '0' + initialDate : String(initialDate));

		return date + '-' + month + '-' + year
	}

	let daftarSiswa = $state([]);
	let errorMessage = $state("");

	onMount(async () => {
		try {
			const responseSiswa = await fetch(`${PUBLIC_API_BASE_URL}/siswa/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!responseSiswa.ok) throw new Error(`Error: ${responseSiswa.statusText}`);

			daftarSiswa = await responseSiswa.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});

	let countSiswa1 = $derived(daftarSiswa.filter(siswa => siswa.kelas_id === 1).length);
	let countSiswa2 = $derived(daftarSiswa.filter(siswa => siswa.kelas_id === 2).length);
    let countSiswa3 = $derived(daftarSiswa.filter(siswa => siswa.kelas_id === 3).length);

	let kelas = $derived(daftarKelas.filter(kelas => kelas.nama === 'jilid_1-3').length);
</script>

<!-- TODO (LOW): innerHTML still hardcoded -->
<section class="sidebar-gap">
	<h1 class="py-5">Selamat Datang, Ustadz ...</h1>
	<div class="container pb-5">
		<div class="row mb-5">
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-check-lg rounded-circle rounded-icon-total-hadir"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Total Hadir</span>
					<span>13 Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-info rounded-circle rounded-icon-izin-sakit"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Izin/Sakit</span>
					<span>2 Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-x rounded-circle rounded-icon-alpha"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Alpha</span>
					<span>0 Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<div class="rounded-circle rounded-icon-outer-tanggal">
					<i class="bi bi-calendar rounded-circle rounded-icon-tanggal"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Tanggal</span>
					<span>{getDate()}</span>
				</div>
			</div>
		</div>
		<div class="row">
			<div class="col shadow-none border pt-4">
				<h3 class="text-black text-center mb-4">Kelas Yang Diampu</h3>
				<div class="d-flex flex-column gap-3">
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Jilid 1-3</span>
							<span class="rounded-pill total-santri">
								{countSiswa1} Santri
							</span>
						</div>
						<span>Senin & Rabu, 14:00-15:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Jilid 4-6</span>
							<span class="rounded-pill total-santri">
								{countSiswa2} Santri
							</span>
						</div>
						<span>Selasa & Kamis, 16:00-15:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Al-Quran</span>
							<span class="rounded-pill total-santri">
								{countSiswa3} Santri
							</span>
						</div>
						<span>Senin & Jumat, 18:00-19:00</span>
					</div>
				</div>
			</div>
			<div class="col shadow-none border pt-4">
				<h3 class="text-black text-center mb-4">Absensi</h3>
				<div class="d-flex flex-column gap-3">
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Jilid 1-3</span>
							<span class="rounded-pill absen sudah-absen">
								Sudah Absen
							</span>
						</div>
						<span>Senin & Rabu, 14:00-15:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Jilid 4-6</span>
							<span class="rounded-pill absen belum-absen">
								Belum Absen
							</span>
						</div>
						<span>Selasa & Kamis, 16:00-15:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Al-Quran</span>
							<span class="rounded-pill absen sedang-absen">
								Sedang Absen
							</span>
						</div>
						<span>Senin & Jumat, 18:00-19:00</span>
					</div>
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

	.rounded-icon-total-hadir {
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

	.total-santri {
		display: flex;
		align-items: center;
		justify-content: center;

		width: 20%;
		height: 30px;

		color: #5495FE;
		background-color: #D2FAFE;
	}

	.absen {
		display: flex;
		align-items: center;
		justify-content: center;

		width: 30%;
		height: 30px;

		color: white;
		background-color: #D2FAFE;
	}

	.sudah-absen {
		background-color: #338136;
	}

	.belum-absen {
		background-color: #FF0000;
	}

	.sedang-absen {
		background-color: #F2B50B;
	}

	.bg-warm-blue {
		background-color: #F3F9FF;
	}

	.col {
		min-height: 150px;
		margin-right: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		padding: 20px;
	}

</style>
