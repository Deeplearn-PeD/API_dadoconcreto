"""
Django Ninja API for acessing the Gdelt database
"""
from ninja import NinjaAPI

api = NinjaAPI()from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    title = models.CharField(max_length=500)
    published_date = models.DateTimeField()
    
    class Meta:
        db_table = 'articles'
        managed = False

class Tone(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tone = models.FloatField()
    positive = models.FloatField()
    negative = models.FloatField()
    polarity = models.FloatField()
    activity_reference_density = models.FloatField()
    self_group_reference_density = models.FloatField()
    word_count = models.IntegerField()
    
    class Meta:
        db_table = 'tone'
        managed = False

class VolumeTimeline(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    volume = models.IntegerField()
    
    class Meta:
        db_table = 'volumetimeline'
        managed = False
from ninja import ModelSchema
from .models import Article, Tone, VolumeTimeline

class ArticleSchema(ModelSchema):
    class Meta:
        model = Article
        fields = ['id', 'url', 'title', 'published_date']

class ToneSchema(ModelSchema):
    class Meta:
        model = Tone
        fields = ['id', 'article_id', 'tone', 'positive', 'negative', 'polarity', 
                 'activity_reference_density', 'self_group_reference_density', 'word_count']

class VolumeTimelineSchema(ModelSchema):
    class Meta:
        model = VolumeTimeline
        fields = ['id', 'date', 'volume']
