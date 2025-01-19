import pandas as pd
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Membaca data dari file CSV
input_file = r'J:\Drive Saya\analisa sentimen git\gojek.csv'
output_file = r'J:\Drive Saya\analisa sentimen git\gojek-clear-data.csv'
data = pd.read_csv(input_file)

# Fungsi normalisasi untuk mengganti kata-kata tertentu dengan kata baku
normalisasi_kata = {"yg": "yang", "gk": "tidak", "dr": "dari", "dgn": "dengan"}  # contoh
def normalisasi(teks):
    for kata, pengganti in normalisasi_kata.items():
        teks = teks.replace(kata, pengganti)
    return teks

# Fungsi pembersihan data
def clean(teks):
    teks = re.sub(r'[^a-zA-Z\s]', '', teks)  # Menghapus simbol
    teks = teks.lower()  # Mengubah ke huruf kecil
    teks = normalisasi(teks)  # Melakukan normalisasi
    return teks

# Menerapkan pembersihan data pada kolom 'content'
data['content'] = data['content'].fillna('')  # Mengisi nilai kosong dengan string kosong
data['content'] = data['content'].apply(clean)

# Menghapus duplikat
data = data.drop_duplicates()

# Menghapus stopwords
stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.get_stop_words()
def hapus_stopwords(teks):
    return ' '.join([kata for kata in teks.split() if kata not in stopwords])

data['content'] = data['content'].apply(hapus_stopwords)

# Melakukan stemming
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()
data['content'] = data['content'].apply(stemmer.stem)

# Menyimpan hasil pembersihan ke file baru
data.to_csv(output_file, index=False)
