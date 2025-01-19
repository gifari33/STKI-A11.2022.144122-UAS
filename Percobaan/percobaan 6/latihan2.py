import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# Pastikan Anda sudah mengunduh tokenizer yang diperlukan
nltk.download('punkt')

# Baca file CSV
input_path = "H:/My Drive/analisa sentimen git/percobaan 6/validation_results_processed.csv"
data = pd.read_csv(input_path)

# Tokenisasi pada kolom 'content' dan 'processed_content'
data['content_tokenized'] = data['content'].apply(lambda x: word_tokenize(str(x)))
data['processed_content_tokenized'] = data['processed_content'].apply(lambda x: word_tokenize(str(x)))

# Simpan hasilnya ke file CSV baru
output_path = "H:/My Drive/analisa sentimen git/percobaan 6/validation_results_tokenized.csv"
data.to_csv(output_path, index=False)

print(f"File berhasil disimpan di {output_path}")
