<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { authState } from '$lib/authStore.svelte';
	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	$effect(() => {
        if (!authState.isLoggedIn || 
			(authState.role !== 'Admin' && authState.role !== 'Pengajar')) {
            goto('/login');
        }
    });

	function handleEdit(id) {
		goto(`/pengajar/edit/${id}`);
	}

	function handleDelete(id) {
		goto(`/pengajar/delete/${id}`);
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
					method: "GET",
					headers: { "Content-Type": "application/json" },
					credentials: "include"
				}),
				fetch(`${PUBLIC_API_BASE_URL}/absensi/tanggal/${getLocalDate()}`, {
					method: "GET",
					headers: { "Content-Type": "application/json" },
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

{#if authState.isLoggedIn && (authState.role === 'Admin' || authState.role === 'Pengajar')}
<section class="content-section">
	<div class="row mb-5 g-3">
		<div class="col-6 col-md-3">
			<div class="text-center d-flex align-items-center justify-content-center border p-3 h-100 shadow-sm bg-body-tertiary rounded-3">
				<div class="rounded-circle rounded-icon bg-green">
					<i class="bi bi-check-lg text-white"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-card-title">Total Hadir</span>
					<span class="fs-card-desc" >{countTotalHadir} Siswa</span>
				</div>
			</div>
		</div>
		<div class="col-6 col-md-3">
			<div class="text-center d-flex align-items-center justify-content-center border p-3 h-100 shadow-sm bg-body-tertiary rounded-3">
				<div class="rounded-circle rounded-icon bg-yellow">
					<i class="bi bi-info-lg text-black"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-card-title">Izin/Sakit</span>
					<span class="fs-card-desc">{countTotalIzinSakit} Siswa</span>
				</div>
			</div>
		</div>
		<div class="col-6 col-md-3">
			<div class="text-center d-flex align-items-center justify-content-center border p-3 h-100 shadow-sm bg-body-tertiary rounded-3">
				<div class="rounded-circle rounded-icon bg-red">
					<i class="bi bi-x fw-bold text-white"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-card-title">Alpha</span>
					<span class="fs-card-desc">{countTotalAlpha} Siswa</span>
				</div>
			</div>
		</div>
		<div class="col-6 col-md-3">
			<div class="text-center d-flex align-items-center justify-content-center border p-3 h-100 shadow-sm bg-body-tertiary rounded-3">
				<div class="rounded-circle rounded-icon bg-primary">
					<i class="bi bi-calendar text-white" style="font-size: 20px;"></i>
				</div>
				<div class="px-3 d-flex flex-column">
					<span class="fs-card-title">Tanggal</span>
					<span class="fs-card-desc">{getFormattedDate()}</span>
				</div>
			</div>
		</div>
	</div>

	<div class="row g-3">
		<div class="col-12 col-md-6">
			<div class="shadow-none border pt-4 p-4 h-100 rounded-3">
				<h5 class="text-black text-center mb-4">Kelas Yang Diampu</h5>
				<div class="d-flex flex-column gap-3">
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Jilid 1-3</span>
							<span class="rounded-pill total-santri fs-card-count">
								{countSiswa1} Santri
							</span>
						</div>
						<!-- TODO: Schedule still static -->
						<span class="fs-card-desc">Senin & Rabu, 14:00-15:00</span>
					</div>
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Jilid 4-6</span>
							<span class="rounded-pill total-santri fs-card-count">
								{countSiswa2} Santri
							</span>
						</div>
						<span class="fs-card-desc">Selasa & Kamis, 16:00-17:00</span>
					</div>
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Al-Quran</span>
							<span class="rounded-pill total-santri fs-card-count">
								{countSiswa3} Santri
							</span>
						</div>
						<span class="fs-card-desc">Senin & Jumat, 18:00-19:00</span>
					</div>
				</div>
			</div>
		</div>
		<div class="col-12 col-md-6">
			<div class="shadow-none border pt-4 p-4 h-100 rounded-3">
				<h5 class="text-black text-center mb-4">Absensi</h5>
				<div class="d-flex flex-column gap-3">
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Jilid 1-3</span>
							<span class="rounded-pill status-absen fs-card-count {getAbsenClass(statusAbsensiKelas[1])}">
								{getAbsenLabel(statusAbsensiKelas[1])}
							</span>
						</div>
						<span class="fs-card-desc">Senin & Rabu, 14:00-15:00</span>
					</div>
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Jilid 4-6</span>
							<span class="rounded-pill status-absen fs-card-count {getAbsenClass(statusAbsensiKelas[2])}">
								{getAbsenLabel(statusAbsensiKelas[2])}
							</span>
						</div>
						<span class="fs-card-desc">Selasa & Kamis, 16:00-17:00</span>
					</div>
					<div class="shadow-sm border p-3 d-flex flex-column rounded-3 bg-warm-blue">
						<div class="d-flex justify-content-between">
							<span class="fs-card-title">Al-Quran</span>
							<span class="rounded-pill status-absen fs-card-count {getAbsenClass(statusAbsensiKelas[3])}">
								{getAbsenLabel(statusAbsensiKelas[3])}
							</span>
						</div>
						<span class="fs-card-desc">Senin & Jumat, 18:00-19:00</span>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
{:else}
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <p>Memverifikasi akses...</p>
    </div>
{/if}

<style>
	.bg-green {
		background-color: green;
	}

	.bg-yellow {
		background-color: yellow;
	}

	.bg-red {
		background-color: red;
	}

	.rounded-icon {
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 25px;
		width: 40px;
		height: 40px;
	}

	.fs-card-title {
		font-size: 18px;
	}

	.fs-card-desc {
		font-size: 16px;
	}

	.fs-card-count {
		font-size: 14px;
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

	.status-absen {
		display: flex;
		align-items: center;
		justify-content: center;

		width: 30%;
		height: 30px;

		color: white;
		background-color: #D2FAFE;
	}

	.sudah-absen { background-color: #338136; }
	.belum-absen { background-color: #FF0000; }
	.sedang-absen { background-color: #F2B50B; }

	.bg-warm-blue { background-color: #F3F9FF; }

	.bg-warm-blue {
		background-color: #F3F9FF;
	}

	.content-section {
		padding: 0;
	}

	.table-container {
		box-shadow: 0 2px 8px rgba(0,0,0,0.08);
	}

	.filter-section {
		background-color: #f8f9fa;
	}

	.table-responsive {
		overflow-x: auto;
		-webkit-overflow-scrolling: touch;
	}

	.btn-group-vertical {
		width: 100%;
	}

	@media (max-width: 768px) {
		.table-responsive {
			border-radius: 0 0 8px 8px;
		}

		.fs-card-title {
			font-size: 16px;
		}

		.fs-card-desc {
			font-size: 14px;
		}

		.fs-card-count {
			font-size: 12px;
		}
	}
</style>
