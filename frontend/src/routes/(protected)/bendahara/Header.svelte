<!-- Header.svelte -->
<script>
	import { page } from '$app/state';

	// TODO: Use Lucide Icons
	// import { NotebookPen, FileUser } from "@lucide/svelte";
</script>

<svelte:head>
	<title>Sistem Informasi TPA</title>
</svelte:head>

<header>
	<ul class="nav-sidebar">
		<div class="nav-sidebar-main">
			<li class="logo">
				<h1>Bendahara</h1>
			</li>
			<li class="nav-sidebar-item">
				<a href="/bendahara" 
					class:active={page.url.pathname === "/bendahara"}>
					<!-- <div class="icon"><NotebookPen /></div> -->
					Beranda
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/bendahara/kelas" 
					class:active={page.url.pathname === "/bendahara/laporan"}>
					<!-- <img src={personsIcon} alt=""> -->
					Laporan
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/bendahara/absensi"
				   class:active={page.url.pathname === "/bendahara/pemasukan"}>
					<!-- <img src={checkSquareIcon} alt=""> -->
					Pemasukan
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/bendahara/rekap-nilai"
				   class:active={page.url.pathname === "/bendahara/pengeluaran"}>
					<!-- <div class="icon"><NotebookPen /></div> -->
					Pengeluaran
				</a>
			</li>
		</div>
		<li id="logout" class="nav-sidebar-item">
			<a href="/">
				<!-- <img src={exitIcon} alt="exit icon"> -->
				Logout
			</a>
		</li>
	</ul>
</header>

<style>
	header {
		margin: 0;
		position: sticky;
	}

	.logo {
		padding: 20px 20px;
		color: white;
		list-style: none;
	}

	.nav-sidebar {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		background-color: #1a3a2e;
		float: left;
		padding: 0 15px;
		min-height: 100vh;
	}

	.nav-sidebar-item {
		display: flex;
		flex-direction: row;
		align-items: center;
		margin: 8px 0;
		border-radius: 10px;
		list-style: none;
	}

	.nav-sidebar-item img {
		width: 23px;
		margin-right: 10px;
		pointer-events: none;
	}

	.nav-sidebar-item a {
		display: flex;
		color: white;
		text-decoration: none;
		padding: 10px 20px;
		width: 100%;
		align-items: center;
	}

	.nav-sidebar-item:hover {
		background-color: rgba(45, 106, 79);
		cursor: pointer;
	}

	.nav-sidebar-item:has(a.active) {
		background-color: rgba(45, 106, 79);
	}

	.icon {
		margin-right: 10px;
	}
</style>
