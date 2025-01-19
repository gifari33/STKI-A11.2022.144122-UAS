import pandas as pd
import ast

# Path dataset
preprocessing_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\data_Preprocessing.csv'
sentiment_words_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\positive dan negative.csv'
output_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\data_sentien.csv'

# Load dataset preprocessing dan sentiment words
df_preprocessing = pd.read_csv(preprocessing_path)
df_sentiment_words = pd.read_csv(sentiment_words_path)

# Buat dictionary dari sentiment words untuk mempercepat pencocokan
sentiment_dict = df_sentiment_words.set_index('word')['weight'].to_dict()

# Fungsi untuk menghitung sentimen
def analyze_sentiment(tokenized_string):
    try:
        # Konversi string tokenisasi menjadi list
        tokens = ast.literal_eval(tokenized_string)
    except (ValueError, SyntaxError):
        # Jika parsing gagal, kembalikan sentimen netral (0)
        return 'neutral'
    
    # Hitung total weight dari tokens yang cocok di sentiment_dict
    sentiment_score = sum(sentiment_dict.get(token.lower(), 0) for token in tokens)
    
    # Tentukan sentimen berdasarkan skor
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

# Terapkan analisis sentimen ke kolom 'tokenisasi'
df_preprocessing['sentimen'] = df_preprocessing['tokenisasi'].apply(analyze_sentiment)

# Simpan hasil ke file baru
df_preprocessing.to_csv(output_path, index=False)

print(f"Analisis sentimen selesai! Data disimpan di {output_path}")
