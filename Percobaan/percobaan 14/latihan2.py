import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import os

# Pastikan nltk tokenizer tersedia
nltk.download('punkt')

# Load file CSV
input_path = r"C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\file.csv"
data = pd.read_csv(input_path)

# Lakukan tokenisasi pada atribut "content"
data['tokenisasi'] = data['content'].apply(lambda x: word_tokenize(str(x)))

# Simpan hasil ke file baru
output_path = r"C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\file_token.csv"
data.to_csv(output_path, index=False)

output_path
