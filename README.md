# Analisador Lexico em Python

Este autômato foi implementado utilizando a linguagem Python e tem como objetivo ler um arquivo .txt, realizar a separação dos tokens, criar uma tabela de símbolos e listar os erros, ali existentes.

## Tokens

O autômato foi programadp para reconhecer linguagens cujos tokens podem ser:
- Identificadores iniciados por uma letra, podendo possuir na sequência números e/ou letras.
- Constantes numéricas formadas por um ou mais números inteiros na casa da dezena, ou
seja, até o valor 99.
- Constantes numéricas formadas por números reais, também na casa da dezena, ou seja,
valor máximo de 99.99 (identificadas pelo ponto). Sempre com duas casas decimais.
- Identificadores no formato de comentários de linha, padrão da Linguagem C (//).
- As palavras reservadas da linguagem C: int, double, float, real, break, case,
char, const, continue.

## Padrão do arquivo aceito

O analisador carrega o arquivo-texto contendo um padrão por linha e reconhece o
token especificado.

## O que ele exibe?

Ao final da análise, o autômato exibe:
- Os tokens de entrada (e a linha onde eles aparecem – tabela léxica).
- A tabela de símbolos.
- A lista das linhas onde os erros aparecem (caso tenham erros no arquivo), bem como a
palavra, não sendo especificado qual erro.
