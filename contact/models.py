from django.db import models
from django.utils import timezone


# blank=True -> deixar o campo opcional

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) # campo para saber se eu quero ou não exibir o contato
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # passar o caminho de onde será salva a imagem
    # vai ser criada a pasta pictures dentro do diretório especificado em MEDIA_ROOT ou seja 'media/'
    # dá para pegar a data que a imagem foi salva 
    category = models.ForeignKey(
        Category, # esse campo category é uma chave estrangeira do model Category (id)
        on_delete=models.SET_NULL, # ao deletar uma categoria vai definir esse campo como Null
        blank=True, # deixa o campo opcional
        null=True, # permite o campo ser nulo
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'