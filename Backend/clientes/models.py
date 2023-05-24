from django.db import models

class Cliente(models.Model):
    NIVEL = (
        ('G', 'Gold'),
        ('P', 'Platinum'),
        ('I', 'Iron')
    )
    nome: models.CharField(max_length=30, null=False, blank=False)
    sobrenome: models.CharField(max_length=60, null=False, blank=False)
    email: models.EmailField(max_length=100, unique=True, null=False, blank=False)
    data_nascimento: models.DateField(blank=False, null=False)
    tipo_cliente: models.CharField(max_length=1, null=False, blank=False, choices=NIVEL, default='I')

    def __str__(self):
        return self.nome + '' + self.sobrenome