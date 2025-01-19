import pandas as pd

# Load the dataset
file_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\validation_results-2.csv'
data = pd.read_csv(file_path)

# Separate positive and negative reviews
positive_reviews = data[data['Value'] == 'Positif']
negative_reviews = data[data['Value'] == 'Negatif']

# Display top 5 positive and negative reviews
print("Top 5 Positive Reviews:")
print(positive_reviews[['userName', 'content']].head(5), "\n")

print("Top 5 Negative Reviews:")
print(negative_reviews[['userName', 'content']].head(5), "\n")

# Analyze common themes in positive and negative feedback
from collections import Counter

# Combine all positive and negative feedback content
positive_text = ' '.join(positive_reviews['content'].astype(str))
negative_text = ' '.join(negative_reviews['content'].astype(str))

# Tokenize and count common words (basic text processing)
positive_words = Counter(positive_text.lower().split())
negative_words = Counter(negative_text.lower().split())

# Display common themes in positive and negative feedback
print("Most Common Positive Words:", positive_words.most_common(10))
print("Most Common Negative Words:", negative_words.most_common(10))
