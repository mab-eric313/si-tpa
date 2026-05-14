<!-- Header.svelte -->
<script>
	import { resolve } from "$app/paths";
	import { page } from '$app/state';

	// Icons
	import accountIcon from "$lib/assets/account.svg";
	import calendarIcon from "$lib/assets/calendar4.svg";
	import checkSquareIcon from "$lib/assets/check2-square.svg";
	import currencyDollarIcon from "$lib/assets/currency-dollar.svg";
	import exitIcon from "$lib/assets/exit.svg";
	import faviconIcon from "$lib/assets/favicon.svg";
	import fileTextIcon from "$lib/assets/file-text.svg";
	import homeIcon from "$lib/assets/home.svg";
	import personsIcon from "$lib/assets/persons.svg";
</script>

<svelte:head>
	<title>Sistem Informasi TPA</title>
</svelte:head>

<header>
	<ul class="nav-sidebar">
		<div class="nav-sidebar-main">
			<li class="logo">
				<h1>SI-TPA</h1>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/dashboard' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/dashboard'} 
				   href={resolve('/dashboard')} data-page="dashboard.html">
					<img src={homeIcon} alt="account icon">
					Dashboard
				</a>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/data-siswa' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/data-siswa'} 
				   href={resolve('/data-siswa')} data-page="data-siswa.html">
					<img src={personsIcon} alt="persons icon">
					Data Siswa
				</a>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/absensi' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/absensi'} 
				   href={resolve('/absensi')} data-page="absensi.html">
					<img src={checkSquareIcon} alt="check square icon">
					Absensi
				</a>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/keuangan' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/keuangan'} 
				   href={resolve('/keuangan')} data-page="keuangan.html">
					<img src={currencyDollarIcon} alt="currency dollar icon">
					Keuangan
				</a>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/laporan-akdemik' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/laporan-akademik'} 
				   href={resolve('/laporan-akademik')} data-page="laporan-akademik.html">
					<img src={fileTextIcon} alt="file text icon">
					Laporan Akademik
				</a>
			</li>
			<li class="nav-sidebar-item" 
				aria-current={page.url.pathname === '/jadwal' ? 'page' : undefined}>
				<a class="nav-item" class:active={page.url.pathname === '/jadwal'} 
				   href={resolve('/jadwal')} data-page="jadwal.html">
					<img src={calendarIcon} alt="calendar icon">
					Jadwal
				</a>
			</li>
		</div>
		<div class="nav-sidebar-profile-logout">
			<li id="profile">
				<img src={accountIcon} alt="home icon">
				<div class="user">
					<p class="username">User</p>
					<p class="role">Admin</p>
				</div>
			</li>
			<li id="logout" class="nav-sidebar-item">
				<a href="#logout">
					<img src={exitIcon} alt="exit icon">
					Keluar
				</a>
			</li>
		</div>
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

	hr {
		width: 100%;
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

	#profile {
		display: flex;
		align-items: center;
		padding: 10px 20px;
		margin: 8px 0;
		border-radius: 10px;
		list-style: none;
		color: white;
	}

	#profile img {
		width: 35px;
		margin-right: 10px;
		color: white;
		background-color: yellow;
		border-radius: 20px;
	}

	#profile .user {
		display: flex;
		flex-direction: column;
	}

	#profile .user .username {
		font-weight: 600;
	}

	#profile .user .role {
		font-size: 12px;
	}

	.nav-sidebar-profile-logout {
		display: flex;
		float: left;
		flex-direction: column;
		padding-left: 0;
	}
</style>
