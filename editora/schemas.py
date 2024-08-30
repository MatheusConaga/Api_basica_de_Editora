from ninja import ModelSchema
from . import models

class EditoraSchema(ModelSchema):
    class Meta:
        model = models.Editora
        fields = ['nome', 'ano', 'contato']