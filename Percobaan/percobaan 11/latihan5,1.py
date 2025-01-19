from sklearn.naive_bayes import MultinomialNB, BernoulliNB

import pandas as pd
import ast
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
import nltk

# Download NLTK resources
nltk.download('stopwords')

# 1. Load Dataset
path = r"J:\Drive Saya\analisa sentimen git\percobaan 11\train_data.csv"
data = pd.read_csv(path)

# Eksplorasi Data
print("Jumlah Data: ", len(data))
print("Contoh Data:\n", data.head())
print("Distribusi Label:\n", data['Value'].value_counts())

# Mengonversi kolom `full_text_tokenized` dari string ke list
data['full_text_tokenized'] = data['full_text_tokenized'].apply(ast.literal_eval)

# Menggabungkan token menjadi satu teks untuk preprocessing lebih lanjut
data['processed_text'] = data['full_text_tokenized'].apply(lambda tokens: " ".join(tokens))

# 2. Preprocessing
# Pembersihan Data
def clean_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'\s+', ' ', text)  # Menghapus spasi berlebih
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Hapus karakter khusus
    return text

data['processed_text'] = data['processed_text'].apply(clean_text)

# Tokenisasi, Stopwords Removal, Stemming
stop_words = set(stopwords.words('indonesian'))  # Stopwords dalam bahasa Indonesia
stemmer = PorterStemmer()

def preprocess_text(text):
    tokens = text.split()  # Tokenisasi
    tokens = [word for word in tokens if word not in stop_words]  # Hapus stopwords
    tokens = [stemmer.stem(word) for word in tokens]  # Stemming
    return " ".join(tokens)

data['processed_text'] = data['processed_text'].apply(preprocess_text)

# Distribusi Data setelah preprocessing
print("\nContoh Data Setelah Preprocessing:\n", data[['processed_text', 'Value']].head())

# 3. Feature Extraction
X = data['processed_text']  # Menggunakan teks yang telah diproses
y = data['Value']  # Label (Negatif/Positif)

# Mengonversi teks ke fitur numerik
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Membagi dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)


# 4. Train Model
# Pilih tipe Naive Bayes
# Gunakan MultinomialNB untuk data teks
# BernoulliNB untuk fitur biner
# Coba dengan parameter yang disesuaikan

# Multinomial Naive Bayes
model = MultinomialNB(alpha=1.0)  # Anda dapat mengubah nilai alpha untuk tuning
# Bernoulli Naive Bayes (gunakan jika data teks diubah menjadi representasi biner, contoh: CountVectorizer(binary=True))
# model = BernoulliNB(alpha=1.0)

model.fit(X_train, y_train)

# 5. Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\nAkurasi Model: {accuracy * 100:.2f}%")
print("\nLaporan Klasifikasi:\n", report)
