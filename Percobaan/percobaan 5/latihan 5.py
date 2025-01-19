import pandas as pd

# Load primary training data
primary_train_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\gojek-train-clean.csv'
primary_data = pd.read_csv(primary_train_path)

# Load additional sentiment lexicons
negative_path = r'J:\Drive Saya\analisa sentimen git\negative.tsv'
positive_path = r'J:\Drive Saya\analisa sentimen git\positive.tsv'

negative_data = pd.read_csv(negative_path, sep='\t')
positive_data = pd.read_csv(positive_path, sep='\t')

# Function to expand lexicon data based on weight
def expand_lexicon(data, label):
    expanded_texts = []
    for _, row in data.iterrows():
        word, weight = row['word'], abs(int(row['weight']))
        expanded_text = ' '.join([word] * weight)  # Repeat the word based on its weight
        expanded_texts.append((expanded_text, label))
    return pd.DataFrame(expanded_texts, columns=['full_text', 'Value'])

# Expand negative and positive lexicon data
negative_expanded = expand_lexicon(negative_data, 'Negatif')
positive_expanded = expand_lexicon(positive_data, 'Positif')

# Combine all datasets
combined_data = pd.concat([primary_data, negative_expanded, positive_expanded], ignore_index=True)

# Save combined dataset
combined_data_path = r'J:\Drive Saya\analisa sentimen git\percobaan 5\combined_train_data.csv'
combined_data.to_csv(combined_data_path, index=False)

print("Combined data saved to:", combined_data_path)
