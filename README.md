# Klasifikasi Transportasi Udara

Project Overview

Proyek ini bertujuan untuk mengklasifikasikan gambar transportasi udara ke dalam empat kategori utama:

Helikopter

Pesawat Kargo

Pesawat Komersial

Pesawat Jet Militer

Model deep learning berbasis Convolutional Neural Network (CNN dan VGG) digunakan untuk memproses citra input dan menghasilkan prediksi yang akurat. Dataset terdiri dari gambar dengan resolusi yang disesuaikan menjadi 128x128 piksel. Proyek ini diimplementasikan menggunakan framework Python dan dilengkapi dengan antarmuka pengguna berbasis Streamlit untuk mempermudah penggunaan.

datasetnya https://drive.google.com/file/d/1X9_gE-fbqjh5r1kLm_v3OOMSaHR5vGFr/view?usp=sharing

modelh5 dari cnn : https://drive.google.com/file/d/1PCbfPmT37OIBnvrL7b5trvFb-Bb9fxCK/view?usp=drive_link

modelh5 dari vgg : https://drive.google.com/file/d/1CwfpzdGdV2LEW9uLLxALiTaw0E2Ma0Mz/view?usp=drive_link

# Algoritma Classification

## 1. Convolutional Neural Network (CNN)

![Typical-CNN-Architecture-1024x374](https://github.com/user-attachments/assets/397d18d4-028a-4409-847f-6168b3a57a60)



CNN adalah arsitektur deep learning yang dirancang khusus untuk memproses data berbentuk grid, seperti gambar. CNN terdiri dari beberapa lapisan utama:

Convolutional Layer: Mengekstraksi fitur-fitur penting dari gambar seperti tepi, tekstur, dan pola.

Pooling Layer: Mengurangi dimensi fitur untuk mengurangi kompleksitas komputasi tanpa kehilangan informasi penting.

Fully Connected Layer: Menghubungkan fitur yang diekstraksi ke lapisan output untuk menghasilkan prediksi.
