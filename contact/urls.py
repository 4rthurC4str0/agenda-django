from django.urls import path
from contact import views


# se eu tivesse outro app com uma url com o mesmo nome 'index' iria dar problema
# então eu crio esse namespace app_name='contact'
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
