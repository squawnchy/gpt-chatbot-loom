# Verwenden der offiziellen Python-Image als Grundlage
FROM python:3.11-slim

# Arbeite aus /app im Container
WORKDIR /app

# Kopiere lokale Code in den Container
COPY . /app

# Installieren von notwendigen Paketen und Reinigen des Caches zur Reduzierung der Größe des Images
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Unser Startbefehl, wenn der Container gestartet wird
CMD ["python", "-m", "chatbot_loom"]