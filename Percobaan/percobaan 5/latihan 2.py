import nltk
nltk.download('stopwords')
nltk.download('punkt')  # for tokenization
nltk.download('wordnet')  # for lemmatization

import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
df = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 5\gojek-train.csv')

# Cleaning function
def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove special characters, emojis, and numbers
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Remove punctuation and lowercase all text
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Remove stopwords
    stop_words = set(stopwords.words('indonesian'))
    tokens = word_tokenize(text)
    text = ' '.join([word for word in tokens if word not in stop_words])
    return text

# Apply the cleaning function to the 'full_text' column
df['clean_text'] = df['full_text'].apply(clean_text)

# Stemming and Lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

df['stemmed_text'] = df['clean_text'].apply(lambda x: ' '.join([stemmer.stem(word) for word in word_tokenize(x)]))
df['lemmatized_text'] = df['stemmed_text'].apply(lambda x: ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(x)]))

# TF-IDF Transformation with adjusted parameters
tfidf = TfidfVectorizer(max_features=1000, min_df=1)  # Adjusted max_features and min_df
tfidf_matrix = tfidf.fit_transform(df['lemmatized_text']).toarray()

# Save cleaned dataset
df['tfidf_vector'] = list(tfidf_matrix)
df.to_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 5\Gojek-train-clean2.csv', index=False)

print("Data cleaning and transformation completed successfully.")
