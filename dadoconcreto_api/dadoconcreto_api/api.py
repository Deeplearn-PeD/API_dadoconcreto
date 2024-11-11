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

@api.get("/articles/{country}", response=List[ArticleSchema])
def list_articles_by_country(request, country: str):
    articles = Article.objects.filter(country=country).all()
    return articles