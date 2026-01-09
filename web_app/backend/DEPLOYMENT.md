# Backend Deployment Guide

## Development Environment

```bash
cd web_app/backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set your HEPAI_API_KEY
python -m app.main
```

## Production Deployment

### Using Uvicorn

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Gunicorn + Uvicorn

```bash
pip install gunicorn
gunicorn app.main:app \
  -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --timeout 300 \
  --access-logfile - \
  --error-logfile -
```

### Using Systemd Service

Create `/etc/systemd/system/hainougat-backend.service`:

```ini
[Unit]
Description=HaiNougat Backend Service
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/path/to/web_app/backend
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn app.main:app \
  -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --timeout 300
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable hainougat-backend
sudo systemctl start hainougat-backend
sudo systemctl status hainougat-backend
```

### Using Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t hainougat-backend .
docker run -d -p 8000:8000 --env-file .env hainougat-backend
```

## Environment Variables

Required:
- `HEPAI_API_KEY`: Your HepAI API key

Optional:
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `MAX_CONCURRENT_REQUESTS`: Max concurrent requests (default: 5)
- `UPLOAD_MAX_SIZE`: Max upload size in bytes (default: 10485760)
- `CORS_ORIGINS`: Allowed CORS origins (comma-separated)

## Health Check

```bash
curl http://localhost:8000/api/v1/health
```

## Logging

Configure logging in production:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```
