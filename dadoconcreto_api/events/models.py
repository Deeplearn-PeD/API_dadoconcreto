# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    title = models.CharField()
    url = models.CharField()
    url_mobile = models.CharField(blank=True, null=True)
    socialimage = models.CharField(blank=True, null=True)
    seendate = models.DateField()
    domain = models.CharField()
    country = models.CharField(blank=True, null=True)
    language = models.CharField()
    theme = models.CharField(blank=True, null=True)
    hash_key = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'article'


class Fulltext(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    content = models.CharField()
    extracted_at = models.DateField()
    hash_key = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'fulltext'


class Tone(models.Model):
    query = models.CharField()
    date = models.DateField()
    value = models.FloatField()
    hash_key = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'tone'


class Volumetimeline(models.Model):
    keyword = models.CharField()
    date = models.DateField()
    volume = models.FloatField()
    top_articles = models.JSONField()
    hash_key = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'volumetimeline'
