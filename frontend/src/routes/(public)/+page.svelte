<svelte:head>
  <title>TPA Ar-Rahmah</title>
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    rel="stylesheet"
  />
</svelte:head>

<div class="latar-hijau-terang">
  <section class="bagian-pembuka wadah-tengah">
    <h1>Selamat Datang di TPA Ar-Rahmah</h1>
    <p>
      Membentuk generasi Qur'ani yang berakhlak mulia, cerdas, dan berprestasi
    </p>
    <a href="/pendaftaran" class="tombol-daftar">Daftar Sekarang</a>
  </section>
</div>

<div class="latar-putih">
  <section class="bagian-profil wadah-tengah">
    <div class="gambar-profil"></div>
    <div class="teks-profil">
      <h2>Profil TPQ</h2>
      <p>
        Taman Pendidikan Al-Qur'an (TPQ) merupakan lembaga pendidikan keagamaan
        nonformal yang didedikasikan untuk membina anak-anak dalam memahami
        serta mencintai Al-Qur'an sejak dini.
      </p>
      <p>
        Berfokus pada kemampuan baca tulis Al-Qur'an sesuai kaidah tajwid, TPQ
        juga menjadi wadah pembentukan karakter melalui pengajaran dasar-dasar
        akidah, akhlak, dan praktik ibadah harian seperti shalat dan wudhu.
      </p>
    </div>
  </section>

  <section class="bagian-visi-misi wadah-tengah">
    <h2 class="judul-tengah">Visi & Misi</h2>
    <div class="kumpulan-kartu-dua">
      <div class="kotak-kartu">
        <h3>Visi</h3>
        <p>
          Mewujudkan generasi Qur'ani yang cerdas, bertaqwa, dan berakhlak
          mulia.
        </p>
      </div>

      <div class="kotak-kartu kartu-daftar-angka">
        <h3>Misi</h3>
        <ol>
          <li>
            Menyelenggarakan pembelajaran baca tulis Al-Qur'an yang benar sesuai
            kaidah tajwid.
          </li>
          <li>
            Menanamkan hafalan surat-surat pendek dan doa harian sejak dini.
          </li>
          <li>
            Membiasakan praktik ibadah dan pembentukan karakter Islami dalam
            kehidupan sehari-hari.
          </li>
        </ol>
      </div>
    </div>
  </section>

  <section class="bagian-berita wadah-tengah">
    <h2 class="judul-tengah">Berita & Informasi Terbaru</h2>
    <div class="kumpulan-kartu-tiga">
      <div class="kotak-berita">
        <h4>Pendaftaran Santri baru 2026</h4>
        <p>
          Pendaftaran santri baru untuk tahun ajaran 2026/2027 telah dibuka.
          Segera daftarkan putra-putri Anda!
        </p>
        <span class="tanggal-berita">1 Mei 2026</span>
      </div>

      <div class="kotak-berita">
        <h4>Lomba Tartil Al-Qur'an Tingkat Kecamatan</h4>
        <p>
          Alhamdulillah, santri TPQ Al-Hikmah meraih juara 1 dalam lomba tartil
          Al-Qur'an tingkat kecamatan.
        </p>
        <span class="tanggal-berita">1 Mei 2026</span>
      </div>

      <div class=""></div>
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
        <p>Gg. XIV No.4 RT/RW 02/03<br />Indro, Kec. Kebomas, Kab. Gresik</p>
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
    .bagian-profil,
    .kumpulan-kartu-dua,
    .kumpulan-kartu-tiga,
    .isi-kaki-halaman {
      flex-direction: column;
      grid-template-columns: 1fr;
    }
  }
</style>

