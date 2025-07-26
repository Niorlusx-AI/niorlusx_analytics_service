#!/bin/bash
# Allow overriding host and port via environment variables.
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
uvicorn app:app --host "$HOST" --port "$PORT"
