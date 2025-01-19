import pandas as pd

# Baca file CSV
file_path = r"C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\Gojek🏍 App Reviews.csv"  # Ganti dengan path file Anda
data = pd.read_csv(file_path)

# Fungsi untuk membersihkan spasi berlebihan
def clean_whitespace(column):
    return column.astype(str).str.strip().str.replace(r'\s+', ' ', regex=True)

# Terapkan pembersihan ke semua kolom teks
data_cleaned = data.apply(clean_whitespace)

# Simpan kembali data yang telah dibersihkan
output_path = "cleaned_data.csv"  # Ganti dengan nama file yang diinginkan
data_cleaned.to_csv(output_path, index=False)

print("Data telah dibersihkan dan disimpan ke", output_path)
