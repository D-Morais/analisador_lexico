palavras_reservadas = ["int", "double", "float", "real", "break", "case", "char", "const", "continue"]
tokens = {} # Um dicionário para guardar os tokens
erros = {} # Um dicionário para guardar os erros
simbolos = {} # Um dicionário para guardar os simbolos
simbolos_aux = [] # Lista para guardar os símbolos
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "h", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "y"]

"""
Método responsável por printar as informações na tela, recebe por parâmetro 3 itens: 
Os itens da tabela de tokens, simbolos ou erros;
A frase informando qual é a tabela;
E a opção que os itens anteriores correspondem.
Após ele ordenas os itens da tabela com a função sorted() e printa as informações de posição e valor correspondente.
"""
def mostrar_informacaos(tabela, string, op):
    tabela_ordenada = sorted(tabela.items())
    cont = 1
    print(f'\n{string}')
    print("================================================")
    if op == 0:
        for item in tabela_ordenada: # printa as informações da tabela de tokens
            print(f'[{item[0]}] {item[1].upper()}')
    if op == 1:
        for item in tabela_ordenada: # printa as informações da tabela de simbolos
            print(f'{cont} - {item[1]}')
            cont += 1
    if op == 2:
        for item in tabela_ordenada: # printa os erros
            print(f'{item[0]} ({item[1]})')
    print("================================================")

"""
 O método procura_comentarios, abre o arquivo e percorre ele até o final, 
pegando linha por linha e verificando se ela é um comentário com a função startswith(),
que verifica se a linha inicia com //.
"""
def procura_comentarios(lista):
    with open("teste.txt", "r") as arquivo:
        cont = 1

        while True:
            linha_atual = arquivo.readline().strip('\n')

            if linha_atual == "": # comando utilizado para fazer o controle de final de arquivo.
                linha_atual = arquivo.readline().strip("\n")
                if linha_atual == "": # verifica duas vezes, para ter caso acha uma linha em branco no arquivo, mas ainda não seja o final dele.
                    break

            if linha_atual.startswith("//"):
                lista.update({cont: "COMENTÁRIO"})

            cont += 1


"""
 O método palavras_reservadas, abre o arquivo e percorre ele até o final, 
pegando linha por linha e comparando com a lista de palavras reservadas, caso o conteúdo da linhas
seja uma palavra reservada, o conteúdo é adicionado ao dicionário(lista).
"""
def procura_palavras_reservadas(lista):
    with open("teste.txt", "r") as arquivo:
        cont = 1
        while True:
            linha_atual = arquivo.readline().strip("\n")

            if linha_atual == "": # comando utilizado para fazer o controle de final de arquivo.
                linha_atual = arquivo.readline().strip("\n")
                if linha_atual == "": # verifica duas vezes, para ter caso acha uma linha em branco no arquivo, mas ainda não seja o final dele.
                    break

            for palavra in palavras_reservadas: # pega palavra por palavra da lista de palavras reservadas, para posterior comparação.
                if palavra == linha_atual:
                    lista.update({cont: f"{palavra.upper()}"}) # adiciona a palavra ao dicionário(lista)

            cont += 1


"""
O método é responsavél de encontrar os tokens de identificador e de numeros,
ele percorre o arquivo verificando linha por linha, e toda vez que encontra
algum identificador ou numero, ele verifica se aquele token já existe,
chamando o método valida_simbolos(), e pega a posição do token na tabela de simbolos,
salvando o token, a posição e a qual dos simbolos ele faz referencia
"""
def procura_identificadores_e_numeros(lista):
    with open("teste.txt", "r") as arquivo:
        cont = 0
        encontrou = False
        while True:
            linha_atual = arquivo.readline().strip("\n")

            if linha_atual == "":
                linha_atual = arquivo.readline().strip("\n")
                if linha_atual == "":
                    break
            cont += 1

            if linha_atual.startswith(" ") or linha_atual.startswith("//"): # verifica se é um comentario ou começa com espaço em branco e pula a linha.
                encontrou = True # quando encontrou recebe True, ele não entra em nenhuma das condicionais de verificação.

            for palavra in palavras_reservadas: # verifica se é uma palavra reservada e pula a linha.
                if palavra == linha_atual:
                    encontrou = True

            if linha_atual.isalnum() and encontrou == False: # verifica se a linha é alfanúmerica
                for letra in alfabeto: # percorre posição por posição da linha
                    if linha_atual[0] == letra or linha_atual[0] == letra.upper(): # verifica se a primeira linha é uma letra maiuscula ou minuscula.
                        ident = valida_simbolos(linha_atual, cont) # pega a posição na tabela de simbolos
                        lista.update({cont: f"IDENTIFICADOR {ident}"}) # salva a informação
                        encontrou = True

            if linha_atual.isnumeric() and encontrou == False: # verifica se é um número
                if int(linha_atual) <= 99 and len(linha_atual) <= 2: # se o número tem duas casa decimais e é menor ou igual a 99
                    ident = valida_simbolos(linha_atual, cont) # pega a posição na tabela de simbolos
                    tokens.update({cont: f"NÚMERO INTEIRO {ident}"}) # salva a informação
                    encontrou = True
                else:
                    erros.update({cont: f"{linha_atual}"}) # se não for então é salvo um erro
                    continue
            if encontrou == False:
                try:
                    if float(linha_atual): # verifica se é um float
                        if linha_atual[0:2].isnumeric() and linha_atual[2:3] == ".":
                            if len(linha_atual) == 5:
                                ident = valida_simbolos(linha_atual, cont)
                                tokens.update({cont: f"NÚMERO REAL {ident}"})
                                encontrou = True
                        if linha_atual[0:1].isnumeric() and linha_atual[1:2] == ".":
                            if len(linha_atual) == 4:
                                ident = valida_simbolos(linha_atual, cont)
                                tokens.update({cont: f"NÚMERO REAL {ident}"})
                                encontrou = True
                except ValueError:
                    continue

            encontrou = False

"""
O método percorre as linhas do arquivo, verificando por meio de ifs, se existe erro na linha,
por erros se entende aquilo que não é aceito pela linguagem, ou seja, caracteres especiais,
uma string que começa com número e depois tem letras, e etc.
"""
def procura_erros():
    with open("teste.txt", "r") as arquivo:
        cont = 0
        while True:
            linha_atual = arquivo.readline().strip("\n")

            if linha_atual == "":
                linha_atual = arquivo.readline().strip("\n")
                if linha_atual == "":
                    break

            cont += 1

            if linha_atual.startswith("//"):
                continue
            if linha_atual.startswith(" "): # verifica se começa com espaço.
                erros.update({cont: f"{linha_atual}"})
                continue
            if linha_atual[0:1].isalpha() and not linha_atual.isalnum(): # verifica se a string começa com uma letra, mas não é um identificador.
                erros.update({cont: f"{linha_atual}"})
                continue
            if linha_atual.isnumeric() and int(linha_atual) > 99: # verifica se um número é maior que 99.
                erros.update({cont: f"{linha_atual}"})
                continue
            if not linha_atual.isalnum(): # verifica os números floats que são errados.
                if linha_atual[2:3] == "." and len(linha_atual) <= 4:
                    erros.update({cont: f"{linha_atual}"})
                    continue
                if linha_atual[1:2] == "." and len(linha_atual) > 4:
                    erros.update({cont: f"{linha_atual}"})
                    continue
            if not linha_atual.isalnum(): # verifica os números floats que são aceitos, para não cair em algum outro erro.
                if linha_atual[0:2].isnumeric() and linha_atual[2:3] == ".":
                    if len(linha_atual) == 5:
                        continue
                if linha_atual[0:1].isnumeric() and linha_atual[1:2] == ".":
                    if len(linha_atual) == 4:
                        continue
                erros.update({cont: f"{linha_atual}"})
            if linha_atual[0:1].isnumeric() and linha_atual[1:].isalnum(): # verifica se a primeira posição da string é um número, mas o restante não.
                if not linha_atual.isnumeric():
                    erros.update({cont: f"{linha_atual}"})
                    continue


"""
 O método é responsável por analisar se já existe o simbolo na lista, 
caso não exista, ele é adicionado a lista de simbolos. 
Para esse controle, o método verifica se o simbolo não está presenta na
lista auxiliar de simbolos, caso ele não esteja, adiciona o elemento ao
dicionário de simbolos e também a lista auxiliar de simbolos.
Após, é verificado a posição que o simbolo se encontra na lista e essa posição
é retornada.
"""
def valida_simbolos(simbolo, posicao):
    cont = 1
    if not simbolo in simbolos_aux:
        simbolos.update({posicao: f"{simbolo}"})
        simbolos_aux.append(simbolo)
    for palavra in simbolos_aux:
        if palavra == simbolo:
            return cont
        cont += 1


# Chamando os métodos
procura_palavras_reservadas(tokens)
procura_comentarios(tokens)
procura_identificadores_e_numeros(tokens)
procura_erros()
mostrar_informacaos(tokens, "Tokens de Entrada:", 0)
mostrar_informacaos(simbolos, "Tabela de Símbolos:", 1)
mostrar_informacaos(erros, "Erros nas linhas:", 2)
