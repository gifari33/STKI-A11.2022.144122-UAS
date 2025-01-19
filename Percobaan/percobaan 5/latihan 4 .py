import pandas as pd
import re ; 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the training data
train_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\combined_train_data.csv'
train_data = pd.read_csv(train_file_path)

# Prepare features and labels
X_train = train_data['full_text']
y_train = train_data['Value']

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # Adjust max_features if needed
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train the Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluate on the training data for initial accuracy check
y_train_pred = model.predict(X_train_tfidf)
print("Training Accuracy:", accuracy_score(y_train, y_train_pred))
print(classification_report(y_train, y_train_pred))

# Load the validation data
validation_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 4\Gojek 1000 data.csv'
validation_data = pd.read_csv(validation_file_path)

# Clean and preprocess the 'content' column in validation data
def preprocess_text(text):
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

validation_data['content'] = validation_data['content'].apply(preprocess_text)
X_validation = validation_data['content']

# Transform validation data using the same TF-IDF vectorizer
X_validation_tfidf = vectorizer.transform(X_validation)

# Predict on validation data
y_validation_pred = model.predict(X_validation_tfidf)

# Add predictions to validation data and save
validation_data['Value'] = y_validation_pred
output_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\validation_results-4.csv'
validation_data.to_csv(output_file_path, index=False)

# Evaluate and print validation accuracy
print("Validation results saved to:", output_file_path)
