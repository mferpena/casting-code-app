pip install Flask

# Construir la imagen Docker
```sh
docker build -t html-to-css-app .
```
# Ejecutar el contenedor
```sh
docker run -p 5000:5000 html-to-css-app
```

# cUrl
```sh
curl --location 'http://localhost:5000/process_html' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'text=<div class="main-container">'
```