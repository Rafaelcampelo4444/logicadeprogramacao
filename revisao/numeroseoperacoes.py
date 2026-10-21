#print(2 * (4+4)/8)

    #Divisão com numero inteiro
#print(4//2)

    #calculos atribuindo variaveis

#b=6

#print((a+b) // 2)

    #resto de uma divisão

#print (5 % 2)

    # Aproveitar o valor da ultima operação

#preco = 10 + 10
#total = 10 * preco

#print(10 + total)

    #Exemplos de texto

#print('teste "teste" teste')

#quebra de linhas

#print("primeiralinha\nsegundalinha")

#para não serem interpretados como caracteres especiais como no exemplo anterior

#print (r'primeiralinha\segundalinha')

#alternativa para realizar a quebra de linha 

#print("""\
#linha1
#linha2
#linha3 """)

#repetição de string

#exemplo1
#print( "-" * 3)

#exemplo2
#numero ='rato'
#print(numero * 3)

#contatenar string com variável.
#print (numero + 'string')

#que letra está na posição x ?
#para ver a posição ao contraria basta clocar o sinal de negativo [-1]
#palavra = 'python' 
#print(palavra[1])

# caracteres da posição 2 (incluída) até 5 (excluída)

#print('paralelepipedo'[2:5])

# caracteres do início até a posição 2 (excluída) 
#print("paralelepipedo"[:2])
# caracteres da posição 4 (incluída) até o fim
#print('paralelepipedo'[4:])
# caracteres da penúltima (incluída) até o fim
#print('paralelepipedo'[-3:])

#Outro exemplo só que contendo soma
#print ('testeposição'[:5] + 'testedeposicao'[7:])


#alterando uma string

#palavra = 't' + palavra[1:]
#print (palavra)

#contagem decaracteres

#contagem = 'python'
#print(len(contagem))

#listas

#lista1 = ['um', 'dois', 'três']

#print(lista1)

#Nas listas também existeem posicionamento dos elementos presentes nela 

#print (lista1[1])

#concatenação de listas 

#lista2 = [1,2,3,4]
#lista3 = [5,6,7,8]

#print (lista2 + lista3)

#alteração de elementos em uma lista

#listaelementos = ['agua', 'vento', 'fogo']

#listaelementos[1] = 'terra'
#print (listaelementos)

#ter como resultado um numero que é outro só que ao cubo, e ver quanto outro numero daria sendo elevado ao cubo

#calculoaocubo = [1,2,3,4,5]

#calculoaocubo.append ()
#calculoaocubo.append (10**3)

#print(calculoaocubo)

#cachorro = ['pastoralemao', 'pincher', 'golden' ]

#raça = cachorro

#print(id(raça) == id(cachorro))

#print (raça)

#cachorro.append('caramelo')

#print (raça)

#manipulando listas

#substituindo elementos

#numeros = [1,2,3,4,5,6,7,8]

#numeros [1:4] = [0,0,0]

#print (numeros)

#removendo numeros especificos

#numeros [1:4] = []
#print (numeros)

#limpar lista

#numeros[:] = []
#print(numeros)

#listando itens da lista
#animais = ['cachorro', 'gato', 'rato']
#for animal in animais:
#    print (animal)

for animal in "cachorro":
    print(animal)