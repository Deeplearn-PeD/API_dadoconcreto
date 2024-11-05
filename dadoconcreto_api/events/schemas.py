from ninja import ModelSchema
from .models import Article, Fulltext, Tone, Volumetimeline

class ArticleSchema(ModelSchema):
    class Config:
        model = Article
        model_fields = "__all__"

class FulltextSchema(ModelSchema):
    class Config:
        model = Fulltext
        model_fields = "__all__"

class ToneSchema(ModelSchema):
    class Config:
        model = Tone
        model_fields = "__all__"

class VolumetimelineSchema(ModelSchema):
    class Config:
        model = Volumetimeline
        model_fields = "__all__"