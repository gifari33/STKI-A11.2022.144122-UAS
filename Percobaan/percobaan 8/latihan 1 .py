import cudf

# Membaca file CSV menggunakan cuDF
file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 8\validation_results.csv'
data = cudf.read_csv(file_path)

# Menghitung jumlah nilai "Negatif" dan "Positif"
negatif_count = (data['Value'] == 'Negatif').sum()
positif_count = (data['Value'] == 'Positif').sum()

# Menampilkan hasil
print(f'Jumlah Negatif: {negatif_count}')
print(f'Jumlah Positif: {positif_count}')