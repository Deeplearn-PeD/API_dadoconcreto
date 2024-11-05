from ninja import NinjaAPI
from typing import List
from events.models import Article, Fulltext, Tone, Volumetimeline
from events.schemas import ArticleSchema, FulltextSchema, ToneSchema, VolumetimelineSchema

api = NinjaAPI()

@api.get("/articles", response=List[ArticleSchema])
def list_articles(request):
    articles = Article.objects.all()
    return articles

@api.get("/articles/{hash_key}", response=ArticleSchema)
def get_article(request, hash_key: str):
    article = Article.objects.get(hash_key=hash_key)
    return article

@api.get("/fulltexts", response=List[FulltextSchema])
def list_fulltexts(request):
    texts =  Fulltext.objects.all()
    return texts

@api.get("/fulltexts/{hash_key}", response=FulltextSchema)
def get_fulltext(request, hash_key: str):
    text =  Fulltext.objects.get(hash_key=hash_key)
    return text

@api.get("/tones", response=List[ToneSchema])
def list_tones(request):
    tones = Tone.objects.all()
    return tones

@api.get("/tones/{hash_key}", response=ToneSchema)
def get_tone(request, hash_key: str):
    tone = Tone.objects.get(hash_key=hash_key)
    return tone

@api.get("/volumetimelines", response=List[VolumetimelineSchema])
def list_volumetimelines(request):
    volumetimelines = Volumetimeline.objects.all()
    return volumetimelines

@api.get("/volumetimelines/{hash_key}", response=VolumetimelineSchema)
def get_volumetimeline(request, hash_key: str):
    volumetimeline = Volumetimeline.objects.get(hash_key=hash_key)
    return volumetimeline

# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libpq-dev

COPY pyproject.toml uv.lock ./
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install -r uv.lock

# Final stage
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["gunicorn", "dadoconcreto_api.wsgi:application", "--bind", "0.0.0.0:8000"]
version: '3.8'

services:
  web:
    build: .
    command: gunicorn dadoconcreto_api.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    expose:
      - 8000
    environment:
      - DJANGO_SETTINGS_MODULE=dadoconcreto_api.settings
      - PYTHONPATH=/app
    networks:
      - app_network
    restart: unless-stopped

networks:
  app_network:
    driver: bridge
