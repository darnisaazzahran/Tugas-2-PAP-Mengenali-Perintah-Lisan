import sounddevice as sd
import soundfile as sf
import os

commands = ["maju", "mundur", "berhenti", "kiri", "kanan"]
save_dir = "data"
fs = 16000  # sample rate
duration = 2  # durasi rekaman per contoh (detik)
n_samples = 3  # jumlah contoh per kata

os.makedirs(save_dir, exist_ok=True)

for cmd in commands:
    cmd_dir = os.path.join(save_dir, cmd)
    os.makedirs(cmd_dir, exist_ok=True)
    print(f"\n=== Merekam kata '{cmd}' ===")

    for i in range(1, n_samples + 1):
        input(f"\nTekan [Enter] lalu ucapkan '{cmd}' ({i}/{n_samples})...")
        print("Rekam...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
        sd.wait()
        file_path = os.path.join(cmd_dir, f"{cmd}{i}.wav")
        sf.write(file_path, audio, fs)
        print(f"Tersimpan: {file_path}")

print("\nSelesai! Semua data suara tersimpan di folder 'data/'.")