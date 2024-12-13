import streamlit as st
import qrcode
from PIL import Image
import io

def main():
    st.title("Generador de Códigos QR")
    st.write("Ingresa el texto o URL para generar el código QR.")

    # Entrada del usuario
    user_input = st.text_input("Texto o URL")

    # Tamaño opcional del código QR
    qr_size = st.slider("Tamaño del QR (píxeles):", 100, 500, 250)

    # Botón para generar QR
    if st.button("Generar QR"):
        if user_input:
            # Generar código QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(user_input)
            qr.make(fit=True)

            # Crear imagen del código QR
            img = qr.make_image(fill_color="black", back_color="white")
            # Se nota que toca tener cuidado con el atributo LANCZOS ya que anteriormente se usaba ANTIALIAS
            img = img.resize((qr_size, qr_size), Image.LANCZOS)

            # Mostrar imagen en Streamlit
            # antes se usaba parámetro use_column_width el cual quedo ha quedado obsoleto
            st.image(img, caption="Código QR generado", use_container_width=False)

            # Botón para descargar el código QR
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Descargar QR",
                data=byte_im,
                file_name="codigo_qr.png",
                mime="image/png",
            )
        else:
            st.warning("Por favor, ingresa un texto o URL para generar el código QR.")

if __name__ == "__main__":
    main()
