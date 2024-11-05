from ninja import ModelSchema
from .models import Article, Fulltext, Tone, Volumetimeline

class ArticleSchema(ModelSchema):
    class Meta:
        model = Article
        fields = "__all__"

class FulltextSchema(ModelSchema):
    class Meta:
        model = Fulltext
        fields = "__all__"

class ToneSchema(ModelSchema):
    class Meta:
        model = Tone
        fields = "__all__"

class VolumetimelineSchema(ModelSchema):
    class Meta:
        model = Volumetimeline
        fields = "__all__"