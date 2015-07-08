from django.db import models

class Talk(models.Model):
    speaker = models.ForeignKey('speakers.Speaker')
    titulo = models.CharField(blank=False, max_length=100)
    descricao = models.TextField(blank=False)
    aprovada = models.BooleanField(default=False)
    alocada = models.BooleanField(default=False)
