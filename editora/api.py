from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from . import schemas
from . import models

api = NinjaAPI()

# Adicionar editora
@api.get('/allEditoras/', response=list[schemas.EditoraSchema])
def getAllEditoras (request):
    editoras = models.Editora.objects.all()
    return editoras

@api.get('/buscaEditora/{editora_id}',response={201: schemas.EditoraSchema})
def getEditora (request, editora_id: int):
    editora = get_object_or_404(models.Editora, pk=editora_id)
    return editora

@api.post('/addEditora/', response={201:schemas.EditoraSchema})
def addEditora (request, payload: schemas.EditoraSchema):
    editora = models.Editora.objects.create(**payload.dict())
    editora.save()
    return editora

@api.put('/editEditora/{editora_id}', response={201:schemas.EditoraSchema})
def editEditora (request, editora_id: int, payload: schemas.EditoraSchema):
    editora = get_object_or_404(models.Editora, id=editora_id)
    for attr, value in payload.dict().items():
        setattr(editora, attr, value)
    editora.save()
    return editora

@api.delete('/deleteEditora/{editora_id}')
def deleteEditora (request, editora_id: int):
    editora = get_object_or_404(models.Editora, id=editora_id)
    editora.delete()
    return {"message": "Editora deletada com sucesso"}