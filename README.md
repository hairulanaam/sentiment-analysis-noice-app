# Sentiment Analysis: Noice App Reviews

Proyek analisis sentimen terhadap review aplikasi **Noice** di Google Play Store menggunakan machine learning untuk mengklasifikasikan sentimen review menjadi kategori positif, negatif, dan netral.

## Overview

Proyek ini mengembangkan sistem klasifikasi sentimen otomatis untuk menganalisis ulasan pengguna aplikasi Noice. Dengan menggunakan teknik natural language processing (NLP) dan machine learning, sistem ini dapat mengklasifikasikan sentimen review menjadi tiga kategori:
- **Positif** 
- **Netral** 
- **Negatif**

## Dataset

- **Sumber**: Google Play Store (Aplikasi Noice)
- **Jumlah Data**: ~10,000+ review
- **Bahasa**: Indonesian
- **Format**: CSV (`noice_app_reviews.csv`)

### Distribusi Sentimen
- Positif: Review dengan rating 4-5
- Netral: Review dengan rating 3
- Negatif: Review dengan rating 1-2

## Metodologi

### 1. Data Scraping
Menggunakan library `google-play-scraper` untuk mengumpulkan review langsung dari Google Play Store.

### 2. Text Preprocessing
Tahapan pembersihan teks meliputi:
- **Cleaning**: Menghapus mention (@), hashtag (#), RT, link URL, angka, dan karakter spesial
- **Casefolding**: Mengubah semua karakter menjadi huruf kecil
- **Slang Correction**: Memperbaiki kata-kata slang informal menjadi bentuk standar
- **Tokenization**: Memecah teks menjadi token (kata-kata)
- **Stopword Removal**: Menghapus kata-kata umum menggunakan Sastrawi
- **Stemming**: Mengurangi kata ke bentuk dasarnya menggunakan Sastrawi

### 3. Feature Extraction
Menggunakan **TF-IDF (Term Frequency-Inverse Document Frequency)** dengan parameter:
- `max_features`: 5000
- `min_df`: 3
- `max_df`: 0.8
- `ngram_range`: (1, 2)

### 4. Data Splitting
Pembagian data:
- **Training Set**: 80%
- **Test Set**: 20%

## Model Machine Learning

Proyek ini membandingkan 5 model machine learning:

| Model | Deskripsi |
|-------|-----------|
| **Naive Bayes** | Probabilistic classifier berbasis Bayes theorem |
| **Logistic Regression** | Linear classifier dengan class balancing |
| **Random Forest** | Ensemble method menggunakan multiple decision trees |
| **Decision Tree** | Tree-based classifier untuk pattern recognition |
| **Support Vector Machine (SVM)** | Kernel-based classifier untuk non-linear separation |
