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
 O método salva_comentario, recebe a posição que o comentario está no arquivo
e salva no dicionário(lista) de tokens.
"""
def salva_comentario(posicao):
    tokens.update({posicao: "COMENTÁRIO"})


"""
 O método salva_palavras_reservadas, recebe a posição e a palavra reservada e 
salva o conteúdo no dicionário(lista) de tokens.
"""
def salva_palavras_reservadas(posicao, palavra):
    tokens.update({posicao: f"{palavra.upper()}"})


"""
O método é responsavél de encontrar os tokens existentes no arquivo,
ele percorre o arquivo verificando linha por linha, e toda vez que encontra
algum token, ele verifica se aquele token já existe,
chamando o método valida_simbolos(), que retorna a posição do token na tabela de simbolos.
Salvando o token, a posição e a qual dos simbolos ele faz referencia
"""
def procura_tokens():
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

            if linha_atual.startswith(" "): # verifica se começa com espaço em branco e pula a linha.
                salva_erro(cont, linha_atual)
                encontrou = True  # quando encontrou recebe True, ele não entra em nenhuma das condicionais de verificação.

            if linha_atual.startswith("//"): # verifica se é um comentario
                salva_comentario(cont)
                encontrou = True

            for palavra in palavras_reservadas: # verifica se é uma palavra reservada
                if palavra == linha_atual:
                    salva_palavras_reservadas(cont, linha_atual)
                    encontrou = True

            if linha_atual.isalnum() and encontrou == False: # verifica se a linha é alfanúmerica
                for letra in alfabeto: # percorre posição por posição da linha
                    if linha_atual[0] == letra or linha_atual[0] == letra.upper(): # verifica se a primeira linha é uma letra maiuscula ou minuscula.
                        ident = valida_simbolos(linha_atual, cont) # pega a posição na tabela de simbolos
                        tokens.update({cont: f"IDENTIFICADOR {ident}"}) # salva a informação
                        encontrou = True
            if linha_atual.isnumeric() and encontrou == False: # verifica se é um número
                if int(linha_atual) <= 99 and len(linha_atual) <= 2: # se o número tem duas casa decimais e é menor ou igual a 99
                    ident = valida_simbolos(linha_atual, cont) # pega a posição na tabela de simbolos
                    tokens.update({cont: f"NÚMERO INTEIRO {ident}"}) # salva a informação
                    encontrou = True
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
                    if encontrou == False:
                        salva_erro(cont, linha_atual)
            if encontrou == False:
                salva_erro(cont, linha_atual)
            encontrou = False


"""
 O método salva_erro, recebe a posição e informação da linha e 
salva o conteúdo no dicionário(lista) de erros.
"""
def salva_erro(posicao, palavra):
    erros.update({posicao: f"{palavra}"})


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
procura_tokens()
mostrar_informacaos(tokens, "Tokens de Entrada:", 0)
mostrar_informacaos(simbolos, "Tabela de Símbolos:", 1)
mostrar_informacaos(erros, "Erros nas linhas:", 2)
