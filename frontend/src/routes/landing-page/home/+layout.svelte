<style>
  /* Menggunakan :global() untuk elemen dasar web */
  :global(*) {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Inter", sans-serif;
  }

  :global(:root) {
    --warna-hijau-gelap: #1a4a20;
    --warna-hijau-terang: #2b7a33;
    --warna-teks-hijau: #268041;
    --warna-abu-tua: #24292e;
    --warna-menu-aktif: #9ea39e;
  }

  :global(body) {
    background-color: #ffffff;
    color: #333333;
    line-height: 1.6;
  }

  /* Sisa class di bawah ini akan di-scope khusus untuk komponen ini */
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

  .latar-hijau-terang {
    background-color: var(--warna-hijau-terang);
    color: white;
  }

  .bagian-pembuka {
    text-align: center;
    padding: 60px 20px 80px;
  }

  .bagian-pembuka h1 {
    font-size: 32px;
    margin-bottom: 10px;
  }

  .bagian-pembuka p {
    font-size: 14px;
    margin-bottom: 30px;
  }

  .tombol-daftar {
    background-color: white;
    color: var(--warna-teks-hijau);
    padding: 12px 36px;
    border-radius: 30px;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
  }

  .latar-putih {
    background-color: #ffffff;
    padding-bottom: 80px;
  }

  .bagian-profil {
    display: flex;
    gap: 40px;
    padding: 80px 20px 60px;
    align-items: center;
  }

  .teks-profil {
    flex: 1;
  }

  .teks-profil h2 {
    color: var(--warna-teks-hijau);
    font-size: 32px;
    margin-bottom: 20px;
  }

  .teks-profil p {
    color: #666666;
    margin-bottom: 15px;
    text-align: justify;
  }

  .judul-tengah {
    text-align: center;
    color: var(--warna-teks-hijau);
    font-size: 32px;
    margin-bottom: 30px;
  }

  .kumpulan-kartu-dua {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }

  .kotak-kartu {
    background: white;
    padding: 30px;
    border-radius: 8px;
    border: 1px solid #eeeeee;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }

  .kartu-daftar-angka ol {
    padding-left: 20px;
  }

  .kumpulan-kartu-tiga {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }

  .kotak-berita {
    background: #fdfdfd;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    position: relative;
    min-height: 200px;
  }

  .kotak-berita h4 {
    color: var(--warna-teks-hijau);
    margin-bottom: 10px;
  }

  .kotak-berita p {
    color: #666666;
    font-size: 13px;
    margin-bottom: 30px;
  }

  .tanggal-berita {
    position: absolute;
    bottom: 15px;
    right: 20px;
    font-size: 12px;
    color: #888888;
  }

  .kartu-kosong {
    background: transparent;
    border-style: dashed;
  }

  footer {
    background-color: var(--warna-abu-tua);
    color: #cccccc;
    padding: 50px 20px 20px;
  }

  .isi-kaki-halaman {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-bottom: 40px;
  }

  .kolom-bawah h4 {
    color: white;
    margin-bottom: 15px;
  }

  .hak-cipta {
    text-align: center;
    border-top: 1px solid #444444;
    padding-top: 20px;
    font-size: 11px;
  }

  @media (max-width: 768px) {
    header,
    .menu-tautan {
      flex-direction: column;
      gap: 15px;
    }
    .bagian-profil,
    .kumpulan-kartu-dua,
    .kumpulan-kartu-tiga,
    .isi-kaki-halaman {
      flex-direction: column;
      grid-template-columns: 1fr;
    }
  }
</style>
