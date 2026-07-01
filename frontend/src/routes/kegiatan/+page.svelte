<script>
  // Data kartu kegiatan
  const daftarKegiatan = [
    {
      judul: "Buka Puasa Bersama",
      tanggal: "15 Maret 2026",
      lokasi: "Halaman TPQ",
      deskripsi: "Buka puasa bersama santri, ustadz, dan orang tua santri",
      gambar:
        "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=400&q=80",
    },
    {
      judul: "Pelatihan Tahfidz",
      tanggal: "21 juni 2026",
      lokasi: "Ruang Tahfidz",
      deskripsi:
        "Program untuk membantu peserta menghafal Al-Qur'an secara terstruktur dan berkualitas.",
      gambar:
        "https://images.unsplash.com/photo-1542816417-0983c9c9ad53?auto=format&fit=crop&w=400&q=80",
    },
    {
      judul: "Khataman Al-Qur'an",
      tanggal: "17 Februari 2026",
      lokasi: "Musholla Ar-Rahmah",
      deskripsi: "kegiatan menamatkan pembacaan seluruh Al-Qur'an",
      gambar:
        "https://images.unsplash.com/photo-1609599006353-e629afabfe14?auto=format&fit=crop&w=400&q=80",
    },
  ];
</script>

<svelte:head>
  <title>Kegiatan - TPA Ar-Rahmah</title>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    rel="stylesheet"
  />
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
      <a href="/kegiatan" class="aktif">Kegiatan</a>
      <a href="/kontak">Kontak</a>
    </nav>
  </header>
</div>

<div class="latar-utama">
  <section class="bagian-pembuka wadah-tengah">
    <h1>
      <span class="teks-hijau-muda">Kegiatan & Informasi</span><br />
      <span class="teks-hijau-tua">Terbaru TPQ Ar-Rahmah</span>
    </h1>
    <p class="teks-deskripsi">
      Jangan ragu untuk menghubungi kami jika Anda memiliki pertanyaan atau
      ingin informasi<br />lebih lanjut tentang TPQ Al-Hikmah
    </p>
  </section>

  <section class="wadah-tengah">
    <div class="kumpulan-kartu-tiga">
      {#each daftarKegiatan as kegiatan}
        <div class="kartu-kegiatan">
          <img
            src={kegiatan.gambar}
            alt={kegiatan.judul}
            class="gambar-kegiatan"
          />
          <div class="isi-kartu">
            <h3>{kegiatan.judul}</h3>
            <div class="info-meta">
              <div class="meta-item">
                <img
                  src="https://img.icons8.com/material-outlined/16/777777/calendar.png"
                  alt="Tanggal"
                />
                {kegiatan.tanggal}
              </div>
              <div class="meta-item">
                <img
                  src="https://img.icons8.com/material-outlined/16/777777/marker.png"
                  alt="Lokasi"
                />
                {kegiatan.lokasi}
              </div>
            </div>
            <p>{kegiatan.deskripsi}</p>
          </div>
        </div>
      {/each}
    </div>
  </section>
</div>

<footer>
  <div class="wadah-tengah">
    <div class="isi-kaki-halaman">
      <div class="kolom-bawah">
        <h4>TPQ Ar-Rahmah</h4>
        <p>
          Taman Pendidikan Al-Qur'an yang berkomitmen membentuk generasi Qur'ani
        </p>
      </div>

      <div class="kolom-bawah">
        <h4>Lokasi</h4>
        <p>Gg. XIV No.A RT/RW 02/03,<br />Indro, kec. Kebomas, kab. Gresik</p>
      </div>

      <div class="kolom-bawah">
        <h4>Jam Belajar</h4>
        <p>
          Siang: Jilid 1,2,3<br />Sore: Jilid 1,2,3 & 4,5,6<br />Malam:
          Al-Qur'an
        </p>
      </div>
    </div>
    <div class="hak-cipta">&copy; 2026 TPQ Ar-Rahmah. All rights reserved.</div>
  </div>
</footer>

<style>
  :global(*) {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Inter", sans-serif;
  }

  :global(:root) {
    --warna-hijau-header: #27652a;
    --warna-hijau-teks: #4b7f39;
    --warna-latar-krem: #f3efe9;
    --warna-biru-dongker: #232b38;
    --warna-menu-aktif: #a3a3a3;
  }

  :global(body) {
    background-color: #ffffff;
    color: #333333;
    line-height: 1.6;
  }

  .wadah-tengah {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
  }

  /* --- Navigasi --- */
  .latar-navigasi {
    background-color: var(--warna-hijau-header);
    padding: 15px 0;
  }

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
  }

  .logo-sekolah {
    font-size: 22px;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .kotak-ikon {
    background-color: white;
    border-radius: 6px;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .ikon-buku {
    width: 20px;
    height: 20px;
  }

  .menu-tautan {
    display: flex;
    gap: 10px;
  }

  .menu-tautan a {
    text-decoration: none;
    color: #333333;
    background-color: #ffffff;
    padding: 6px 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
  }

  .menu-tautan a.aktif {
    background-color: var(--warna-menu-aktif);
    color: #111;
  }

  .menu-tautan a:hover {
    background-color: #e2e2e2;
  }

  /* --- Bagian Utama --- */
  .latar-utama {
    background-color: #f4f1ea;
    padding-top: 50px;
    padding-bottom: 80px;
  }

  .bagian-pembuka {
    text-align: center;
    margin-bottom: 40px;
  }

  .bagian-pembuka h1 {
    font-size: 36px;
    line-height: 1.3;
    margin-bottom: 15px;
    font-weight: 700;
  }

  .teks-hijau-muda {
    color: #618a49;
  }

  .teks-hijau-tua {
    color: #356730;
  }

  .teks-deskripsi {
    color: #333333;
    font-size: 15px;
    line-height: 1.6;
  }

  /* --- Kartu Kegiatan --- */
  .kumpulan-kartu-tiga {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }

  .kartu-kegiatan {
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  }

  .gambar-kegiatan {
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
  }

  .isi-kartu {
    padding: 24px;
  }

  .isi-kartu h3 {
    font-size: 18px;
    color: #111;
    margin-bottom: 12px;
    font-weight: 600;
  }

  .info-meta {
    margin-bottom: 15px;
  }

  .meta-item {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 8px;
  }

  .meta-item img {
    width: 16px;
    height: 16px;
    opacity: 0.6;
  }

  .isi-kartu p {
    color: #4b5563;
    font-size: 15px;
    line-height: 1.6;
  }

  /* --- Footer --- */
  footer {
    background-color: var(--warna-biru-dongker);
    color: #cccccc;
    padding: 50px 20px 20px;
  }

  .isi-kaki-halaman {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-bottom: 40px;
  }

  .kolom-bawah h4 {
    color: white;
    margin-bottom: 15px;
    font-weight: 600;
    font-size: 16px;
  }

  .kolom-bawah p {
    font-size: 13px;
    line-height: 1.6;
  }

  .hak-cipta {
    text-align: center;
    border-top: 1px solid #3a4556;
    padding-top: 20px;
    font-size: 12px;
    color: #888;
  }

  @media (max-width: 768px) {
    header,
    .menu-tautan {
      flex-direction: column;
      gap: 15px;
    }
    .kumpulan-kartu-tiga,
    .isi-kaki-halaman {
      grid-template-columns: 1fr;
    }
  }
</style>
