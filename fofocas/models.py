# fofocas/models.py

from django.db import models

TAG_CHOICES = [
    ('chocante', 'Chocante'),
    ('descontraida', 'Descontraída'),
    ('denuncia', 'Denúncia'),
    ('ajuda', 'Ajuda'),
    ('novidade', 'Novidade'),
]

class Fofoca(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=20, choices=TAG_CHOICES, default='descontraida')
    
    reacao_feliz = models.IntegerField(default=0)
    reacao_triste = models.IntegerField(default=0)
    reacao_bravo = models.IntegerField(default=0)
    reacao_surpreso = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
    def get_tags_colors(self):
        colors = {
            'chocante': {'bg': 'bg-yellow-100', 'text': 'text-yellow-800'},
            'descontraida': {'bg': 'bg-purple-100', 'text': 'text-purple-800'},
            'denuncia': {'bg': 'bg-red-100', 'text': 'text-red-800'},
            'ajuda': {'bg': 'bg-blue-100', 'text': 'text-blue-800'},
            'novidade': {'bg': 'bg-green-100', 'text': 'text-green-800'},
        }
        return colors.get(self.tags, {'bg': 'bg-gray-100', 'text': 'text-gray-800'})

class Comentario(models.Model):
    fofoca = models.ForeignKey(Fofoca, on_delete=models.CASCADE, related_name='comentarios')
    corpo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    
    # Campo para o comentário pai. Crucial para o aninhamento.
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    
    def __str__(self):
        return f'Comentário na fofoca: {self.fofoca.titulo}'