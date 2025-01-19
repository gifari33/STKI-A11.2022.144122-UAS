import pandas as pd
import re

# Load the data
file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\gojek-train.csv'
data = pd.read_csv(file_path)

# Remove irrelevant columns, keeping only 'full_text' and 'Value'
data = data[['full_text', 'Value']]

# Function to clean text data
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove special characters, emojis, and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply the cleaning function to the 'full_text' column
data['full_text'] = data['full_text'].apply(clean_text)

# Save the cleaned data
cleaned_file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\gojek-train-clean.csv'
data.to_csv(cleaned_file_path, index=False)

print("Data cleaning completed and saved to:", cleaned_file_path)
