import pandas as pd
import re

# Load main data
data = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 3\gojek-clear-data.csv')

# Load positive and negative lexicons
positive_words = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\positive.tsv', sep='\t')
negative_words = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\negative.tsv', sep='\t')

# Create dictionaries for quick lookup of word weights
positive_dict = dict(zip(positive_words['word'], positive_words['weight']))
negative_dict = dict(zip(negative_words['word'], negative_words['weight']))

# Define stopwords to remove
stopwords = set(["nya", "saja", "aja", "yang", "di", "ke", "dari", "untuk", "dengan", "pada", "dan", "ini"])

# Function to calculate sentiment weight for each entry
def calculate_sentiment(content):
    words = re.findall(r'\b\w+\b', content.lower())  # Tokenize and clean text
    words = [word for word in words if word not in stopwords]  # Remove stopwords

    # Calculate sentiment weight based on lexicon
    positive_weight = sum(positive_dict.get(word, 0) for word in words)
    negative_weight = sum(negative_dict.get(word, 0) for word in words)
    
    # Debugging print statements
    print(f"Content: {content}")
    print(f"Words: {words}")
    print(f"Positive Weight: {positive_weight}, Negative Weight: {negative_weight}")

    # Determine sentiment based on the weights
    if positive_weight > negative_weight:
        return "positive", positive_weight - negative_weight
    elif negative_weight > positive_weight:
        return "negative", negative_weight - positive_weight
    else:
        return "neutral", 0

# Apply sentiment calculation to each row in the data
data['sentiment'], data['weight'] = zip(*data['content'].apply(lambda x: calculate_sentiment(str(x))))

# Filter positive and negative data
positive_data = data[data['sentiment'] == 'positive'].drop(columns='sentiment')
negative_data = data[data['sentiment'] == 'negative'].drop(columns='sentiment')

# Save the data to separate CSV files if not empty
if not positive_data.empty:
    positive_data.to_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 3\gojek-clear-positif.csv', index=False)

if not negative_data.empty:
    negative_data.to_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 3\gojek-clear-negatif.csv', index=False)
else:
    print("Warning: No negative data found.")

print("Sentiment-separated data has been processed and saved.")
