# 🔐 Password Strength Checker with Machine Learning

## 📘 Deskripsi Proyek
Proyek ini bertujuan untuk **membangun sistem yang mampu menilai kekuatan password** berdasarkan pola data menggunakan metode **Machine Learning**.  
Sistem dikembangkan dengan **Python (Flask)** di sisi backend, serta **HTML, CSS, dan JavaScript** untuk frontend interaktif.  

Pengguna dapat memasukkan password pada antarmuka web, dan sistem akan mengklasifikasikan kekuatan password ke dalam tiga kategori:
- **Weak (Lemah)**
- **Medium (Sedang)**
- **Strong (Kuat)**

---

## ⚙️ Teknologi yang Digunakan
- **Backend:** Python 3, Flask, Flask-CORS, scikit-learn, Pandas, NumPy  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Machine Learning Models:**
  - Decision Tree  
  - Logistic Regression  
  - Naive Bayes (BernoulliNB)  
  - Random Forest  

---

## 🧠 Konsep Machine Learning
Sistem ini menerapkan **supervised learning**, di mana model dilatih menggunakan dataset password yang sudah memiliki label kekuatan (Weak, Medium, Strong).  
Dataset diubah menjadi representasi numerik menggunakan **TF-IDF Vectorizer**, kemudian digunakan untuk melatih empat algoritma Machine Learning.  

Metrik evaluasi yang digunakan:
- **Accuracy** – proporsi prediksi benar terhadap total data  
- **Precision** – ketepatan model dalam mengenali kelas tertentu  
- **Recall** – kemampuan model menemukan seluruh data dari tiap kelas  
- **F1-Score** – rata-rata harmonis antara Precision dan Recall  

Hasil terbaik diperoleh oleh **Random Forest Classifier** dengan akurasi **83.2%**.

---

## 🧾 Dataset
Dataset yang digunakan berasal dari **[Kaggle – Password Strength Classification Dataset](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier)**.  

Dataset ini terdiri dari dua kolom utama:
- `password` — teks sandi dalam bentuk string  
- `strength` — label numerik kekuatan password (0 = Weak, 1 = Medium, 2 = Strong)  

Dalam proyek ini, label disesuaikan berdasarkan panjang karakter password agar lebih sesuai dengan kasus umum:
- **< 8 karakter** → Weak  
- **8–15 karakter** → Medium  
- **> 15 karakter** → Strong  

Dataset asli disimpan dalam file:
Book3_converted (1).xlsx

yaml
Copy code

---

## 🧩 Struktur Folder
```bash
Password-Strength-Checker/
│
├── app.py                     # Backend Flask API
├── index.html                 # Frontend web utama
├── password_final.ipynb       # Proses training dan evaluasi model
├── Book3_converted (1).xlsx   # Dataset password
├── static/
└── README.md                  # Dokumentasi proyek
```

## 🚀 Cara Menjalankan Proyek di Lokal
1. Instalasi Dependensi
Pastikan Python 3 sudah terpasang, lalu jalankan perintah berikut di terminal:

bash
Copy code
pip install flask flask-cors pandas numpy scikit-learn
2. Menjalankan Backend Flask
bash
Copy code
python app.py
Server akan berjalan di alamat:
http://127.0.0.1:5000/

3. Menjalankan Frontend
Buka file index.html di browser.
Masukkan password pada kolom input, lalu tekan tombol Check untuk melihat hasil klasifikasi kekuatan password.

---

## ☁️ Menjalankan di Google Colab
Jika ingin menjalankan proyek di Google Colab:
- Upload file password_final.ipynb dan dataset.xlsx ke Colab.
- Instal pustaka berikut:
  - python
  - Copy code
  - !pip install flask flask-cors pandas numpy scikit-learn
  - Jalankan semua sel hingga model selesai dilatih.

(Opsional) Gunakan ngrok atau localtunnel untuk mengakses Flask API dari browser.

---

## 📊 Hasil Evaluasi Model
| Model                | Accuracy  | Precision  | Recall  | F1-Score  |
|----------------------|-----------|------------|---------|-----------|
| Random Forest        | 0.824     | 0.812      | 0.824   | 0.795     |
| Logistic Regression  | 0.816     | 0.807      | 0.816   | 0.774     |
| Decision Tree        | 0.776     | 0.765      | 0.776   | 0.769     |
| Naive Bayes          | 0.816     | 0.698      | 0.816   | 0.751     |


Model Random Forest memberikan hasil paling stabil dan akurat, sehingga dipilih sebagai model utama.

---

## 📸 Tampilan Antarmuka Website
Tampilan utama aplikasi menampilkan input password, indikator kekuatan secara real-time, serta hasil prediksi dari keempat algoritma beserta metrik performanya.

![Tampilan Aplikasi](PasswordCheckUI.png)

---

## 🌐 Fitur Utama
- ✅ Menampilkan indikator kekuatan password secara real-time.
- ✅ Menggunakan empat algoritma Machine Learning untuk perbandingan hasil.
- ✅ Menampilkan tabel metrik performa dari setiap model.
- ✅ Antarmuka web sederhana dan responsif.

---

## 👨‍💻 Pengembang
Proyek ini dikembangkan sebagai bagian dari mata kuliah Machine Learning,
dengan fokus pada penerapan pembelajaran mesin dalam bidang keamanan siber (Cyber Security).

---

## 🧾 Lisensi
Proyek ini bersifat open-source untuk keperluan pembelajaran dan penelitian.
Anda dapat memodifikasi, menggunakan, dan mengembangkan proyek ini secara bebas untuk tujuan edukatif.
