
## Models
são classes que representam tabelas no banco de dados, cada atributo da classe
vira uma coluna da tabela

Quando eu fizer alterações no meu Model eu rodo esse comando, para criar um 
registro nas migrations

```
python manage.py makemigrations
```

Esse comando eu rodo para aplicar as migrations que ainda não foram aplicadas
( na tabela 'django_migrations' ele pega o que não foi aplicado e executa o sql 
no banco )
```
python manage.py migrate
```

## Migrations
São arquivos que registram as mudanças feitas nos models, para que o Django 
saiba como criar/alterar as tabelas no banco de dados

Cada arquivo descreve o que mudou de uma versão para a outra

- ### 0001 → criou a tabela do zero:
```
operations = [
    migrations.CreateModel(
        name='Produto',
        fields=[
            ('id', models.AutoField(primary_key=True)),
            ('nome', models.CharField(max_length=200)),
        ]
    )
]
```

- ### 0002 → adicionou um campo:
```
operations = [
    migrations.AddField(
        model_name='produto',
        name='foto',
        field=models.ImageField(upload_to='fotos/'),
    )
]
```

- ### 0003 → removeu um campo:
```
operations = [
    migrations.RemoveField(
        model_name='produto',
        name='descricao',
    )
]
```

```
Você altera models.py  (aqui você cria o modelo da tabela)
    ↓
makemigrations → cria arquivo 0002_....py (o "registro")
    ↓
migrate → lê o arquivo e executa o SQL no banco
    ↓
Anota na tabela django_migrations que já foi aplicado
```


## Registrar o Model no admin
Aqui eu configuro o model no admin do django, só após colocar o model aqui ele 
estará disponivel no admin.
```py
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
```

### list_display: 
 - Serve para selecionar as colunas que serão exibidas no admin do django
```py
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
```

## ordering:
 - Serve para criar uma ordenação por padrão (crescente por padrão) '-id' -> decrescente 
```py
ordering = ('id', )
```

## list_filter:
 - Serve para criar uma lista de filtros no admin
```py
list_filter = ('created_date', )
```

## search_fields:
 - Serve para adicionar um campo de pesquisa, irá pesquisar pelos campos passados
```py
search_fields = 'id', 'first_name', 'last_name',
```

## list_per_page:
 - Serve para listar os itens cadastrados no admin em uma determinada quantidade por página 
```py
list_per_page = 1
list_max_show_all = 200
```
- O 'list_max_show_all' faz com que o botão 'mostrar tudo' das páginas não mostre tudo quando tiver mais de 200 itens

## list_editable:
 - Serve para transformar o campo em um input editável, facilitando a modificação do valor
```py
list_editable = 'first_name', 'last_name',
```

## list_display_link:
 - Serve para tranformar o campo em um link para o contato(item)
```py
list_display_links = 'id', 'phone',
```

## Shell Django - salvando itens na base de dados

```py
# Aqui foi a importação do model para o shell
>>> from contact.models import Contact

# Aqui a classe foi printada para saber qual era a classe
>>> Contact
<class 'contact.models.Contact'>

# Aqui foi cadastrado o vaor do campo 'first_name'( armazenado dentro de uma variável )
>>> c = Contact(first_name='Carvalho')
>>> c
<Contact: Carvalho > #( Aqui eu vejo o que tem dentro da variável )
>>> c.save()

# Cadastrando outro campo de forma diferente 
>>> c.last_name = 'Ronaldo'
>>> c.save()
>>> c
<Contact: Carvalho Ronaldo>
 
# Para deletar o item
>>> c.delete()

# Pega somente um item(objeto) do model Contact
>>> c = Contact.objects.get(id=1)

# Pega todos os valores ( da para fazer um for nessa lista de objetos )
# normalmente não utilzado porque realmente retorna todos os itens da base de dados
>>> c = Contact.objects.all()


# Mais utilizado para selecionar valores é filter()
>>> c = Contact.objects.filter(pk=1)

# Pega todos os objetos do bd mas ordenado de forma decrescente
>>> c = Contact.objects.all().order_by('-id')

# Para criar um objeto no banco de dados 
# A diferença é que o 'create()' já salva no banco de dados, não precisa usar o 'save()'
>>> c = Contact.objects.create(first_name='Marcos', last_name='Vitor')
```


## UPLOAD DE ARQUIVOS E IMAGENS:

```py
# É o caminho da pasta do disco do servidor, onde os arquivos enviados pelo usuário 
# em algum campo ImageField ou FileField, serão salvos.
MEDIA_ROOT = BASE_DIR / 'media'
```

```py
# É o prefixo da URL que o navegador vai usar para acessar a pasta dos arquivos enviados pelo usuário (MEDIA_ROOT) 
MEDIA_URL = 'media/'
```

Isso significa: se você salvou um arquivo foto.jpg, ele vai ficar acessível em algo como:
```
http://localhost:8000/media/foto.jpg
```

### Criando o campo de imagem no Model
 - Passar o caminho de onde será salva a imagem em 'upload_to'
 - Vai ser criada a pasta 'pictures/' dentro do diretório especificado em MEDIA_ROOT ou seja 'media/'
 - Dá para pegar a data que a imagem foi salva 
```py
picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
```


```py
# o django vai procurar tudo que é arquivo estático e vai jogar dentro dessa pasta 
# aí nessa pasta é onde o servidor vai buscar os arquivos estáticos
STATIC_ROOT = BASE_DIR / 'static' # collectstatic

# comando para coletar os arquivos estáticos
python manage.py collectstatic
```
