"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
#from django.http import HttpResponse
#from home import views as home_views
#from blog import views as blog_views
# Ter cuidado pra não importar 2 módulos de mesmo nome 
# Senão um pode sobrescrever o outro
# Por isso somente aqui vou mudar o nome do módulo


# HTTP Request <-> HTTP Response
# MVT é uma varição do MVC

# view: é uma função que recebe a request (quando o cliente acessa)
# Normalmente não é criada aqui

# Posso ter uma VIEW chamada de HOME:
#def home(request):
#    print('HOME') # Esse print aparece no meu terminal não na página do navegador
# Eu posso executar coisas dentro do meu servidor mesmo antes da 'HttpResponse'
# O que eu colocar aqui no lugar desse print será sempre alguma indicação sobre a reponse que virá depois
#    return HttpResponse('HOME1')
# Tudo foi comentado porque foi transferido pro arquivo correto

#def blog(request):
    #print('Posso fazer outras coisas')
#    print('blog')
    #return HttpResponse('Uma mensagem para alguém especial')
#    return HttpResponse('blog')
    
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/', blog),
# Se eu quiser colocar algo na home (raíz do site), poderia usar essa mesma função 'blog'
# Seria como se fossemos somente colocar uma '/' na frente da url, mas isso n pode acontecer
# Porque nenhuma 'url' pode começar com '/'. Quando for assim tem que deixar vazio
    #path('/', blog),
    #path('', blog),
# Nesse caso a url fica vazia, chama a mesma view (porque não criei outra) e consequentemente vai exibir a mesma response
    #path('', home), # Uma rota home com outra view específica para essa rota
    #path('', home_views.home), # Usando agora os módulos importados 
    path('', include('home.urls')), # Aqui vou aninhar urls, por isso comentei a rota anterior
    #path('', home_views.home),
    path('blog/', include('blog.urls')),
]

# Quando eu faço o aninhamento de urls quando eu vou buscar lá no navegador já fica preenchido
# Para fazer esse aninhamento foi preciso comentar alguns módulos que eu havia importado mas que não serão mais precisos
