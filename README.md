# Tugas-2-PAP-Mengenali-Perintah-Lisan
### Tugas Pengenalan Perintah Lisan ini menggunakan Metode Template Matching Berbasis MFCC
## 1. Latar Belakang
Kecerdasan buatan saat ini telah banyak diterapkan dalam interaksi manusia dan mesin, salah satunya melalui pengenalan perintah suara (speech command recognition).
Sistem semacam ini memungkinkan pengguna memberikan instruksi hanya melalui ucapan, tanpa perangkat input tambahan seperti keyboard atau mouse.

Dalam tugas ini, dibuat sebuah sistem sederhana untuk mengenali lima perintah dasar berbahasa Indonesia, yaitu:

> “maju”, “mundur”, “berhenti”, “kiri”, dan “kanan”.

Sistem diimplementasikan menggunakan metode sederhana berbasis Template Matching dan fitur MFCC (Mel-Frequency Cepstral Coefficients).
Pendekatan ini dipilih karena:
- Jumlah perintah terbatas (hanya 5 kelas).
- Tidak membutuhkan dataset besar atau pelatihan kompleks.
- Mudah diimplementasikan dan dijalankan secara offline.

## 2. Metodologi
a. Deskripsi Dataset
`maju, mundur, berhenti, kiri, kanan`

b. Spesifikasi Audio
- Format: `.wav`
- Durasi per file: ±1–1.5 detik
- Jumlah total: 15 file (3 kata × 5 contoh)

c. Pra-Pemrosesan
- Normalisasi audio menjadi mono, 16 kHz.
- Ekstraksi fitur MFCC menggunakan librosa.
- Ambil nilai rata-rata MFCC per file (13 koefisien).

d. Pelatihan
- Tidak dilakukan pelatihan seperti model ML.
- Template dibuat dengan menghitung rata-rata MFCC dari beberapa contoh tiap kelas.

e. Pengenalan
- Rekam suara baru.
- Ekstraksi fitur MFCC.
- Hitung jarak Euclidean antara input dan template setiap kelas.
- Pilih perintah dengan jarak terkecil sebagai hasil pengenalan.

f. Implementasi

Librari utama:

`librosa, numpy, scipy, sounddevice, soundfile`

## 3. Analisis dan Pembahasan
a. Kinerja Sistem

Dengan 5 kelas perintah dan total 15 file (3 contoh per kelas), sistem diuji menggunakan 10 ucapan baru.
Rata-rata tingkat keberhasilan mencapai 80–90% pada lingkungan tenang.
Kesalahan terjadi jika:
- Pengucapan sangat pelan atau cepat.
- Ada noise latar belakang.
- Mikrofon terlalu jauh dari mulut.

b. Keunggulan
- Tidak perlu pelatihan model besar.
- Ringan dan berjalan offline.
- Mudah diterapkan di perangkat sederhana (misalnya robot mini, Arduino + Raspberry Pi).

c. Keterbatasan
- Sensitif terhadap noise dan intonasi.
- Hanya efektif untuk jumlah kelas kecil.
- Tidak mengenali penutur baru dengan suara yang jauh berbeda.

## Kesimpulan

Sistem pengenal perintah suara sederhana berbasis MFCC + Template Matching berhasil mengenali lima perintah dasar (“maju”, “mundur”, “berhenti”, “kiri”, “kanan”) dengan akurasi yang cukup baik pada kondisi ideal.
Metode ini efektif untuk aplikasi kontrol sederhana berbasis suara, khususnya jika sumber daya terbatas.
Namun, untuk penggunaan di lingkungan nyata (noisy environment), disarankan menggunakan metode tambahan seperti model ML terlatih.
