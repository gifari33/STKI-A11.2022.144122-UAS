import pandas as pd

# Tentukan path file
file_path = r"C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\data_sentien.csv"

# Baca data CSV
df = pd.read_csv(file_path)

# Hitung jumlah sentimen
sentimen_counts = df['sentimen'].value_counts()

print(sentimen_counts)

# Hitung jumlah sentimen dan konversi ke persentase
sentimen_counts = df['sentimen'].value_counts(normalize=True) * 100

print(sentimen_counts)