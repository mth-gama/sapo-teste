FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala pacotes Python
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia o restante do projeto
COPY . .

# Porta da aplicação
EXPOSE 8000

# Roda migrations e inicia o servidor
CMD ["bash", "-c", "\
    python manage.py makemigrations --noinput && \
    python manage.py migrate --noinput && \
    gunicorn app.wsgi:application --bind 0.0.0.0:8000 \
"]
