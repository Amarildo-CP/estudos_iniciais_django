from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
#from . import data # Outra maneira de importar usando o caminho relativo
from blog.data import posts
# Importando usando o caminho absoluto (sem o namespace do módulo)

# Create your views here.
# Aqui será onde realmente vamos criar nossos views
# Os mesmos que criamos como exemplo lá na pasta 'project' dentro do arquivo 'urls.py'

def blog(request):
    #print('Posso fazer outras coisas')
    print('blog')
# Adicionar a variável 'context' para ser exibido no template
    context = { 'text': 'Controlo aqui o valor da variável lá no template - blog',
    #return HttpResponse('Uma mensagem para alguém especial')
    #return HttpResponse('blog do app 1')
    'posts': posts} # Para importar os dados que foram salvos da api
    return render(request, 'blog/index.html', context,)


# Criando uma nova view para ser usada nas 'urls dinâmicas':
# Posso colocar o nome que eu quiser para essa nova 'view'
# Nessa view eu preciso receber o 'id' já que pertence à url dinâmica
def post(request, post_id): # Como tem uma função do python que chama 'id' podemos alterar o nome pra não fazer confusão
    found_post = None # Primeiro crio uma variável vazia
# Tudo tendo como baso nosso arquivo 'data.py'
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None: # Para corrigir um possível erro de tipagem
        #raise Exception('Post não existe')
        raise Http404('Post não existe')
# Para o erro de página não encontrada existe uma exceção específica: 404 (tem no próprio django 'Http404')
# Agora sim criei uma exceção correta para esse erro de 'página não encontrada'. Com o 'status code' correto 
# Continua sendo um erro porém agora com o código correto
# Depois que eu encontrei o 'post' eu não preciso mais ler o restante dos posts (por isso esse 'break')
# Se fosse dentro de uma função poderia ser um 'return'
    print('post', id) # Só pra mostrar qual 'id' estamos acessando (isso vai aparecer no meu terminal aqui do VSCode)
# Eu posso usar esse parâmetro a meu favor já que será mostrado no meu terminal o que o usuário quer acessar
    post = next((p for p in posts if p['id'] == id), None) # Fiz isso por indicação de aluno pq não dava certo
    context = { #'text': 'Controlo aqui o valor da variável lá no template - blog',
# Vou comentar o 'text' já que fiz aquele 'if' não vai gerar nenhum erro no código
    'post': found_post,
    #'title': 'O context vai aparecer-'} # Aqui eu estou colocando um título aleatório
    # Mas eu posso fazer com que o título do próprio 'post' seja tbm o título da página
    'title': found_post['title'] + ' - '} # Título do post sendo tbm o título da página
    #'post': post} 
    return render(request, 'blog/post.html', context,)


# Criação de uma nova view:
# Para se ligar à nova url que foi adicionada
def exemplo(request):
    print('exemplo')
    context = { 'text': 'Controlo aqui o valor da variável lá no template - exemplo',
               'title': 'Essa é uma página de exemplo - '}
# Vou adicionar mais de uma chave pra essa variável
# Coloco um espaço no final pq é uma variável de títiulo (pra não ficar mto colado)
    #return HttpResponse('exemplo do app 1')
    return render(request, 'blog/exemplo.html', context,)

# Vou fazer as mesmas alterações que fiz pro app 'home' para renderizar templates
# Comentar o que não é mais preciso e colocar como deve ser mesmo feito
# Nesse caso como tem 2 views, cada um está renderizando um template

# Lembrando que para templates de mesmo nome temos que criar um namespace pro programa não pegar o primeiro que encontrar
# Adiciona 1 passo a mais e evita colisão de nomes de arquivos

# Com a adição da variável 'context' e usando essa variável na função 'render()'
# Eu posso ter um 'context' diferente para ser exibido em cada template através de sua view