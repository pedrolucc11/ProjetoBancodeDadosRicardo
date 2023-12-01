from django.db import models

class Jog(models.Model):
    nome = models.CharField(max_length=200, help_text= "Nome do Jogador")

    posicao = models.CharField(max_length=50, help_text= "Posição")

    def __str__(self):
        return f'Nome: {self.nome}. Posicao: {self.posicao}.'
