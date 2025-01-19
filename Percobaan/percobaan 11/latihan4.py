import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load Dataset
path = r"J:\Drive Saya\analisa sentimen git\percobaan 11\train_data.csv"
data = pd.read_csv(path)

# 2. Preprocessing
# Menangkap teks dan label
X = data['full_text']  # Data teks
y = data['Value']  # Label (Negatif/Positif)

# Mengubah teks menjadi representasi numerik
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Membagi dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 3. Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# 4. Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Akurasi Model: {accuracy * 100:.2f}%")
print("\nLaporan Klasifikasi:\n", report)

# 5. Save Model
model_path = "sentiment_model.pkl"
vectorizer_path = "tfidf_vectorizer.pkl"

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)

print(f"Model disimpan di: {model_path}")
print(f"Vectorizer disimpan di: {vectorizer_path}")
