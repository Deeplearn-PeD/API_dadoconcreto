"""
Django Ninja API for acessing the Gdelt database
"""
from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Article, Tone, VolumeTimeline
from .schemas import ArticleSchema, ToneSchema, VolumeTimelineSchema

api = NinjaAPI()

@api.get("/articles", response=List[ArticleSchema])
def list_articles(request):
    """Get all articles"""
    return Article.objects.all()

@api.get("/articles/{article_id}", response=ArticleSchema)
def get_article(request, article_id: int):
    """Get a specific article by ID"""
    return get_object_or_404(Article, id=article_id)

@api.get("/tone", response=List[ToneSchema])
def list_tone(request):
    """Get all tone entries"""
    return Tone.objects.all()

@api.get("/tone/{tone_id}", response=ToneSchema)
def get_tone(request, tone_id: int):
    """Get a specific tone entry by ID"""
    return get_object_or_404(Tone, id=tone_id)

@api.get("/tone/article/{article_id}", response=List[ToneSchema])
def get_article_tone(request, article_id: int):
    """Get tone entries for a specific article"""
    return Tone.objects.filter(article_id=article_id)

@api.get("/volumetimeline", response=List[VolumeTimelineSchema])
def list_volume_timeline(request):
    """Get all volume timeline entries"""
    return VolumeTimeline.objects.all()

@api.get("/volumetimeline/{timeline_id}", response=VolumeTimelineSchema)
def get_volume_timeline(request, timeline_id: int):
    """Get a specific volume timeline entry by ID"""
    return get_object_or_404(VolumeTimeline, id=timeline_id)
