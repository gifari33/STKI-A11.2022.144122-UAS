import pandas as pd
import ast
from collections import Counter

# Path input dan output
input_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\data_tokenisasi.csv'
output_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 12\data_Preprocessing.csv'
stopwords_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 12\data stopwords.txt'

# Load dataset
df = pd.read_csv(input_path)

# 1. Menghapus data duplikat
df = df.drop_duplicates()

# 2. Load stopwords dari file
with open(stopwords_path, 'r') as file:
    custom_stopwords = set([line.strip().lower() for line in file])

# Fungsi untuk membersihkan tokens
def preprocess_tokens(tokens_str):
    try:
        # Konversi string ke list menggunakan ast.literal_eval
        tokens = ast.literal_eval(tokens_str)
    except (ValueError, SyntaxError):
        # Jika tidak bisa dikonversi, kembalikan list kosong
        tokens = []
    
    # Lowercasing dan menghapus stopwords
    return [word.lower() for word in tokens if word.lower() not in custom_stopwords]

# 3. Terapkan preprocessing pada kolom 'tokenisasi' dan tambahkan kolom baru 'data_Preprocessing'
df['data_Preprocessing'] = df['tokenisasi'].apply(preprocess_tokens)

# Simpan hasil ke CSV
df.to_csv(output_path, index=False)
print(f"Proses selesai! Data dengan kolom tambahan disimpan di {output_path}")

# Analisis frekuensi kata pada kolom 'data_Preprocessing'
# 4. Load data preprocessed
df_preprocessed = pd.read_csv(output_path)

# Parse kolom 'data_Preprocessing' menjadi list
df_preprocessed['data_Preprocessing'] = df_preprocessed['data_Preprocessing'].apply(ast.literal_eval)

# Flatten semua kata menjadi satu list
all_words = [word for row in df_preprocessed['data_Preprocessing'] for word in row]

# Hitung frekuensi kata
word_counts = Counter(all_words)

# Ambil 100 kata paling umum
most_common_words = word_counts.most_common(100)

# Tampilkan hasil
print("100 Kata Paling Umum:")
for word, count in most_common_words:
    print(f"{word}: {count}")
