# 🐣 Fils_Incubator_Project - Dockerfile
# ✅ Creates a lightweight container for deployment.

FROM python:3.9

WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY src/ src/
COPY config/ config/
COPY templates/ templates/
COPY static/ static/

# Set Up Default Configuration
RUN mkdir -p logs
COPY config/default_settings.json config/settings.json

EXPOSE 5000

CMD ["python3", "src/web_server.py"]
