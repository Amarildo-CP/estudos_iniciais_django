from django.urls import path
from . import views
# Essa importação acima é um tipo de importação relativa
# Se tiver na dúvida melhor usar sempre o caminho completo que da no mesmo

# Criar todos os apps com esse namespace já garantido
app_name = 'home'


urlpatterns = [
    path('', views.home, name= 'home'), 
    ]