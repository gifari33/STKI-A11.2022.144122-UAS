import os

# Path ke folder utama
base_folder = r"C:\Users\ghiff\Downloads\upload\STKI-A11.2022.144122-UAS\Percobaan"

# Cari dan hapus semua file .csv di dalam folder dan subfolder
for root, _, files in os.walk(base_folder):
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"File {file_path} berhasil dihapus.")
            except Exception as e:
                print(f"Gagal menghapus file {file_path}: {e}")

print("Proses penghapusan selesai.")
