# Leadgen Bot - AI-Powered Lead Generation Platform

A FastAPI-based service for intelligent lead generation and processing.

## Project Structure

```
leadgen-bot/
├── src/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py               # Configuration management
│   ├── core/
│   │   ├── __init__.py
│   │   ├── security.py         # Authentication & authorization
│   │   └── exceptions.py       # Custom exceptions
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── health.py       # Health check endpoints
│   │       └── leads.py        # Lead management endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── database.py         # Database connection management
│   │   ├── minio_service.py    # MinIO operations
│   │   └── lead_service.py     # Lead processing logic
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py          # Pydantic schemas
│   │   └── database.py         # SQLAlchemy models (future)
│   └── utils/
│       ├── __init__.py
│       └── logging.py          # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   ├── test_health.py          # Health endpoint tests
│   └── test_leads.py           # Lead service tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.12+ (for local development)

### Environment Setup

```bash
# Copy example environment file
cp .env.example .env

# Update with your configuration
vim .env
```

### Running with Docker Compose

```bash
# Create external network
docker network create leadgen_net

# Start the service
docker-compose up -d

# Check health
curl http://localhost:8000/api/v1/health
```

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run with uvicorn
uvicorn src.main:app --reload --port 8000
```

## API Endpoints

### Health Check
- **GET** `/api/v1/health` - System health status

```json
{
  "status": "ok",
  "postgres": true,
  "minio": true
}
```

## Configuration

All configuration is managed through environment variables. See `.env.example` for all available options.

### PostgreSQL
- `POSTGRES_HOST` - Database host
- `POSTGRES_PORT` - Database port
- `POSTGRES_DB` - Database name
- `POSTGRES_USER` - Database user
- `POSTGRES_PASSWORD` - Database password

### MinIO
- `MINIO_ENDPOINT` - MinIO endpoint URL
- `MINIO_ACCESS_KEY` - MinIO access key
- `MINIO_SECRET_KEY` - MinIO secret key
- `MINIO_BUCKET` - Default bucket name
- `MINIO_SECURE` - Use HTTPS for MinIO

## Development

### Running Tests

```bash
pip install pytest pytest-asyncio pytest-cov
pytest tests/ -v --cov=src
```

### Code Quality

```bash
pip install black flake8 mypy
black src/
flake8 src/
mypy src/
```

## Deployment

The service is containerized and ready for deployment in any Docker-compatible environment (Kubernetes, Docker Swarm, etc.).

### Health Check Endpoint

The `/api/v1/health` endpoint can be used for liveness and readiness probes:

```yaml
livenessProbe:
  httpGet:
    path: /api/v1/health
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /api/v1/health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and quality checks
4. Submit a pull request

## License

MIT
