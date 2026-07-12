<!-- TODO: class schedule still static -->
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

	function getFormattedDate() {
		const now = new Date();
		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		return `${day}-${month}-${year}`;
	}

	function getLocalDate() {
		const now = new Date();
		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	let daftarSiswa = $state([]);
	let daftarAbsensi = $state([]);
	let errorMessage = $state("");

	onMount(async () => {
		try {
			const [resSiswa, resAbsensi] = await Promise.all([
				fetch(`${PUBLIC_API_BASE_URL}/siswa/`, {
					credentials: "include"
				}),
				fetch(`${PUBLIC_API_BASE_URL}/absensi/tanggal/${getLocalDate()}`, {
					credentials: "include"
				}),
			]);

			if (!resSiswa.ok) throw new Error(`Error: ${resSiswa.statusText}`);
			if (!resAbsensi.ok) throw new Error(`Error: ${resAbsensi.statusText}`);

			daftarSiswa = await resSiswa.json();
			daftarAbsensi = await resAbsensi.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});

	let countTotalHadir = $derived(
		daftarAbsensi.filter(a => a.kehadiran === "Hadir").length
	);
	let countTotalIzinSakit = $derived(
		daftarAbsensi.filter(a => a.kehadiran === "Izin" || a.kehadiran === "Sakit").length
	);
	let countTotalAlpha = $derived(
		daftarAbsensi.filter(a => a.kehadiran === "Alpha").length
	);

	let countSiswa1 = $derived(daftarSiswa.filter(s => s.kelas_id === 1).length);
	let countSiswa2 = $derived(daftarSiswa.filter(s => s.kelas_id === 2).length);
    let countSiswa3 = $derived(daftarSiswa.filter(s => s.kelas_id === 3).length);

	let statusAbsensiKelas = $derived.by(() => {
		const result = {};
		[1, 2, 3].forEach(kelasId => {
			const siswaDiKelas = daftarSiswa.filter(s => s.kelas_id === kelasId);
			const totalSiswa = siswaDiKelas.length;

			if (totalSiswa === 0) {
				result[kelasId] = "belum";
				return;
			}

			const siswaSudahAbsen = siswaDiKelas.filter(siswa =>
				daftarAbsensi.some(absen => absen.siswa_id === siswa.id)
			).length;

			if (siswaSudahAbsen === 0) {
				result[kelasId] = "belum";
			} else if (siswaSudahAbsen === totalSiswa) {
				result[kelasId] = "sudah";
			} else {
				result[kelasId] = "sedang";
			}
		});
		return result;
	});

	function getAbsenClass(status) {
		switch(status) {
			case "sudah": return "sudah-absen";
			case "belum": return "belum-absen";
			case "sedang": return "sedang-absen";
			default: return "belum-absen";
		}
	}

	function getAbsenLabel(status) {
		switch(status) {
			case "sudah": return "Sudah Absen";
			case "belum": return "Belum Absen";
			case "sedang": return "Sedang Absen";
			default: return "Belum Absen";
		}
	}
</script>

<section class="sidebar-gap">
	<h1 class="py-5">Selamat Datang, Ustadz ...</h1>
	<div class="container pb-5">
		<div class="row mb-5">
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-check-lg rounded-circle rounded-icon-total-hadir"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Total Hadir</span>
					<span>{countTotalHadir} Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-info rounded-circle rounded-icon-izin-sakit"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Izin/Sakit</span>
					<span>{countTotalIzinSakit} Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<i class="bi bi-x rounded-circle rounded-icon-alpha"></i>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Alpha</span>
					<span>{countTotalAlpha} Siswa</span>
				</div>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center shadow-none border">
				<div class="rounded-circle rounded-icon-outer-tanggal">
					<i class="bi bi-calendar rounded-circle rounded-icon-tanggal"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-5">Tanggal</span>
					<span>{getFormattedDate()}</span>
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
						<span>Selasa & Kamis, 16:00-17:00</span>
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
							<span class="rounded-pill absen {getAbsenClass(statusAbsensiKelas[1])}">
								{getAbsenLabel(statusAbsensiKelas[1])}
							</span>
						</div>
						<span>Senin & Rabu, 14:00-15:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Jilid 4-6</span>
							<span class="rounded-pill absen {getAbsenClass(statusAbsensiKelas[2])}">
								{getAbsenLabel(statusAbsensiKelas[2])}
							</span>
						</div>
						<span>Selasa & Kamis, 16:00-17:00</span>
					</div>
					<div class="shadow-none border p-3 d-flex flex-column rounded-4 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-4">Al-Quran</span>
							<span class="rounded-pill absen {getAbsenClass(statusAbsensiKelas[3])}">
								{getAbsenLabel(statusAbsensiKelas[3])}
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

	.sudah-absen { background-color: #338136; }
	.belum-absen { background-color: #FF0000; }
	.sedang-absen { background-color: #F2B50B; }

	.bg-warm-blue { background-color: #F3F9FF; }

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
