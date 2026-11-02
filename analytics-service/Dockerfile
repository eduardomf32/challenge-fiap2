FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8005

# Cria usuário não-root por segurança
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -s /bin/bash appuser

# Instala dependências mantendo compatibilidade com Flask 2.2.2 (Werkzeug < 3.0)
COPY requirements.txt .
RUN pip install --no-cache-dir "Werkzeug<3.0" -r requirements.txt

# Copia o código da aplicação
COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8005

CMD ["sh", "-c", "exec gunicorn --timeout 60 --bind 0.0.0.0:${PORT:-8005} app:app"]
