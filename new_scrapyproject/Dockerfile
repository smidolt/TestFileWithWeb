FROM python:3.9-slim

WORKDIR /app

COPY new_scrapyproject/requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyOpenSSL==20.0.1 cryptography==3.4.8
RUN apt-get update && apt-get install -y postgresql-client
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /app/temp_project && cd /app/temp_project && scrapy startproject valid_project_name && mkdir -p /app/new_scrapyproject && mv valid_project_name/* /app/new_scrapyproject && rm -rf /app/temp_project

COPY new_scrapyproject .



