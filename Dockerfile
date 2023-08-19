# Verwenden der offiziellen Python-Image als Grundlage
FROM python:3.11-slim

# Arbeite aus /app im Container
WORKDIR /app

COPY requirements.txt /app

# Installieren von notwendigen Paketen und Reinigen des Caches zur Reduzierung der Größe des Images
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY /chatbot_loom /app/chatbot_loom

# Exponieren des Ports 8967
EXPOSE 8967

# Unser Startbefehl, wenn der Container gestartet wird
ENTRYPOINT ["python", "-m"]
CMD ["chatbot_loom"]
