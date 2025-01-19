import pandas as pd

# Membaca dataset utama yang ingin dianalisis
data_df    = pd.read_csv(r"J:\Drive Saya\analisa sentimen git\gojek.csv")


# Membaca data sentimen positif dan negatif
negative_df = pd.read_csv(r"J:\Drive Saya\analisa sentimen git\negative.tsv", sep="\t")
positive_df = pd.read_csv(r"J:\Drive Saya\analisa sentimen git\positive.tsv", sep="\t")

# Menggunakan kolom 'word' dari data negatif dan positif untuk analisis
negative_set = set(negative_df["word"])
positive_set = set(positive_df["word"])

# Memisahkan data menjadi positif dan negatif berdasarkan analisis
positive_content = data_df[
    data_df["content"].apply(lambda x: any(word in x for word in positive_set))
]
negative_content = data_df[
    data_df["content"].apply(lambda x: any(word in x for word in negative_set))
]

# Menyimpan hasil analisis ke dalam file CSV baru
positive_content.to_csv("gojek-positif.csv", index=False)
negative_content.to_csv("gojek-negative.csv", index=False)

print("Data positif telah disimpan sebagai 'gojek-positif.csv'")
print("Data negatif telah disimpan sebagai 'gojek-negative.csv'")
