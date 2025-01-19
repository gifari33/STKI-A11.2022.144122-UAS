import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Path data
train_data_path = r'J:\Drive Saya\analisa sentimen git\percobaan 4\gojek-train.csv'
val_data_path = r'J:\Drive Saya\analisa sentimen git\percobaan 4\Gojek 1000 data.csv'
output_path = r'J:\Drive Saya\analisa sentimen git\percobaan 4\Gojek-hasil.csv'

print("Memuat data pelatihan...")
train_df = pd.read_csv(train_data_path)
print("Data pelatihan berhasil dimuat.")

print("Memuat data validasi...")
val_df = pd.read_csv(val_data_path)
print("Data validasi berhasil dimuat.")

# Persiapkan fitur (text) dan label (sentimen) untuk training
print("Memproses fitur dan label untuk data pelatihan...")
X_train = train_df['full_text']
y_train = train_df['Value']
print("Fitur dan label siap.")

# Vectorize teks menggunakan TF-IDF
print("Memulai proses vectorization dengan TF-IDF...")
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
print("Vectorization selesai.")

# Inisialisasi dan latih model Logistic Regression
print("Training model Logistic Regression...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)
print("Model training selesai.")

# Lakukan prediksi pada data validasi
print("Melakukan prediksi pada data validasi...")
X_val = val_df['content']  # Sesuaikan dengan kolom teks yang ada di data validasi
X_val_tfidf = tfidf_vectorizer.transform(X_val)
val_predictions = model.predict(X_val_tfidf)
print("Prediksi selesai.")

# Simpan hasil prediksi ke dalam file CSV
print(f"Menyimpan hasil prediksi ke {output_path}...")
val_df['Predicted_Value'] = val_predictions
val_df.to_csv(output_path, index=False)
print("Hasil prediksi berhasil disimpan.")
