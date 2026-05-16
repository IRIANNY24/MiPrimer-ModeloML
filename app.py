import streamlit as st
import random

st.title("Generador de Ecuaciones de Primer Grado")

# Generar valores aleatorios
x = random.randint(1, 10)
a = random.randint(1, 10)
b = random.randint(1, 20)

# Crear ecuación
resultado = a * x + b

st.subheader("Resuelve la siguiente ecuación:")
st.write(f"{a}x + {b} = {resultado}")

# Entrada del usuario
respuesta = st.number_input("Ingresa el valor de x:", step=1)

# Botón para verificar
if st.button("Verificar"):
    if respuesta == x:
        st.success("Correcto")
    else:
        st.error(f"Incorrecto. La respuesta correcta era x = {x}")
