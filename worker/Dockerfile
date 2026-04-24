FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

HEALTHCHECK CMD python -c "import redis; r=redis.Redis(host='redis', port=6379); r.ping()" || exit 1

CMD ["python", "-u", "worker.py"]