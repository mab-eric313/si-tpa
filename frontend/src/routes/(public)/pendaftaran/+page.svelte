<script>
  // State untuk menyimpan data formulir pendaftaran
  // TODO: use $state()
  let namaSantri = '';
  let umur = '';
  let alamat = '';
  let namaWali = '';
  let whatsapp = '';
  let files = null;

  // Fungsi untuk menangani pengiriman form
  function handleSubmit() {
    // Validasi sederhana (karena semua field wajib diisi)
    if (!namaSantri || !umur || !alamat || !namaWali || !whatsapp) {
      alert('Mohon lengkapi semua data yang wajib diisi (*).');
      return;
    }

    const formData = {
      namaSantri,
      umur,
      alamat,
      namaWali,
      whatsapp,
      berkas: files ? files[0] : null
    };

    console.log('Data pendaftaran berhasil dikirim:', formData);
    alert('Pendaftaran berhasil dikirim! Admin akan segera menghubungi Anda.');
    
    // Reset form setelah sukses
    resetForm();
  }

  function resetForm() {
    namaSantri = '';
    umur = '';
    alamat = '';
    namaWali = '';
    whatsapp = '';
    files = null;
  }
</script>

<!-- UTAMA / CONTAINER -->
<div class="container">
  <div class="title">
    <h1>Pendaftaran Santri Baru</h1>
    <p>
      Silakan lengkapi form di bawah ini untuk mendaftarkan putra/putri Anda sebagai santri TPA Ar-Rahmah
    </p>
  </div>

  <!-- SYARAT -->
  <div class="card">
    <h2>Syarat Pendaftaran</h2>
    <ul>
      <li>Usia minimal 5 tahun</li>
      <li>Fotocopy Kartu Keluarga (KK)</li>
      <li>Fotocopy Akta Kelahiran</li>
      <li>Pas foto ukuran 3x4 (2 lembar)</li>
      <li>Mengisi formulir pendaftaran dengan lengkap</li>
    </ul>
  </div>

  <!-- FORM PENDAFTARAN -->
  <div class="card">
    <h2>Form Pendaftaran</h2>

    <form on:submit|preventDefault={handleSubmit}>
      <div class="form-group">
        <label for="nama-santri">Nama Lengkap Santri<span>*</span></label>
        <input 
          id="nama-santri"
          type="text" 
          placeholder="Masukkan nama lengkap" 
          bind:value={namaSantri}
          required
        />
      </div>

      <div class="form-group">
        <label for="umur">Umur<span>*</span></label>
        <input 
          id="umur"
          type="number" 
          placeholder="Masukkan umur" 
          bind:value={umur}
          min="5"
          required
        />
      </div>

      <div class="form-group">
        <label for="alamat">Alamat Lengkap<span>*</span></label>
        <textarea 
          id="alamat"
          placeholder="Masukkan alamat lengkap" 
          bind:value={alamat}
          required
        ></textarea>
      </div>

      <div class="form-group">
        <label for="nama-wali">Nama Orang Tua/Wali<span>*</span></label>
        <input 
          id="nama-wali"
          type="text" 
          placeholder="Masukkan nama orang tua/wali" 
          bind:value={namaWali}
          required
        />
      </div>

      <div class="form-group">
        <label for="whatsapp">Nomor Whatsapp<span>*</span></label>
        <input 
          id="whatsapp"
          type="text" 
          placeholder="contoh: 081234567890" 
          bind:value={whatsapp}
          required
        />
      </div>

      <div class="form-group">
        <label for="berkas">Upload Berkas (KK, Akta, Foto)<span>*</span></label>
        <div class="upload-box">
          <div class="upload-icon">⬆</div>
          
          <input 
            id="berkas"
            type="file" 
            accept="image/*,application/pdf"
            capture="environment"
            bind:files={files}
            required
          />

          <div class="upload-text">
            {#if files && files[0]}
              <span class="file-selected">Terpilih: {files[0].name}</span>
            {:else}
              format: JPG, PNG, PDF (Maks. 5MB per file)
            {/if}
          </div>
        </div>
      </div>

      <button type="submit" class="btn">
        Kirim Pendaftaran
      </button>
    </form>
  </div>

  <!-- INFORMASI TAMBAHAN -->
  <div class="card info-box">
    <h2>Informasi Tambahan</h2>
    <p>
      Setelah mengirimkan formulir, admin kami akan menghubungi Anda dalam 1-2 hari kerja untuk konfirmasi dan jadwal tes mengaji.
    </p>
    <br />
    <p>
      Untuk informasi lebih lanjut, hubungi:
      <b>+62 XXX XXXX XXXX</b>
    </p>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="footer-container">
    <div class="footer-box">
      <h3>TPA Ar-Rahmah</h3>
      <p>Tempat Pendidikan Al-Qur'an yang berkomitmen membentuk generasi Qurani</p>
    </div>

    <div class="footer-box">
      <h3>Lokasi</h3>
      <p>
        Ds. XYZ No.45 RT 02/03,<br />
        Indonesia
      </p>
    </div>

    <div class="footer-box">
      <h3>Jam Belajar</h3>
      <p>
        Senin - Jumat<br />
        Sore 15.30 - 17.00
      </p>
    </div>
  </div>
</footer>

<style>
  .navbar {
    background-color: #2f7d1f;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 40px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 10px;
    color: white;
    font-weight: bold;
    font-size: 22px;
  }

  .logo-box {
    width: 28px;
    height: 28px;
    background-color: white;
    border-radius: 5px;
  }

  .menu {
    display: flex;
    gap: 12px;
  }

  .menu a {
    text-decoration: none;
    color: black;
    background-color: white;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 14px;
    transition: 0.3s;
  }

  .menu a:hover {
    background-color: #d9ffd0;
  }

  .container {
    max-width: 850px;
    margin: 50px auto;
    padding: 0 20px;
  }

  .title {
    text-align: center;
    margin-bottom: 30px;
  }

  .title h1 {
    color: #4c8b2b;
    font-size: 42px;
    margin-bottom: 10px;
  }

  .title p {
    color: #666;
    font-size: 15px;
  }

  .card {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 25px;
  }

  .card h2 {
    color: #4c8b2b;
    margin-bottom: 18px;
    font-size: 34px;
  }

  .card ul {
    padding-left: 20px;
    color: #555;
    line-height: 1.8;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: block;
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: bold;
    color: #444;
  }

  .form-group span {
    color: red;
  }

  input,
  textarea {
    width: 100%;
    padding: 13px;
    border: 1px solid #ccc;
    border-radius: 6px;
    outline: none;
    transition: 0.3s;
  }

  input:focus,
  textarea:focus {
    border-color: #4c8b2b;
  }

  textarea {
    min-height: 100px;
    resize: vertical;
  }

  .upload-box {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 30px;
    text-align: center;
    color: #777;
  }

  .upload-icon {
    font-size: 40px;
    margin-bottom: 10px;
  }

  .upload-box input {
    border: none;
  }

  .upload-text {
    margin-top: 10px;
    font-size: 13px;
  }

  .file-selected {
    color: #2f7d1f;
    font-weight: bold;
  }

  .btn {
    width: 100%;
    background-color: #2f7d1f;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s;
  }

  .btn:hover {
    background-color: #256318;
  }

  .info-box {
    background-color: #e9eef5;
  }

  .info-box h2 {
    color: #222;
  }

  .info-box p {
    color: #555;
    line-height: 1.7;
  }

  .info-box b {
    color: black;
  }

  footer {
    background-color: #1f2937;
    color: white;
    padding: 35px 50px;
    margin-top: 50px;
  }

  .footer-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 30px;
  }

  .footer-box h3 {
    margin-bottom: 12px;
  }

  .footer-box p {
    color: #d1d5db;
    font-size: 14px;
    line-height: 1.7;
  }

  @media (max-width: 768px) {
    .navbar {
      flex-direction: column;
      gap: 15px;
    }

    .menu {
      flex-wrap: wrap;
      justify-content: center;
    }

    .title h1 {
      font-size: 30px;
    }

    .card h2 {
      font-size: 26px;
    }

    .footer-container {
      flex-direction: column;
    }
  }
</style>
