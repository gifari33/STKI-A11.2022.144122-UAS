import pandas as pd
import re
from deep_translator import GoogleTranslator

# Load data dari file CSV
file_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaan 14\cleaned_data.csv'
df = pd.read_csv(file_path)

# 1. Hapus Data Duplikat
initial_count = len(df)
df.drop_duplicates(subset=['userName', 'content', 'at'], keep='first', inplace=True)
final_count = len(df)
duplicates_removed = initial_count - final_count

print(f"Jumlah data awal: {initial_count}")
print(f"Jumlah data setelah menghapus duplikat: {final_count}")
print(f"Jumlah data duplikat yang dihapus: {duplicates_removed}")

# Tampilkan data duplikat yang dihapus (opsional)
# duplicated_data = df[df.duplicated(subset=['userName', 'content', 'at'], keep=False)]
# print("\nData Duplikat yang Dihapus:")
# print(duplicated_data)

# **Tambahkan baris ini untuk menghapus baris dengan nilai kosong di kolom 'content'**
df.dropna(subset=['content'], inplace=True)

# 2. Koreksi Ejaan dan Tata Bahasa serta Hapus Karakter Khusus dan Emoji
def clean_text(text):
    # Hapus karakter khusus dan emoji
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text) # Menghapus karakter non-ASCII
    return text.lower()

def correct_spelling(text):
    try:
        translator = GoogleTranslator(source='auto', target='id')
        corrected_text = translator.translate(text)
        return corrected_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text  # Kembalikan teks asli jika terjadi error

df['koreksi_ejaan'] = df['content'].apply(clean_text)
df['koreksi_ejaan'] = df['koreksi_ejaan'].apply(correct_spelling)

print("\nContoh data setelah koreksi ejaan dan penghapusan karakter khusus:")
print(df[['content', 'koreksi_ejaan']].head())

# 3. Filter Data yang Tidak Relevan
# Cara mengidentifikasi data yang tidak relevan sangat bergantung pada konteks.
# Beberapa pendekatan:

# Pendekatan 1: Berdasarkan Panjang Teks
# Komentar yang terlalu pendek mungkin tidak relevan atau tidak informatif.
df_filtered = df[df['koreksi_ejaan'].apply(lambda x: len(x.split()) > 2)]
print(f"\nJumlah data setelah filter berdasarkan panjang teks: {len(df_filtered)}")

# Pendekatan 2: Berdasarkan Kata Kunci
# Anda bisa membuat daftar kata kunci yang sering muncul di komentar yang tidak relevan,
# misalnya promosi atau ajakan.
irrelevant_keywords = ['promo', 'diskon', 'kode referral', 'bergabung', 'gratis']
df_filtered = df_filtered[~df_filtered['koreksi_ejaan'].str.contains('|'.join(irrelevant_keywords), case=False)]
print(f"Jumlah data setelah filter berdasarkan kata kunci: {len(df_filtered)}")

# Pendekatan 3: Kombinasi dan Analisis Manual
# Cara terbaik adalah dengan melihat sampel data Anda secara manual
# dan mengidentifikasi pola atau ciri-ciri komentar yang tidak relevan.
# Anda mungkin perlu melakukan iterasi dan memperbaiki kriteria filter Anda.

# Contoh cara melihat data dan mengidentifikasi pola:
# pd.set_option('display.max_colwidth', None)
# print("\nContoh beberapa data untuk dianalisis manual:")
# print(df['koreksi_ejaan'].sample(10))

# Kesimpulan tentang Filter Data Tidak Relevan:
# Tidak ada cara otomatis yang sempurna untuk memfilter data yang tidak relevan.
# Ini seringkali memerlukan pemahaman konteks dan mungkin melibatkan:
# 1. Pemeriksaan manual sebagian data untuk mengidentifikasi pola.
# 2. Pembuatan daftar kata kunci atau pola kalimat yang tidak relevan.
# 3. Penggunaan model klasifikasi (setelah data dilabeli) untuk memprediksi
#    apakah suatu komentar relevan atau tidak.

# 4. Pelabelan Data
# Contoh pelabelan manual (Anda perlu melakukan ini berdasarkan pemahaman Anda
# tentang masalah-masalah umum di aplikasi Gojek)

def label_comment(text):
    text = text.lower()
    if 'terlambat' in text or 'lama' in text and 'datang' in text:
        return 'Keterlambatan Driver'
    elif 'gps' in text or 'peta' in text or 'lokasi' in text:
        return 'Masalah GPS/Peta'
    elif 'aplikasi' in text and ('keluar sendiri' in text or 'error' in text or 'tidak bisa dibuka' in text):
        return 'Kesalahan Aplikasi'
    elif 'gopay' in text and 'blokir' in text:
        return 'Masalah Gopay'
    elif 'pin' in text and 'salah' in text:
        return 'Masalah PIN'
    # ... tambahkan label lain sesuai kebutuhan ...
    else:
        return 'Lain-lain'  # Kategori umum jika tidak cocok dengan label spesifik

df_filtered['label'] = df_filtered['koreksi_ejaan'].apply(label_comment)

print("\nContoh data setelah pelabelan:")
print(df_filtered[['koreksi_ejaan', 'label']].head(10))

# Simpan data yang sudah dipersiapkan ke file CSV baru
output_file_path = r'C:\Users\ghiff\Documents\kuliah\Analisa_Sentimen_Gojek\percobaa15\Persiapan Data.csv'
df_filtered.to_csv(output_file_path, index=False, encoding='utf-8')

print(f"\nData yang sudah dipersiapkan berhasil disimpan ke: {output_file_path}")

# Data yang sudah dipersiapkan (df_filtered) siap untuk langkah selanjutnya