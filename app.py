import csv
# import streamlit as st
import io
import json

SAMPLE_CSV = """idBerita;Headline;Content"""

# --- Fungsi untuk load data ---
def load_news(news_data):
    try:
        text = io.StringIO(news_data.getvalue().decode("utf-8"))
    except AttributeError:
        text = io.StringIO(news_data)
    reader = csv.DictReader(text, delimiter=",")
    rows = []
    for row in reader :
        rows.append({
            "idBerita" : (row.get("idBerita") or "").strip(),
            "Headline" : (row.get("Headline") or "").strip(),
            "Content" : (row.get("Content") or "").strip(),
        })
    return rows
rows = load_news(SAMPLE_CSV)
                
    # """Baca file news_data.csv ke list of dict"""
    # # TODO: buka file CSV (filename) dan baca dengan csv.DictReader
    # # kembalikan hasilnya dalam bentuk list
    # pass

SAMPLE_CSV2 = """idKomentar;idBerita;Komentar;Rating"""
def load_comments(comment_news):
    try :
        text = io.StringIO(comment_news.getvalue().decode("utf-8"))
    except AttributeError :
        text = io.StringIO(comment_news)
    reader = csv.DictReader(text, delimiter=",")
    rows = []
    for row in reader :
        rows.append({
            "idKomentar" : (row.get("idKomentar") or "").strip(),
            "idBerita" : (row.get("idBerita") or "").strip(),
            "Komentar" : (row.get("Komentar") or "").strip(),
            "Rating" : (row.get("Rating") or "").strip(),
        })
    return rows
rows = load_comments(SAMPLE_CSV2)

    # """Baca file comment_news.csv ke list of dict"""
    # # TODO: sama seperti load_news tapi untuk file komentar
    # pass

# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """
    # TODO: Buat dictionary untuk kumpulkan komentar per idBerita
    comments_per_news = {}
    for i in comments_list:
        comments_per_news["idBerita"] = st


    # TODO: isi comments_per_news dari comments_list
    # hint: per idBerita simpan ratings (list) dan count

    # TODO: Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        # TODO: cek apakah idb ada di comments_per_news,
        # hitung rata-rata rating dan jumlah komentar
        rata = 0  # ganti dengan hitungan
        jumlah = 0  # ganti dengan hitungan
        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    # --- Urutkan berdasarkan rating pakai fungsi biasa ---
    def ambil_rating(item):
        return item['Rata-rata Rating']

    # TODO: urutkan result berdasarkan ambil_rating reverse=True
    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    colom_config = {
        "idBerita" : st.colom_config>TextColum("idBerita"),
        ""
    }
    # TODO: baca data CSV
    news_data = []     # ganti dengan pemanggilan load_news
    comment_data = []  # ganti dengan pemanggilan load_comments

    # TODO: proses data
    hasil = []  # ganti dengan pemanggilan process_data

    # TODO: tampilkan tabel di Streamlit
    # hint: gunakan st.table(hasil)
    pass

if __name__ == '__main__':
    main()
