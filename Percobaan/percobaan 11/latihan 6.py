import joblib

# Load model dan vectorizer
model = joblib.load(r"J:\Drive Saya\analisa sentimen git\sentiment_model2.pkl")
vectorizer = joblib.load(r"J:\Drive Saya\analisa sentimen git\tfidf_vectorizer2.pkl")

# Contoh prediksi
new_text = ["drivernya bagus"]
new_text_vectorized = vectorizer.transform(new_text)
prediction = model.predict(new_text_vectorized)

print(f"Hasil prediksi: {prediction[0]}")
