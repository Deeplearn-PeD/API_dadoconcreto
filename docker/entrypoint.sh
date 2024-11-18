#!/usr/bin/env bash
uv sync --frozen --no-dev
source /app/.venv/bin/activate

/app/.venv/bin/gunicorn dadoconcreto_api.wsgi:application --bind 0.0.0.0:9090