
# Views aqui é um pacote, entao quando eu importo o pacote 
# as coisas do que são importadas aqui no __init__ ficam disponiveis em outros arquivos
# assim não preciso importar os arquivos apenas o pacote 

# --- Posso fazer assim
# from contact import views
# tudo que foi importado aqui no init vai estar disponivel no 'views.'

# --- Ao contrário disso
# teria que importar todos os arquivos especificos em outro lugar em vez de somente o pacote Views
# from contact.views import contact_views  

# - Transformar a 'views.py' em um pacote 'views' é legal para que eu não deixe tudo em um arquivo views.py
# assim posso criar varios outros arquivos separando o código especifico para cada págin
# organizando o projeto 

from .contact_views import *