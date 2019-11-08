from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Perfil(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, related_name="usuario",on_delete=models.CASCADE)
    descricao = models.TextField(max_length=200)
    amigos = models.ManyToManyField('Perfil', verbose_name="lista_amigos",null=True, blank=True)
    ativo = models.BooleanField(default=True)
    

    def __str__(self):
        return self.usuario.username

class Comentario(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    pessoa = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)
    comentario = models.TextField(max_length=200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.pessoa.username
    

   
class Publicao(models.Model):    
    pessoa = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True)
    conteudo = models.TextField('Conteúdo',max_length = 200)
    data = models.DateTimeField(auto_now_add=True)
    comentarios = models.ManyToManyField(Comentario,verbose_name="lista_comentarios",null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def reveso(self):
        return reverse("Publicao", kwargs={"Publicao": self.pk})

    def __str__(self):
        return self.pessoa.username