import pandas as pd

# Memuat dataset
# Misalnya, data Anda berada dalam file CSV
df = pd.read_csv('Gojek 1000 data.csv')

# Menghapus kolom 'score', 'at', dan 'appVersion'
df = df.drop(columns=['score', 'at', 'appVersion'])

# Menyimpan dataset yang telah dimodifikasi ke dalam file CSV baru
df.to_csv('gojek.csv', index=False)

print("Dataset telah disimpan sebagai 'gojek.csv'")
