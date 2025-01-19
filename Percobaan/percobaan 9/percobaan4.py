import pandas as pd

# Baca dataset
data_path = r'J:\Drive Saya\analisa sentimen git\percobaan 9\validation_results_tokenized.csv'
df = pd.read_csv(data_path)

# Ubah kolom token yang berbentuk string ke dalam bentuk list
df['processed_content_tokenized'] = df['processed_content_tokenized'].apply(eval)

# Pisahkan data berdasarkan kata "gojek" di kategori Negatif dan Positif
negatif_driver = df[(df['Value'] == 'Negatif') & (df['processed_content_tokenized'].apply(lambda tokens: 'driver' in tokens))]
positif_driver = df[(df['Value'] == 'Positif') & (df['processed_content_tokenized'].apply(lambda tokens: 'driver' in tokens))]

# Tampilkan hasil dengan format yang diinginkan
print('Negatif - Kata: "driver"')
print('Jumlah Kemunculan:', len(negatif_driver))
print('Contoh Kalimat Negatif yang Mengandung "driver":')
for example in negatif_driver['processed_content'].tolist()[:3]:  # Tampilkan 3 contoh pertama
    print(f'"{example}"')

print("\n")

print('Positif - Kata: "driver"')
print('Jumlah Kemunculan:', len(positif_driver))
print('Contoh Kalimat Positif yang Mengandung "driver":')
for example in positif_driver['processed_content'].tolist()[:3]:  # Tampilkan 3 contoh pertama
    print(f'"{example}"')
