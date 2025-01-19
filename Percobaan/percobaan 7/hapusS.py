import pandas as pd

# Baca file CSV
df = pd.read_csv("J:\\Drive Saya\\analisa sentimen git\\percobaan 5\\validation_results-3.csv")

# Hapus spasi berlebih pada setiap kolom
df = df.apply(lambda x: x.str.strip())

# Simpan hasil ke file CSV baru
df.to_csv("J:\\Drive Saya\\analisa sentimen git\\percobaan 7\\validation_results.csv", index=False)

print("Spasi berlebih telah dihapus.")