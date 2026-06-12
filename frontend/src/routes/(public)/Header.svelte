
<svelte:head>
	<title>Sistem Informasi TPA</title>
</svelte:head>

<div class="latar-navigasi">
	<header class="wadah-tengah">
		<div class="logo-sekolah">
		  <div class="kotak-ikon">
			<img
			  src="https://img.icons8.com/material-outlined/24/000000/book.png"
			  alt="Buku"
			  class="ikon-buku"
			/>
		  </div>
		  TPA Ar-Rahmah
		</div>
		<nav class="menu-tautan">
		  <a href="/">Beranda</a>
		  <a href="/pendaftaran">Pendaftaran</a>
		  <a href="/kegiatan">Kegiatan</a>
		  <a href="/kontak">Kontak</a>
		  <a href="/login">Login</a>
		</nav>
	</header>
</div>

<style>
  .wadah-tengah {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .latar-navigasi {
    background-color: var(--warna-hijau-gelap);
    padding-top: 15px;
    padding-bottom: 10px;
  }

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
  }

  .latar-navigasi {
    background-color: var(--warna-hijau-gelap);
    padding-top: 15px;
    padding-bottom: 10px;
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
  }

  .menu-tautan a {
    text-decoration: none;
    color: #333333;
    background-color: #ffffff;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 500;
  }

  .menu-tautan a.active {
    background-color: var(--warna-menu-aktif);
  }

  .menu-tautan a:hover {
    background-color: #e2e2e2;
  }

  @media (max-width: 768px) {
    header,
    .menu-tautan {
      flex-direction: column;
      gap: 15px;
    }
  }

</style>
