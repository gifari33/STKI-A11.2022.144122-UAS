import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Pastikan stopwords dan punkt sudah diunduh
nltk.download('punkt')
nltk.download('stopwords')

# Membuat stemmer untuk bahasa Indonesia menggunakan Sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Fungsi untuk normalisasi teks
def normalize_text(text):
    # Menghapus karakter non-alfanumerik dan mengubah menjadi huruf kecil
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

# Fungsi untuk tokenisasi, stop word removal, dan stemming
def preprocess_text(text):
    # Normalisasi
    text = normalize_text(text)
    
    # Tokenisasi
    tokens = word_tokenize(text)
    
    # Stop word removal
    stop_words = set(stopwords.words('indonesian'))  # Pastikan 'indonesian' telah didownload
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    return ' '.join(stemmed_tokens)

# Membaca file CSV
file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 6\validation_results-4.csv'
data = pd.read_csv(file_path)

# Menghapus duplikat
data = data.drop_duplicates()

# Menampilkan jumlah total data setelah menghapus duplikat
print(f"Jumlah total data setelah menghapus duplikat: {len(data)}")

# Menerapkan preprocessing ke kolom 'content'
data['processed_content'] = data['content'].astype(str).apply(preprocess_text)

# Menghitung jumlah positif dan negatif
jumlah_positif = len(data[data['score'] > 0])
jumlah_negatif = len(data[data['score'] < 0])

print(f"Jumlah positif: {jumlah_positif}")
print(f"Jumlah negatif: {jumlah_negatif}")

# Menyimpan DataFrame yang sudah diproses ke file CSV baru
output_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 6\validation_results_processed.csv'
data.to_csv(output_file_path, index=False)

print(f"Data yang sudah diproses disimpan di: {output_file_path}")

# Menampilkan beberapa contoh hasil preprocessing
print(data[['content', 'processed_content']].head())
