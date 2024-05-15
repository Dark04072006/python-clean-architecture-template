import os  # noqa: N999

host = os.getenv("SERVER_HOST", "localhost")
port = os.getenv("SERVER_PORT", "8000")

bind = f"{host}:{port}"
workers = int(os.getenv("GUNICORN_WORKERS", "4"))

loglevel = "info"
graceful_timeout = 300
worker_class = "uvicorn.workers.UvicornWorker"
