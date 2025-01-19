import pandas as pd
from collections import Counter

# Baca dataset
data_path = r'H:\My Drive\analisa sentimen git\percobaan 9\validation_results_tokenized.csv'
df = pd.read_csv(data_path)

# Ubah kolom token yang berbentuk string ke dalam bentuk list
df['processed_content_tokenized'] = df['processed_content_tokenized'].apply(eval)

# Pisahkan data berdasarkan sentimen
negatif_data = df[df['Value'] == 'Negatif']
positif_data = df[df['Value'] == 'Positif']

# Hitung frekuensi kata pada data negatif dan positif
negatif_words = Counter([word for tokens in negatif_data['processed_content_tokenized'] for word in tokens])
positif_words = Counter([word for tokens in positif_data['processed_content_tokenized'] for word in tokens])

# Tampilkan kata terbanyak di masing-masing kategori
top_negatif_word, top_negatif_count = negatif_words.most_common(1)[0]
top_positif_word, top_positif_count = positif_words.most_common(1)[0]

# Cari contoh kalimat untuk memahami konteks kata
negatif_examples = negatif_data[negatif_data['processed_content_tokenized'].apply(lambda tokens: top_negatif_word in tokens)]['processed_content'].tolist()
positif_examples = positif_data[positif_data['processed_content_tokenized'].apply(lambda tokens: top_positif_word in tokens)]['processed_content'].tolist()

# Output yang diformat
print("\n")
print(f'Kata yang Negatif')
print(f'Kata: "{top_negatif_word}"')
print(f'Jumlah Kemunculan: {top_negatif_count} kali')
print('Contoh Kalimat Negatif yang Mengandung "{}":'.format(top_negatif_word))
for example in negatif_examples[:5]:  # Tampilkan 5 contoh pertama
    print(f'"{example}"')

print("\n")

print(f'Kata yang Positif')
print(f'Kata: "{top_positif_word}"')
print(f'Jumlah Kemunculan: {top_positif_count} kali')
print('Contoh Kalimat Positif yang Mengandung "{}":'.format(top_positif_word))
for example in positif_examples[:5]:  # Tampilkan 5 contoh pertama
    print(f'"{example}"')
