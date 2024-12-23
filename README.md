# Klasifikasi Transportasi Udara
![image](https://github.com/user-attachments/assets/4d0275ea-c857-4bbc-b702-52e2f46f84ff)


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

CNN digunakan dalam proyek ini karena kemampuannya yang tinggi dalam mengenali pola visual pada gambar dengan presisi yang baik.


## 2. VGG (Visual Geometry Group)

<img width="611" alt="VGG16-CNN-Architecture" src="https://github.com/user-attachments/assets/66dd108e-30b2-4e76-a453-55e966665b4b" />



VGG adalah varian CNN yang menggunakan lapisan konvolusi berukuran kecil (3x3) dengan jumlah filter yang meningkat secara bertahap. VGG sangat populer untuk klasifikasi gambar karena arsitekturnya yang sederhana dan efektif. Karakteristik utama VGG meliputi:

Kedalaman jaringan yang lebih dalam dibandingkan CNN standar, yang meningkatkan kemampuan jaringan dalam mengenali fitur yang kompleks.

Struktur lapisan yang seragam, memudahkan untuk diperluas dan diadaptasi.

Dalam proyek ini, VGG dipertimbangkan sebagai baseline model karena kemampuannya yang sudah terbukti untuk tugas klasifikasi gambar dengan dataset besar maupun kecil.

## Preprocessing

Preprocessing data dilakukan untuk memastikan gambar berada dalam format yang dapat diproses oleh model deep learning. Langkah-langkah preprocessing meliputi:

Resize: Semua gambar diubah ukurannya menjadi 128x128 piksel untuk memastikan dimensi input seragam.

Normalisasi: Nilai piksel gambar dinormalisasi ke rentang [0, 1] dengan membagi nilai piksel dengan 255.

Data Augmentation: Untuk memperkaya dataset, teknik augmentasi seperti rotasi, flipping, dan zooming diterapkan pada gambar saat pelatihan.

### Exploratory Data Analysis (EDA)

![image](https://github.com/user-attachments/assets/b28afd4a-ff77-4366-bb33-c199abb0ed1d)

![image](https://github.com/user-attachments/assets/d81f44a6-659d-4241-987c-405424baedbe)

![image](https://github.com/user-attachments/assets/596474ca-28a6-4058-80da-c12f00ce4f38)

![image](https://github.com/user-attachments/assets/6a560bb4-7fc4-49d8-8767-03b61babc3fd)

![image](https://github.com/user-attachments/assets/33794416-d76b-424e-a425-f23eadba7aaa)


## Modelling

## Arsitektur Model

CNN

Input layer menerima gambar dengan ukuran 128x128x3.

Beberapa lapisan konvolusi dengan kernel 3x3, diikuti oleh lapisan pooling untuk ekstraksi fitur.

Fully connected layer untuk klasifikasi ke 4 kategori output.

Aktivasi softmax pada output layer untuk menghasilkan probabilitas pada setiap kelas.

![image](https://github.com/user-attachments/assets/88305eab-8920-489f-857f-734b8d1aa4fa)

VGG

VGG

Pretrained model VGG-16 digunakan sebagai dasar (transfer learning) dengan lapisan fully connected yang dimodifikasi untuk klasifikasi 4 kelas.

Lapisan awal VGG-16 tetap, sedangkan lapisan akhir di-retrain menggunakan dataset ini.

![image](https://github.com/user-attachments/assets/2e31bab3-e056-4a64-bd2e-fe3d5960c23d)


## Evaluasi

CNN

![image](https://github.com/user-attachments/assets/2ad23737-3503-4780-b460-d21e1fc1d16a)

![image](https://github.com/user-attachments/assets/efe5319f-465e-4535-bbf7-03ff9706b807)

![image](https://github.com/user-attachments/assets/d8b926a0-2cf3-4da1-802e-a915dcf3ec98)


VGG

![image](https://github.com/user-attachments/assets/bb194b42-829f-48b0-85ea-f606b69a64f3)

![image](https://github.com/user-attachments/assets/b2fb1f57-ab72-4293-8b8a-2748ab203f29)

![image](https://github.com/user-attachments/assets/b0a047d4-7b69-4313-9132-8227bbb78142)



## Antarmuka Pengguna Deployment

<img width="782" alt="1" src="https://github.com/user-attachments/assets/f5e7c083-3125-4c50-96a7-cf7b19d9d423" />

hasil dari model.h5 cnn

![image](https://github.com/user-attachments/assets/d7206f68-a721-47db-906a-5e00f456dec4)

hasil dari model.h5 vgg

![image](https://github.com/user-attachments/assets/0690c341-6f76-4a1e-b989-11f373a4acfa)


cara runnningnya di windows dengan menginstall

python 3.11.0

powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"

pip install --upgrade pip

pip install tensorflow

pip install streamlit

pip install scikit-learb

pip install joblib

pip install matplotlib

setelah itu

streamlit run app.py








