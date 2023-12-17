# Construir la imagen Docker

```sh
docker build -t casting-code-app .
```

# Ejecutar el contenedor

```sh
docker run -d -p 5000:5000 casting-code-app
```

# cUrl

## Casting HTML to CSS

```sh
curl --location 'http://localhost:5000/process_html' \
--header 'Content-Type: text/plain' \
--data '<div class="main-container">'
```

## Casting JSON to JAVA

```sh
curl --location 'http://127.0.0.1:5000/json_to_java' \
--header 'Content-Type: application/json' \
--data '{
    "totalResultsAvailable": "1827221",
    "totalResultsReturned": 2,
    "firstResultPosition": 1,
}
'
```
