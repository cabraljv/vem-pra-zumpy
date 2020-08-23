'''
    Linguagem: Python 3

    Autor: João Victor Cabral

    Exercício: Dependências Transitivas

    Estratégia:
        Primeiramente tive que receber do usuário o numero de classes a serem inseridas, após isso fui lendo as 
        dependências de cada classe e as dependências de suas dependências para adicionar no seu determinado array,
        por ultimo tive que verificar todas as outras classes e atualizar suas dependências, caso dependessem da 
        classe atual 

'''


n = int(input())
classes = {}


for i in range(n):
    linha = input().split()
    
    classe_atual = linha.pop(0); # Classe atual (primeiro elemento do array)
    
    dep_atuais = set(linha) # Dependências da classe atual
    
    # Primeiramente temos que adicionar as dependências das 
    # dependências atuais caso alguma dependência ja exista 
    # nas classes
    for j in linha:
        if j in classes:
            dep_atuais = set(list(dep_atuais) + list(classes[j]))
    
    # Setado o set das dependências da dependência atual
    # o "set" é uma uma list que não permite elementos 
    # duplicados por isso o utilizamos
    classes[classe_atual] = set(dep_atuais)

    # Depois disso temos que adicionar as dependências da 
    # classe atual em todas as classes que dependem dela
    for j in classes:
        if classe_atual in classes[j]:
           classes[j] = set(list(classes[j])+ list(classes[classe_atual]))


# Print resultado
print('')
for i in classes:
    print(i, end=' ')
    classes[i] = sorted(classes[i]) # Ordenando set
    for j in classes[i]:
        print(' '+j,end='')
    print('')
