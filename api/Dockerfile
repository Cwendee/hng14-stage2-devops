# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Install curl (for healthcheck)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser

# Copy installed packages
COPY --from=builder /root/.local /home/appuser/.local

# Copy app code
COPY . .

# Set PATH
ENV PATH=/home/appuser/.local/bin:$PATH

# Switch user
USER appuser

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8000/docs || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]