import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
file_path = r"J:\Drive Saya\analisa sentimen git\percobaan 11\train_data.csv"
data = pd.read_csv(file_path)

# 2. Data Preparation
# Extract features and labels
X = data['full_text_tokenized'].apply(eval).apply(lambda tokens: ' '.join(tokens))  # Convert tokens back to a string
y = data['Value']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Text Vectorization (Check Transformation)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)  # Transform training data
X_test_vec = vectorizer.transform(X_test)        # Transform testing data

# 4. Train the Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)  # Train model on transformed data

# 5. Make Predictions and Evaluate
print("Shape of X_test_vec:", X_test_vec.shape)  # Debugging: Check the shape of the vectorized test data
print("Type of X_test_vec:", type(X_test_vec))  # Debugging: Ensure it's a sparse matrix or array

# Predict using vectorized test data
y_pred = model.predict(X_test_vec)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
