import pandas as pd
from collections import Counter
import re

# Load the positive and negative sentiment data files
positive_data = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 2\gojek-clear-positif.csv')
negative_data = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 2\gojek-clear-negatif.csv')

# Function to count word frequency
def get_top_words(data, num_words=5):
    # Combine all content into a single string for analysis
    all_text = ' '.join(str(content) for content in data['content'] if pd.notnull(content))
    
    # Tokenize and clean words (remove special characters and convert to lowercase)
    words = re.findall(r'\b\w+\b', all_text.lower())
    
    # Count word frequency
    word_counts = Counter(words)
    
    # Return the most common words
    return word_counts.most_common(num_words)

# Get and display the top 5 most common words for positive data
print("Top 5 most common words in positive data:")
for word, count in get_top_words(positive_data):
    print(f"{word}: {count}")

# Get and display the top 5 most common words for negative data
print("\nTop 5 most common words in negative data:")
for word, count in get_top_words(negative_data):
    print(f"{word}: {count}")
