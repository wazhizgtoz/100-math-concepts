from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Modulo(models.Model):
    """Módulo de aprendizado (ex: Álgebra Linear I)"""
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    icone = models.CharField(max_length=50, default='view_module')
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.nome

class Conceito(models.Model):
    """Conceito individual de matemática para ML"""
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='conceitos')
    descricao = models.TextField()
    explicacao = models.TextField(help_text="Explicação detalhada do conceito")
    exemplo_codigo = models.TextField(blank=True, help_text="Exemplo em Python/NumPy")
    icone = models.CharField(max_length=50, default='widgets')
    ordem = models.IntegerField(default=0)
    concluido = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['modulo__ordem', 'ordem']

    def __str__(self):
        return f"{self.modulo.nome} - {self.titulo}"

    def get_absolute_url(self):
        return reverse('concepts:detalhe', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

