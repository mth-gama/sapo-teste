# Base Python
FROM python:3.12-slim

# Evita problemas de buffer no log
ENV PYTHONUNBUFFERED=1

# Cria diretório da app
WORKDIR /app

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements primeiro (melhor cache)
COPY requirements.txt /app/

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia tudo
COPY . /app/

# Expõe porta do Gunicorn
EXPOSE 8000

# Comando padrão para rodar a aplicação
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
