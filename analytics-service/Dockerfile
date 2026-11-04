# RBHU Enterprise Operations Platform - Python Analytics Microservice
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required for Kaleido & Plotly rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ANALYTICS_PORT=5001
ENV ANALYTICS_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5001

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5001/health || exit 1

CMD ["python", "app.py"]
