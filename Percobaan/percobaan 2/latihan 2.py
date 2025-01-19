import pandas as pd

# Load positive and negative sentiment data
positive_data = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 2\gojek-clear-positif.csv')
negative_data = pd.read_csv(r'J:\Drive Saya\analisa sentimen git\percobaan 2\gojek-clear-negatif.csv')

# Function to search for sentences containing a specific word
def find_sentences_with_word(data, word, num_sentences=5):
    sentences = [content for content in data['content'] if pd.notnull(content) and word in content.lower()]
    return sentences[:num_sentences]

# # Search for sentences with "bagus" in positive data
# print("Sentences in positive data containing 'bagus':")
# for sentence in find_sentences_with_word(positive_data, 'bagus'):
#     print(f"- {sentence}")

# # Search for sentences with "aplikasi" in positive data
# print("\nSentences in positive data containing 'aplikasi':")
# for sentence in find_sentences_with_word(positive_data, 'aplikasi'):
#     print(f"- {sentence}")

# Search for sentences with "bagus" in negative data
print("\nSentences in negative data containing 'lama':")
for sentence in find_sentences_with_word(negative_data, 'lama'):
    print(f"- {sentence}")

# Search for sentences with "aplikasi" in negative data
print("\nSentences in negative data containing 'gojek':")
for sentence in find_sentences_with_word(negative_data, 'gojek'):
    print(f"- {sentence}")
