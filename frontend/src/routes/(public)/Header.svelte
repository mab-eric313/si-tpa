<svelte:head>
	<title>Sistem Informasi TPA</title>
</svelte:head>

<script>
	let isMenuOpen = $state(false);

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}
</script>

<nav class="latar-navigasi">
	<header class="wadah-tengah">
		<div class="logo-sekolah">
			<div class="kotak-ikon">
				<img
					src="https://img.icons8.com/material-outlined/24/000000/book.png"
					alt="Buku"
					class="ikon-buku"
				/>
			</div>
			<span>TPA Ar-Rahmah</span>
		</div>
		<button 
			class="tombol-hamburger" 
			onclick={toggleMenu} 
			aria-label="Buka menu navigasi"
			aria-expanded={isMenuOpen}
		>
			<span class="garis"></span>
			<span class="garis"></span>
			<span class="garis"></span>
		</button>
		<nav class="menu-tautan" class:active={isMenuOpen}>
			<a href="/">Beranda</a>
			<a href="/pendaftaran">Pendaftaran</a>
			<a href="/kegiatan">Kegiatan</a>
			<a href="/kontak">Kontak</a>
			<a href="/login" class="tombol-login">Login</a>
		</nav>
	</header>
</nav>

<style>
	.wadah-tengah {
		max-width: 1000px;
		margin: 0 auto;
		padding: 0 20px;
		position: relative;
	}

	.latar-navigasi {
		background-color: var(--warna-hijau-gelap, #1a4d2e);
		padding-top: 15px;
		padding-bottom: 15px;
	}

	header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		color: white;
	}

	.logo-sekolah {
		font-size: 24px;
		font-weight: bold;
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.kotak-ikon {
		background-color: white;
		border-radius: 8px;
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.ikon-buku {
		width: 24px;
		height: 24px;
	}

	.menu-tautan {
		display: flex;
		gap: 12px;
		align-items: center;
	}

	.menu-tautan a {
		text-decoration: none;
		color: #333333;
		background-color: #ffffff;
		padding: 8px 16px;
		border-radius: 8px;
		font-size: 15px;
		font-weight: 500;
		transition: background-color 0.2s ease;
	}

	.menu-tautan a:hover {
		background-color: #e2e2e2;
	}

	/*
	.menu-tautan a.tombol-login {
		background-color: var(--warna-menu-aktif, #d4edda);
		font-weight: 600;
	}
	*/

	.tombol-hamburger {
		display: none;
		flex-direction: column;
		justify-content: space-around;
		width: 30px;
		height: 25px;
		background: transparent;
		border: none;
		cursor: pointer;
		padding: 0;
		z-index: 20;
	}

	.tombol-hamburger .garis {
		width: 100%;
		height: 3px;
		background-color: white;
		border-radius: 2px;
		transition: all 0.3s ease;
	}
	
	@media (max-width: 768px) {
		.tombol-hamburger {
			display: flex;
		}
		.menu-tautan {
			position: absolute;
			top: 100%;
			left: 0;
			width: 100%;
			background-color: var(--warna-hijau-gelap, #1a4d2e);
			flex-direction: column;
			gap: 5px;
			align-items: center;
			padding: 0;
			max-height: 0;
			overflow: hidden;
			transition: max-height 0.4s ease-out, padding 0.4s ease;
			box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
			z-index: 10;
		}

		.menu-tautan.active {
			max-height: 400px;
			padding: 20px 0;
		}

		.menu-tautan a {
			width: 85%;
			text-align: center;
			margin: 6px 0;
			padding: 15px 0;
			color: white;
			background-color: rgba(255, 255, 255, 0.1);
			border: 1px solid rgba(255, 255, 255, 0.2);
		}

		.menu-tautan a:hover {
			background-color: rgba(255, 255, 255, 0.2);
		}

		.menu-tautan a.tombol-login {
			background-color: white;
			color: var(--warna-hijau-gelap, #1a4d2e);
			margin-top: 10px;
		}
	}

</style>
