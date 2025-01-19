import pandas as pd

# Tentukan path file Excel dan path tujuan CSV
excel_path = r"J:\Drive Saya\analisa sentimen git\percobaan 4\Gojek.xlsx"
csv_path = r"J:\Drive Saya\analisa sentimen git\percobaan 4\gojek-train.csv"

# Baca file Excel dan simpan sebagai CSV
df = pd.read_excel(excel_path)
df.to_csv(csv_path, index=False)
