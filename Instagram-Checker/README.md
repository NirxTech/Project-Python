# Instagram Follow Check

Script Python sederhana untuk membandingkan data followers dan following dari Instagram. Tujuan utamanya adalah untuk mengecek:

- Siapa yang kamu follow tapi tidak follback kamu 🤔
- Siapa yang follow kamu tapi tidak kamu follback 😅

## 📦 Struktur File

Letakkan file berikut dalam folder yang sama dengan script:

- `followers_1.json`: File dari data followers (diunduh dari Instagram)
- `following.json`: File dari data following (diunduh dari Instagram)

## ▶️ Cara Menjalankan

1. Install Python (jika belum):
   https://www.python.org/downloads/

2. Jalankan skrip dengan perintah:

```bash
python instagram_check.py
Hasil akan ditampilkan langsung di terminal/command prompt.

📁 Cara Mendapatkan File JSON dari Instagram
Buka Instagram di browser.

Masuk ke Settings > Privacy and Security > Data Download.

Minta salinan data dan unduh file yang dikirim via email.

Ekstrak file ZIP dan cari file:

followers_1.json

following.json

Letakkan di direktori yang sama dengan script ini.

🧑‍💻 Lisensi
MIT License — silakan digunakan dan dimodifikasi sesuai kebutuhan.

yaml
Copy
Edit

---

Kalau kamu butuh file `requirements.txt` juga (walau script ini tidak butuh pustaka eksternal), kamu cukup buat file kosong atau isi:

```txt
# Tidak ada dependency eksternal
