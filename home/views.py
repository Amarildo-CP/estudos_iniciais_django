from django.shortcuts import render
# esse módulo foi importado automaticamente. Por enquanto não vamos usar por isso foi comentado
#from django.http import HttpResponse

# Create your views here.
def home(request):
    print('HOME') 
    #return HttpResponse('home <b>do</b> app 1')
# Agora eu importo pro arquivo onde estava essa views
# Posso adicionar tags html aqui na mensagem (o 'HttpResponse()' renderiza)
# Porém, digitar html e css aqui dessa maneira é improvável porque fica tudo muito grande 
# Por isso não vamos precisar desse 'HttpResponse()' mais e vou comentar a importação desse módulo
# Vamos usar o 'render' e vou descomentar esse módulo que eu havia comentado anteriormente
# Sendo assim vou retornar a função 'render()' 
    #return render(request, 'home/index.html') # Esse segundo parâmetro é o 'template_name'
# Pelas configurações o programa já vai buscar os templates na pasta correta de cada app
# É só eu criar o arquivo que por padrão essa busca será no lugar certo
# Esse arquivo tem que ter precisamente o mesmo nome que eu coloquei aqui nesse segundo parâmetro
# Se fizer somente assim vamos receber uma msg de erro de que esse template não existe
# Temos que configurar algumas coisas pra dar certo
# Primeiro temos que conferir se tudo está digitado corretamente
# Se tudo estiver correto 99% de chance de eu ter me esquecido de colocar o meu app dentro das configurações do 'INSTALLED_APPS' do django

# Mudei nome do template pra termos um namespace de proteção no caso de nomes de templates iguais 
# Temos que mudar em todos pra manter um padrão

# Vamos tentar usar um template GLOBAL (para isso será preciso comentar o outro)
# Lembrando que a pasta 'base' faz parte do caminho até o arquivo que realmente importa
# Ela não é inclusa, começa a incluir aqui a partir da pasta 'global' que está dentro da pasta 'base' 
# Só pensar que incluímos a partir da pasta que faz o papel de namespace, pra diferenciar os templates dentre os outros
    #return render(request, 'global/base.html')

# Porém, eu quero continuar carregando o template anterior (junto com o template global)
# Volto aqui com a view que estava 'home/index.html' e lá nesse arquivo eu extendo ao template global
    #return render(request, 'home/index.html')

# Para enviar dados para serem executados no template temos que acrescentar um terceiro parâmetro 
# Aqui nessa função 'render()'. Esse terceiro parâmetro será o 'context'
# Qualquer coisa que tiver chave e valor - dicionário (qualquer valor). Posso até mesmo não enviar nada
    context = { 'text': 'Controlo aqui o valor da variável lá no template'}
    return render(request, 'home/index.html',
                  #context = { 'text': 'Controlo aqui o valor da variável lá no template'}
                  context,)

# A idéia é exibir esse texto lá no template
# Essa chave 'text' fica como se fosse uma variável lá dentro do template
# E o valor dessa variável é controlado aqui no 'views'
# Posso jogar esse context mesmo dentro de uma variável qualquer fora da função 'render()'
# Só tem que ser antes do 'return' porque depois do return não pode vim nada
# Agora posso mover essa variável para outras views no meu código