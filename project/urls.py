"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# A função static() é um helper do Django que gera padrões de URL (urlpatterns) automaticamente, 
# para servir arquivos de uma pasta específica.
from django.conf.urls.static import static

# da acesso a todas as configurações do projeto MEDIA_URL, etc
from django.conf import settings

urlpatterns = [
    path('', include('contact.urls')),
    path('admin/', admin.site.urls),
]

# apenas para desenvolvimento 
# o que o static está fazendo aqui é mapeando a url 'media/arquivo' 
# executando uma view chamada 'serve' para retornar o arquivo como resposta HTTP
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  