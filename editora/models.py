from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField(default=2024)
    contato = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
