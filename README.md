# Tugas-2-PAP-Mengenali-Perintah-Lisan
## 🧩 Deskripsi Singkat

Program ini mengenali lima jenis perintah lisan menggunakan pendekatan template matching sederhana.
Setiap perintah memiliki beberapa contoh rekaman (dataset) yang digunakan untuk menghitung fitur MFCC (Mel-Frequency Cepstral Coefficients).
Ketika pengguna mengucapkan perintah baru, sistem akan mengekstraksi ciri-cirinya dan membandingkannya dengan template yang sudah disimpan menggunakan jarak Euclidean.

Metode ini termasuk pendekatan sederhana namun efektif untuk jumlah perintah yang terbatas.

## ⚙️ Fitur Utama

✅ Pengenalan suara offline tanpa koneksi internet

✅ Bisa mengenali 5 jenis perintah (`maju, mundur, berhenti, kiri, kanan`)

✅ Dua mode pengenalan:
- 🎤 Rekam langsung lewat mikrofon
- 🎧 Unggah file `.wav`
  
✅ Tampilan hasil pengenalan dan jarak antar kelas

✅ Bisa diperluas untuk menambah perintah lain

## 📂 Struktur Folder

data                                   ← folder database suara (suara contoh)

recognize_command_choicerecord.py      ← file utama

record_dataset.py                      ← file pembuatan database

README.md                              ← dokumentasi

Hasil Analisis.md                      ← laporan hasil analisis dari tugas

## 💻 Instalasi dan Persiapan

### 1️⃣ Clone Repositori
git clone https://github.com/<username>/pengenalan-perintah-lisan.git
cd pengenalan-perintah-lisan

