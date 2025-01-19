import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
import re
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Load the training data
train_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\combined_train_data.csv'
train_data = pd.read_csv(train_file_path)

# Prepare features and labels
X_train = train_data['full_text']
y_train = train_data['Value']

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Membagi data menjadi training dan testing (opsional)
X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train_vectorized, y_train, test_size=0.2, random_state=42)

# Melatih model (misalnya menggunakan Logistic Regression)
model = LogisticRegression()
model.fit(X_train_split, y_train_split)

# Prediksi pada data training
y_train_pred = model.predict(X_train_split)

# Menghitung akurasi pelatihan
training_accuracy = accuracy_score(y_train_split, y_train_pred)

# Cetak akurasi pelatihan
print(f"Akurasi Pelatihan: {training_accuracy:.2f}")

