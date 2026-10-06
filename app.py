from datetime import datetime
import os
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="¡La Gran Fiesta de Pocoyó para Emil!",
    page_icon="🎈",
    layout="centered",
)

# Estilos CSS con la temática de Pocoyó
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0099ff;
    }
    .titulo {
        color: #ffffff;
        text-align: center;
        font-family: 'Comic Sans MS', 'Arial', sans-serif;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .subtitulo {
        color: #ffeb3b;
        text-align: center;
        font-size: 1.3rem;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .tarjeta {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        text-align: center;
        border: 5px solid #ff5722;
    }
    .tarjeta h2, .tarjeta p, .tarjeta b, .tarjeta i {
        color: #333333 !important;
    }
    .caja-contador {
        background-color: #4caf50;
        color: white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        border: 3px solid #ffeb3b;
    }
    h3, label {
        color: #ffffff !important;
    }
    .btn-asistencia {
        display: block;
        width: 100%;
        background-color: #ff5722;
        color: white;
        padding: 15px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        text-decoration: none;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        margin-top: 10px;
    }
    .btn-asistencia:hover {
        background-color: #e64a19;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Encabezado principal
st.markdown(
    "<h1 class='titulo'>¡Acompaña a Emil en su Cumpleaños! 🎈</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='subtitulo'>¡Una aventura al estilo Pocoyó nos espera!</p>",
    unsafe_allow_html=True,
)

# Imagen de Pocoyó
col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
  if os.path.exists("pocoyo.png"):
    st.image("pocoyo.png", use_container_width=True)

st.write("")

# --- CÁLCULO DE LA CUENTA REGRESIVA ---
fecha_fiesta = datetime(2026, 12, 19, 15, 0, 0)
ahora = datetime.now()
diferencia = fecha_fiesta - ahora
dias_faltantes = diferencia.days
horas_faltantes = divmod(diferencia.seconds, 3600)[0]

if dias_faltantes > 0:
  texto_contador = (
      f"⏳ ¡Faltan {dias_faltantes} días y {horas_faltantes} horas para la"
      " gran fiesta! 🎉"
  )
elif dias_faltantes == 0:
  texto_contador = (
      "🔥 ¡Es HOY! ¡Es HOY! ¡La fiesta de Emil es el día de hoy! 🥳"
  )
else:
  texto_contador = (
      "❤️ ¡Gracias a todos los que acompañaron a Emil en su gran día!"
  )

st.markdown(
    f"<div class='caja-contador'>{texto_contador}</div>", unsafe_allow_html=True
)

# Tarjeta central con los detalles
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
  st.markdown(
      """
        <div class="tarjeta">
            <h2>🎉 ¡Diversión a lo grande! 🎉</h2>
            <p><b>Fecha:</b> Sábado, 19 de Diciembre de 2026</p>
            <p><b>Hora:</b> 3:00 PM</p>
            <p><i><b>Lugar:</b> ¡Próximamente por definir! 📍</i></p>
            <hr style="border: 0.5px dashed #0099ff; margin: 15px 0;">
            <p style="font-size: 0.95rem; color: #e91e63 !important;"><b>💡 Nota:</b> Te enviaremos la ubicación exacta y un recordatorio antes del evento.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.write("")

# Sección de Confirmación con el Enlace del Formulario
st.markdown(
    "<h3 style='text-align: center;'>📥 Confirma tu asistencia</h3>",
    unsafe_allow_html=True,
)

col_esp1, col_form, col_esp2 = st.columns([1, 2, 1])
with col_form:
  st.markdown(
      "<p style='text-align: center; color: #ffffff;'>Haz clic en el botón"
      " para registrar tu nombre:</p>",
      unsafe_allow_html=True,
  )

  # PEGA AQUÍ EL ENLACE DE TU GOOGLE FORM ENTRE LAS COMILLAS
  enlace_formulario = "PEGA_AQUÍ_EL_ENLACE_DE_TU_GOOGLE_FORM"

  st.markdown(
      f"<a href='{enlace_formulario}' target='_blank'"
      " class='btn-asistencia'>¡Confirmar mi asistencia! 🚀</a>",
      unsafe_allow_html=True,
  )

# Pie de página