# App en Streamlit: Ecuaciones de Primer Grado

Copia este código en un archivo llamado:

```python
app.py
```

Luego súbelo a tu repositorio de GitHub.

---

## Código

```python
import streamlit as st
import random

st.title("Generador de Ecuaciones de Primer Grado")

# Generar números aleatorios
x = random.randint(1, 10)
a = random.randint(1, 10)
b = random.randint(1, 20)

# Crear ecuación
resultado = a * x + b

st.subheader("Resuelve la siguiente ecuación:")
st.write(f"{a}x + {b} = {resultado}")

# Respuesta del usuario
respuesta = st.number_input("Ingresa el valor de x:", step=1)

# Verificar respuesta
if st.button("Verificar"):
    if respuesta == x:
        st.success("¡Correcto! 🎉")
    else:
        st.error(f"Incorrecto ❌. La respuesta correcta era x = {x}")
```

---

## Cómo ejecutarlo en Streamlit

### 1. Instalar Streamlit

```bash
pip install streamlit
```

### 2. Ejecutar la app

```bash
streamlit run app.py
```

---

## Cómo subirlo a GitHub

1. Entra a tu repositorio.
2. Haz clic en:

   * Add file
   * Upload files
3. Sube el archivo `app.py`.
4. Commit changes.

---

## Cómo desplegar en Streamlit Cloud

1. Entra a Streamlit Cloud.
2. Deploy app.
3. Selecciona tu repositorio.
4. Main file path:

```python
app.py
```

5. Deploy.

Y listo 🎉



