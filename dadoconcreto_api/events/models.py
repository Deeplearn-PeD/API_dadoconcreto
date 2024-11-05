# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1255)
    url_mobile = models.CharField(blank=True, null=True,max_length=255)
    socialimage = models.CharField(blank=True, null=True,max_length=1255)
    seendate = models.DateField()
    domain = models.CharField(max_length=255)
    country = models.CharField(blank=True, null=True,max_length=255)
    language = models.CharField(max_length=255)
    theme = models.CharField(blank=True, null=True,max_length=2550)
    hash_key = models.CharField(unique=True,max_length=2550)

    class Meta:
        managed = False
        db_table = 'article'


class Fulltext(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    content = models.CharField(max_length=5000)
    extracted_at = models.DateField()
    hash_key = models.CharField(max_length=255,unique=True)

    class Meta:
        managed = False
        db_table = 'fulltext'


class Tone(models.Model):
    query = models.CharField(max_length=255)
    date = models.DateField()
    value = models.FloatField()
    hash_key = models.CharField(max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = 'tone'


class Volumetimeline(models.Model):
    keyword = models.CharField(max_length=255)
    date = models.DateField()
    volume = models.FloatField()
    top_articles = models.JSONField()
    hash_key = models.CharField(max_length=255,unique=True)

    class Meta:
        managed = False
        db_table = 'volumetimeline'
