FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY ./init.sql /init.sql
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyOpenSSL==20.0.1 cryptography==3.4.8
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/entrypoint.sh"]
