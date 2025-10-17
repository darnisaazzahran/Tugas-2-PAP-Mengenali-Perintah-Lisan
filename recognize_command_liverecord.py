import librosa
import numpy as np
import os
import sounddevice as sd
import scipy.spatial.distance as dist

# Folder data suara
DATASET_DIR = "data"

# Fungsi ekstraksi fitur MFCC
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13), axis=1)
    return mfcc

# Membuat template rata-rata setiap kata
def build_templates():
    templates = {}
    for label in os.listdir(DATASET_DIR):
        folder = os.path.join(DATASET_DIR, label)
        if not os.path.isdir(folder):
            continue

        features = []
        for file in os.listdir(folder):
            if file.endswith(".wav"):
                file_path = os.path.join(folder, file)
                features.append(extract_features(file_path))

        if len(features) > 0:
            templates[label] = np.mean(features, axis=0)
    return templates

# Fungsi untuk merekam suara input pengguna
def record_audio(duration=2, fs=16000):
    print("Silakan ucapkan perintah (misal: 'maju', 'mundur', 'berhenti', 'kiri', 'kanan')...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(recording)

# Menyimpan rekaman ke file sementara
def save_temp_audio(audio, filename="input.wav", fs=16000):
    import soundfile as sf
    sf.write(filename, audio, fs)

# Mencari perintah paling mirip
def recognize_command(input_file, templates):
    input_feat = extract_features(input_file)
    min_distance = float("inf")
    recognized_label = None

    for label, tmpl in templates.items():
        d = dist.euclidean(input_feat, tmpl)
        if d < min_distance:
            min_distance = d
            recognized_label = label

    return recognized_label, min_distance

# ===================== MAIN =====================
if __name__ == "__main__":
    print("=== Sistem Pengenalan Perintah Suara Sederhana ===")
    templates = build_templates()
    print(f"Template berhasil dibuat: {list(templates.keys())}")

    # Rekam suara pengguna
    audio = record_audio()
    save_temp_audio(audio)

    # Deteksi perintah
    label, jarak = recognize_command("input.wav", templates)
    print(f"\nPerintah dikenali sebagai: {label.upper()} (jarak={jarak:.2f})")
