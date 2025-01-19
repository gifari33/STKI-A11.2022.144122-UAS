import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Download stopwords NLTK
nltk.download('stopwords')

# Menggunakan stopwords bahasa Indonesia
stop_words = stopwords.words('indonesian')

# File path dataset
train_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\combined_train_data.csv'

# Load dataset
train_data = pd.read_csv(train_file_path)

# Memisahkan fitur (X) dan label (y)
X_train = train_data['full_text']
y_train = train_data['Value']

# Fungsi preprocessing teks
def preprocess_text(text):
    text = re.sub(r'\W', ' ', str(text))  # Menghapus karakter non-alfabet
    text = text.lower()  # Mengubah teks menjadi lowercase
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)  # Menghapus kata dengan satu huruf
    text = re.sub(r'\s+', ' ', text)  # Menghapus spasi berlebih
    return text

# Preprocessing teks pada dataset
X_train = X_train.apply(preprocess_text)

# Vectorization menggunakan TF-IDF dengan bigram
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000, stop_words=stop_words)
X_train_vectorized = vectorizer.fit_transform(X_train)

# Membagi data menjadi training dan testing (80% training, 20% testing)
X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(
    X_train_vectorized, y_train, test_size=0.2, random_state=42
)

# Melatih model Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train_split, y_train_split)

# Prediksi pada data training
y_train_pred_logistic = logistic_model.predict(X_train_split)

# Menghitung akurasi pelatihan Logistic Regression
training_accuracy_logistic = accuracy_score(y_train_split, y_train_pred_logistic)
print(f"Akurasi Pelatihan (Logistic Regression): {training_accuracy_logistic:.2f}")

# Random Forest dengan GridSearchCV
rf = RandomForestClassifier()
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10],
}

# Mencari hyperparameter terbaik menggunakan Grid Search
grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train_vectorized, y_train)

# Mengambil model terbaik
best_rf = grid_search.best_estimator_

# Prediksi pada data training menggunakan Random Forest terbaik
y_train_pred_rf = best_rf.predict(X_train_vectorized)

# Menghitung akurasi pelatihan Random Forest
training_accuracy_rf = accuracy_score(y_train, y_train_pred_rf)
print(f"Akurasi Pelatihan setelah peningkatan (Random Forest): {training_accuracy_rf:.2f}")
