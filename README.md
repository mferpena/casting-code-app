pip install Flask

# Construir la imagen Docker
```sh
docker build -t html-to-css-app .
```
# Ejecutar el contenedor
```sh
docker run -d -p 5000:5000 html-to-css-app
```

# cUrl
```sh
curl --location 'http://localhost:5000/process_html' \
--header 'Content-Type: text/plain' \
--data '<div class="main-container">'
```