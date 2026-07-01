<script>
  let nama = "";
  let email = "";
  let pesan = "";

  function kirimPesan() {
    alert("Pesan berhasil dikirim!");
  }
</script>

  <!-- Contact Section -->
  <section class="contact-section">
    <h1>Hubungi Kami</h1>

    <p class="subtitle">
      Jangan ragu untuk menghubungi kami jika Anda memiliki pertanyaan atau ingin
      informasi lebih lanjut tentang TPQ Al-Hikmah
    </p>

    <div class="contact-container">
      <!-- Informasi Kontak -->
      <div class="card">
        <h2>Informasi Kontak</h2>

        <div class="info-item">
          <div class="icon">📍</div>
          <div>
            <h3>Alamat</h3>
            <p>
              Gg. XIV No.A RT/RW 02/03,<br />
              Indro, kec. Kebomas, kab. Gresik, Jawa Timur
            </p>
          </div>
        </div>

        <div class="info-item">
          <div class="icon">📞</div>
          <div>
            <h3>No. Telp/Whatsapp</h3>
            <p>+62 812 3456 7890</p>
            <p>+62 890 1234 5678</p>
          </div>
        </div>

        <div class="info-item">
          <div class="icon">🕒</div>
          <div>
            <h3>Jam Operasional</h3>
            <p>Senin - Jumat: 15.00 - 17.00 WIB</p>
            <p>Sabtu - Minggu: 08.00 - 10.00 WIB</p>
          </div>
        </div>
      </div>

      <!-- Form -->
      <div class="card">
        <h2>Kirim Pesan</h2>

        <form on:submit|preventDefault={kirimPesan}>
          <label>Nama Lengkap Santri</label>
          <input
            type="text"
            bind:value={nama}
            placeholder="Masukkan nama lengkap"
          />

          <label>Email</label>
          <input
            type="email"
            bind:value={email}
            placeholder="Masukkan email"
          />

          <label>Pesan</label>
          <textarea
            bind:value={pesan}
            placeholder="Masukkan Pesan"
          ></textarea>

          <button type="submit">Kirim Pesan</button>
        </form>
      </div>
    </div>
  </section>

<style>
  :global(body) {
    margin: 0;
    font-family: "Poppins", sans-serif;
    background: #f4f2ee;
  }

  .page {
    min-height: 100vh;
  }

  .contact-section {
    padding: 60px 40px;
    text-align: center;
  }

  .contact-section h1 {
    color: #4c7d31;
    font-size: 52px;
    margin-bottom: 10px;
  }

  .subtitle {
    max-width: 700px;
    margin: auto;
    margin-bottom: 50px;
  }

  .contact-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    max-width: 1200px;
    margin: auto;
  }

  .card {
    background: #fafafa;
    border: 1px solid #d8d8d8;
    border-radius: 12px;
    padding: 30px;
    text-align: left;
  }

  .card h2 {
    color: #4c7d31;
    font-size: 38px;
    margin-bottom: 30px;
  }

  .info-item {
    display: flex;
    gap: 16px;
    margin-bottom: 30px;
  }

  .icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #d7f1de;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 20px;
  }

  .info-item h3 {
    margin: 0;
    font-size: 18px;
  }

  .info-item p {
    margin: 5px 0;
    color: #666;
  }

  /* Form */
  form {
    display: flex;
    flex-direction: column;
  }

  label {
    margin-bottom: 6px;
    font-weight: 500;
  }

  input,
  textarea {
    margin-bottom: 16px;
    padding: 12px;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    font-size: 14px;
  }

  textarea {
    height: 120px;
    resize: none;
  }

  button {
    background: #5b8d3e;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
  }

  button:hover {
    background: #4c7d31;
  }

</style>
