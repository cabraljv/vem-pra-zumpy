'''
    Linguagem: Python 3

    Autor: João Victor Cabral

    Exercício: Contando as letras dos números

    Estratégia:
        Através de um laço eu percorri todos os mil números, buscando a quantidade de letras de cada um. Criando 
        arrays com a quantidade de letras dos números mais simples foi fácil determinar o número de letras dos mais
        complexos, apesar de ocorrerem algumas quebras de padrões como a primeira dezena (onze, doze...) eu apenas tive
        que tratá-las
'''



# Quantidade de letras das unidades (um, dois, tres...)
unidades = [2,4,4,6,5,4,4,4,4,3] 

#Quantidade de letras da primeira dezena (onze,doze...)
primeira_dezena = [4,4,5,8,6,9,9,7,8,5]

#Quantidade de letras das dezenas (dez, vinte ...)
dezenas = [3,5,6,8,9,8,7,7,7,3]

#Quantidade de letras das centenas
centenas = [5,8,9,12,10,10,10,10,10,3]

total = 0

#Percorrendo os números de um a mil
for i in range(1,1001):

    letras_num=0 # Letras desse determinado número

    # Primeiros cem números
    if i-100<0:

        # Primeiras unidades
        if i-10<=0:
            letras_num+=unidades[i-1]

        # Primeiras primeira dezena(possui um padrao diferente ex: onze, doze...)
        elif i-20<=0:
            letras_num+=primeira_dezena[i-11]

        # Numero com mais de duas dezenas
        else:

            # Dezena redonda (vinte, trinta...)
            if i%10==0:
                letras_num+=dezenas[int((i/10))-1]
            # Dezena com unidade (vinte e um, trinta e cinco...)
            else:
                letras_num+=dezenas[int((i/10))-1]+unidades[i%10-1]+1

    # Número com mais de uma centena
    else:

        # O número "cem" tem uma escrita fora do padrão por isso tem que ser tratado separadamente
        if i==100:
            letras_num+=3
        else:
            # Números com centenas arredondadas (duzentos, trezentos...)
            if i%100==0:
                letras_num+=centenas[int(i/100)-1]
            else:
                 # Números com centenas e unidades apenas (cento e cinco, duzentos e sete...)
                if (i%100)-10<=0:
                    letras_num+=centenas[int(i/100)-1]+unidades[(i%100)-1]+1

                # Números com centenas e a primeira dezena (cento e onze, trezentos e quinze...)
                elif (i%100)-20<=0:
                    letras_num+=centenas[int(i/100)-1]+primeira_dezena[(i%100)-11]+1

                # Números com centena e dezena
                else:
                    # Números com centena e dezena arredondados
                    if (i%100)%10==0:
                        letras_num+=centenas[int(i/100)-1]+dezenas[int((i%100)/10)-1]+1

                    # Números com centena, dezena e unidade (quinhentos e cinquenta e quatro, cento e vinte e três...)
                    else:
                        letras_num+=centenas[int(i/100)-1]+dezenas[int((i%100)/10)-1]+unidades[(i%100)%10-1]+2
    total+=letras_num

print(total)
