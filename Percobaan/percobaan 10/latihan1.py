import pandas as pd
import re
import nltk
import time
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Pastikan stopwords dan tokenizer yang diperlukan sudah diunduh
nltk.download('punkt')
nltk.download('stopwords')

# Membuat stemmer untuk bahasa Indonesia menggunakan Sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Fungsi untuk normalisasi teks
def normalize_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

# Fungsi untuk tokenisasi, stop word removal, dan stemming
def preprocess_text(text):
    text = normalize_text(text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    return ' '.join(stemmed_tokens)

# Fungsi untuk melacak waktu dan menampilkan progress
def track_progress(current, total, start_time):
    elapsed_time = time.time() - start_time
    average_time = elapsed_time / current if current > 0 else 0
    remaining_time = average_time * (total - current)
    print(f"Proses: {current}/{total} - Estimasi waktu tersisa: {remaining_time:.2f} detik")

# Path input dan output
input_path = r'H:\My Drive\analisa sentimen git\percobaan 10\validation_filtered.csv'
output_path = r'H:\My Drive\analisa sentimen git\percobaan 10\validation_tokenized-2.csv'

# Mulai proses membaca file CSV
start_time = time.time()
data = pd.read_csv(input_path)
print(f"File CSV dimuat - {len(data)} baris. Waktu yang dibutuhkan: {time.time() - start_time:.2f} detik")

# Menghapus duplikat
data = data.drop_duplicates()
print(f"Duplikat dihapus - {len(data)} baris tersisa. Waktu yang dibutuhkan: {time.time() - start_time:.2f} detik")

# Menerapkan preprocessing ke kolom 'content' dengan progress
start_preprocessing_time = time.time()
total_rows = len(data)
data['processed_content'] = ''

for index, row in data.iterrows():
    data.at[index, 'processed_content'] = preprocess_text(str(row['content']))
    if (index + 1) % 100 == 0 or (index + 1) == total_rows:  # Update progress setiap 100 baris atau di akhir
        track_progress(index + 1, total_rows, start_preprocessing_time)

print(f"Preprocessing selesai. Total waktu yang dibutuhkan: {time.time() - start_preprocessing_time:.2f} detik")

# Menghitung jumlah positif dan negatif
jumlah_positif = len(data[data['score'] > 0])
jumlah_negatif = len(data[data['score'] < 0])
print(f"Jumlah positif: {jumlah_positif}")
print(f"Jumlah negatif: {jumlah_negatif}")

# Tokenisasi pada kolom 'content' dan 'processed_content' dengan progress
start_tokenization_time = time.time()
data['content_tokenized'] = ''
data['processed_content_tokenized'] = ''

for index, row in data.iterrows():
    data.at[index, 'content_tokenized'] = word_tokenize(str(row['content']))
    data.at[index, 'processed_content_tokenized'] = word_tokenize(str(row['processed_content']))
    if (index + 1) % 100 == 0 or (index + 1) == total_rows:  # Update progress setiap 100 baris atau di akhir
        track_progress(index + 1, total_rows, start_tokenization_time)

print(f"Tokenisasi selesai. Total waktu yang dibutuhkan: {time.time() - start_tokenization_time:.2f} detik")

# Menyimpan DataFrame yang sudah diproses ke file CSV baru
data.to_csv(output_path, index=False)
print(f"Data yang sudah diproses disimpan di: {output_path}")

# Menampilkan waktu total untuk seluruh proses
print(f"Proses selesai dalam {time.time() - start_time:.2f} detik")

# Menampilkan beberapa contoh hasil preprocessing dan tokenisasi
print(data[['content', 'processed_content', 'content_tokenized', 'processed_content_tokenized']].head())
