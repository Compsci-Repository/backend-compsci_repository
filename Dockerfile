FROM python:3.12.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-distutils \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py

EXPOSE 5000


CMD ["env", "FLASK_APP=run.py", "python", "-m", "flask", "run", "--host=0.0.0.0"]