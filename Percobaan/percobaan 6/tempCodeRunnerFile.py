import pandas as pd

# Baca dataset
data_path = r'J:\Drive Saya\analisa sentimen git\percobaan 6\validation_results_tokenized.csv'
df = pd.read_csv(data_path)

# Ubah kolom token yang berbentuk string ke dalam bentuk list
df['processed_content_tokenized'] = df['processed_content_tokenized'].apply(eval)

# Pisahkan data berdasarkan kata "gojek" di kategori Negatif dan Positif
negatif_gojek = df[(df['Value'] == 'Negatif') & (df['processed_content_tokenized'].apply(lambda tokens: 'gojek' in tokens))]
positif_gojek = df[(df['Value'] == 'Positif') & (df['processed_content_tokenized'].apply(lambda tokens: 'gojek' in tokens))]

# Tampilkan hasil dengan format yang diinginkan
print('Negatif - Kata: "gojek"')
print('Jumlah Kemunculan:', len(negatif_gojek))
print('Contoh Kalimat Negatif yang Mengandung "gojek":')
for example in negatif_gojek['processed_content'].tolist()[:3]:  # Tampilkan 3 contoh pertama
    print(f'"{example}"')

print("\n")

print('Positif - Kata: "gojek"')
print('Jumlah Kemunculan:', len(positif_gojek))
print('Contoh Kalimat Positif yang Mengandung "gojek":')