# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY html_to_css.py .
COPY json_to_yml.py .
COPY json_to_java.py .
COPY main.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Define el comando por defecto para ejecutar tu aplicación
CMD ["python", "main.py"]
