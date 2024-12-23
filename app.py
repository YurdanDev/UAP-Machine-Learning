import streamlit as st
from tensorflow.keras.models import load_model  # type:ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array  # type:ignore
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk memuat dan memproses gambar
def process_image(image_path, target_size=(128, 128)):
    img = load_img(image_path, target_size=target_size)  # Ubah ukuran gambar
    img_array = img_to_array(img)  # Konversi ke array
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
    img_array = img_array / 255.0  # Normalisasi
    return img_array

# Fungsi untuk memprediksi label
def predict_image(model, image_array, class_labels):
    prediction = model.predict(image_array)
    predicted_label = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return predicted_label, confidence

# Fungsi untuk menampilkan gambar dengan prediksi
def display_image_with_prediction(image, label, confidence):
    plt.imshow(image)
    plt.title(f"Predicted: {label} ({confidence:.2f}%)")
    plt.axis('off')
    st.pyplot(plt)

# Judul aplikasi
st.title("Klasifikasi Transportasi Udara")

# Deskripsi
st.write("""
Aplikasi ini menggunakan model deep learning untuk mengklasifikasikan gambar transportasi udara ke dalam kategori:
- **Helikopter**
- **Pesawat Kargo**
- **Pesawat Komersial**
- **Pesawat Jet Militer**
""")

# Muat model yang sudah dilatih
model_path = "model_klasifikasi_transportasi_cnn.h5" 

try:
    model = load_model(model_path)  # Muat model
except Exception as e:
    st.error(f"Model tidak dapat dimuat: {e}")

# Kelas/label dataset
class_labels = ['Helikopter', 'Pesawat Kargo', 'Pesawat Komersial', 'Pesawat Jet Militer'] 

# Widget untuk mengunggah gambar
uploaded_file = st.file_uploader("Unggah gambar transportasi udara", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    if 'model' in locals():  # Pastikan model sudah dimuat
        # Simpan gambar yang diunggah
        with open("uploaded_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Muat dan proses gambar
        st.image("uploaded_image.jpg", caption="Gambar yang diunggah", use_column_width=True)
        image_array = process_image("uploaded_image.jpg")

        # Prediksi
        predicted_label, confidence = predict_image(model, image_array, class_labels)

        # Tampilkan hasil prediksi
        st.write("### Prediksi:")
        st.write(f"**Kategori:** {predicted_label}")
        st.write(f"**Kepercayaan:** {confidence:.2f}%")
    else:
        st.error("Model belum dimuat, harap periksa kembali file model Anda.")
