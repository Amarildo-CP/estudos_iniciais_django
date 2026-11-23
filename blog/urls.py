from django.urls import path
from . import views
# Essa importação acima é um tipo de importação relativa
# Se tiver na dúvida melhor usar sempre o caminho completo que da no mesmo

# Para criar um namespace para a url:
app_name = 'blog' # Estou dizendo que esse app inteiro chama 'blog'
# Esse 'app_name' é o namespace de todas as urls que estão nesse app
# Agora vou lá no arquivo 'menu.html' e mudo o nome da url para esse nome desse namespace 'app_name' senão não vai dar mais match
# Dessa forma eu troco o nome dessa url para 'home' afinal essa url é a home do blog
# Não vai dar erro de match porque lá no 'menu.html' a procura será pelo namespace e não pelo nome da url como era feito antes 


urlpatterns = [
    path('post/<int:post_id>/', views.post, name= 'post'),  # Criando 'urls' dinâmicas
    path('post/', views.blog, name= 'home'), # Coloquei 'urls' mais específicas primeiro do que as outras
    # Por isso inverti aqui a ordem das urls
    # O que vem depois da '/' é que fica dinâmico (<id>). Eu coloco aqui o que eu quiser criar, pode ser qualquer coisa
    # Lembrando que isso tem que bater com a minha 'view', nesse caso a view do blog que é onde eu estou
    # Essa view tem que receber o request (que foi definido lá no início) E esse '<id>', por isso não posso reutilizar conforme estava
    # Se eu não fizer essa alteração na view tbm vai gerar um erro
    path('exemplo/', views.exemplo, name= 'exemplo'), # Vou acrescentar uma nova url

    ]
# Essa 'url' está sendo incluída por outra url por isso o espaço vazio no primeiro parâmetro
# Fica como se fosse a 'home' mas é 'blog/'
# Ele está sendo incluído pela url do project
# Na url do project ele já começa com 'blog/' esse aqui só complementa

# Nesse caso a url 'exemplo/' tem que estar abaixo da url 'blog/'
# Se, na hora de buscar no navegador eu inverter essa ordem vai gerar mensagem de erro

# O parâmetro 'name' é pra colocar um nome para essa url pra depois ela ser buscada por esse nome 
# Para evitar de ter que colocar a url na forma hard coded
# Esse nome pode ser o que eu quiser, desde que faça match com o nome que eu coloquei la na tag '<a>' no arquivo 'menu.html