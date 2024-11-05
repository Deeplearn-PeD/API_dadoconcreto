from ninja import NinjaAPI
from typing import List
from events.models import Article, Fulltext, Tone, Volumetimeline
from events.schemas import ArticleSchema, FulltextSchema, ToneSchema, VolumetimelineSchema

api = NinjaAPI()

@api.get("/articles", response=List[ArticleSchema])
def list_articles(request):
    return Article.objects.all()

@api.get("/articles/{hash_key}", response=ArticleSchema)
def get_article(request, hash_key: str):
    return Article.objects.get(hash_key=hash_key)

@api.get("/fulltexts", response=List[FulltextSchema])
def list_fulltexts(request):
    return Fulltext.objects.all()

@api.get("/fulltexts/{hash_key}", response=FulltextSchema)
def get_fulltext(request, hash_key: str):
    return Fulltext.objects.get(hash_key=hash_key)

@api.get("/tones", response=List[ToneSchema])
def list_tones(request):
    return Tone.objects.all()

@api.get("/tones/{hash_key}", response=ToneSchema)
def get_tone(request, hash_key: str):
    return Tone.objects.get(hash_key=hash_key)

@api.get("/volumetimelines", response=List[VolumetimelineSchema])
def list_volumetimelines(request):
    return Volumetimeline.objects.all()

@api.get("/volumetimelines/{hash_key}", response=VolumetimelineSchema)
def get_volumetimeline(request, hash_key: str):
    return Volumetimeline.objects.get(hash_key=hash_key)

