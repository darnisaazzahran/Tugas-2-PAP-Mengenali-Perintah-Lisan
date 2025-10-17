import os
import numpy as np
import librosa
import sounddevice as sd
import soundfile as sf
import scipy.spatial.distance as dist

# ==============================
# 1️⃣ FUNGSI EKSTRAKSI FITUR
# ==============================
def extract_features(file_path):
    """Ekstraksi MFCC dari file suara."""
    y, sr = librosa.load(file_path, sr=None)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)
    return mfcc

# ==============================
# 2️⃣ MEMBANGUN TEMPLATE SETIAP PERINTAH
# ==============================
def build_templates(dataset_dir="data"):
    """Bangun template MFCC rata-rata untuk tiap kelas perintah."""
    templates = {}
    for label in os.listdir(dataset_dir):
        folder = os.path.join(dataset_dir, label)
        if not os.path.isdir(folder):
            continue
        feats = []
        for f in os.listdir(folder):
            if f.endswith(".wav"):
                try:
                    feats.append(extract_features(os.path.join(folder, f)))
                except Exception as e:
                    print(f"Gagal memproses {f}: {e}")
        if len(feats) > 0:
            templates[label] = np.mean(feats, axis=0)
            print(f"✅ Template '{label}' berhasil dibuat ({len(feats)} file).")
    return templates

# ==============================
# 3️⃣ REKAM SUARA LANGSUNG
# ==============================
def record_audio(file_path="input.wav", duration=2, fs=16000):
    """Rekam suara pengguna langsung dari mikrofon."""
    print("\n🎤 Ucapkan perintah sekarang...")
    rec = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    sf.write(file_path, rec, fs)
    print("✅ Rekaman selesai disimpan ke:", file_path)
    return file_path

# ==============================
# 4️⃣ PENGENALAN PERINTAH
# ==============================
def recognize_command(file_path, templates):
    """Klasifikasi suara berdasarkan jarak Euclidean ke setiap template."""
    inp = extract_features(file_path)
    min_d, cmd = float("inf"), None
    for label, tmpl in templates.items():
        d = dist.euclidean(inp, tmpl)
        if d < min_d:
            min_d, cmd = d, label
    print(f"\n🎯 Hasil pengenalan: {cmd.upper()} (jarak={min_d:.2f})")
    return cmd

# ==============================
# 5️⃣ PROGRAM UTAMA
# ==============================
def main():
    print("=======================================")
    print("  SISTEM PENGENALAN PERINTAH LISAN")
    print("=======================================")
    print("Perintah yang dikenali: maju | mundur | berhenti | kiri | kanan")
    print("---------------------------------------")

    # Bangun template dari dataset
    templates = build_templates("data")

    while True:
        print("\nPilih mode pengenalan:")
        print("1. 🎙️ Rekam langsung dari mikrofon")
        print("2. 📁 Gunakan file audio (.wav)")
        print("3. ❌ Keluar")
        choice = input("Masukkan pilihan (1/2/3): ").strip()

        if choice == "1":
            # Mode rekam langsung
            file_path = record_audio()
            recognize_command(file_path, templates)

        elif choice == "2":
            # Mode upload file
            file_path = input("\nMasukkan path lengkap file .wav: ").strip()
            if os.path.exists(file_path):
                recognize_command(file_path, templates)
            else:
                print("⚠️ File tidak ditemukan, coba lagi.")

        elif choice == "3":
            print("\n👋 Program selesai. Terima kasih!")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi.")

# ==============================
# 6️⃣ EKSEKUSI PROGRAM
# ==============================
if __name__ == "__main__":
    main()
