#Parte de boas vindas ao programa  

print( '-'* 11 + ' Bem-vindo a pizzaria de Rafael Campelo Ferreira ' + '-' * 12)  
cardapio=print('-' * 30 + ' Cardápio ' + '-' * 32)  

#menu de opções do cardapio para ser apresentado para o cliente  
print(72 * '-')  

print("---"'|'  '   Tamanho    '  '|'  '    Pizza Salgada(PS)    ' '|' '    Pizza Doce (PD)    ' '|''---' )  
print("---"'|'  '      p       '  '|'  '        R$ 30.00         ' '|' '        R$ 34.00       ' '|''---' )  
print("---"'|'  '      M       '  '|'  '        R$ 45.00         ' '|' '        R$ 48.00       ' '|''---' )  
print("---"'|'  '      G       '  '|'  '        R$ 60.00         ' '|' '        R$ 66.00       ' '|''---' )  
print(72 * '-')  


# while que engloba a validação do sabor, do tamanho e se o usuario quer pedir mais alguma coisa.
total=0.0

#validação da resposta do usuario (sabor)
while True: 
        sabor=input('Digite o sabor desejado (PS/PD):')  
        while True: 
            if(sabor not in ['PS','PD','ps','pd']): 
                print('Sabor inválido. Tente novemente.') 

                sabor=input('Digite o sabor desejado (PS/PD):')  
            else: 
                break 
        
    #validação da resposta do usuario (tamanho) 
    
        tamanho=input('Digite o tamanho desejado (P/M/G):')  
        while True: 
            if(tamanho not in ["P",'p','M','m','G','g'] ):
                print('Tamanho inválido. Tente novemente.') 

                tamanho=input('Tamanho invalido digite novamente(P/M/G):')  
            else: 
                break 
     
# Tabela de preços em formato de codigo para dar valor a cada tipo de combinação de sabor e tamanho de pizza para mais tarde ser feita a soma cumulativa dos itens e também ser apresentado o valor deles na confirmação de cada item.

        preco= 0.0

        if (tamanho in ['p','P']) and (sabor in ['ps','PS']): 
                preco += 30
        elif (tamanho in ['p','P']) and (sabor in ['pd','PD']) : 
                preco += 34

        elif (tamanho in ['M','m']) and (sabor in ['ps','PS']): 
                preco += 45 

        elif (tamanho in ['M','m']) and (sabor in ['pd','PD']): 
                preco += 48 

        elif (tamanho in ['g','G']) and (sabor in ['ps','PS']): 
                preco += 60 

        elif (tamanho in ['G','g']) and (sabor in ['pd','PD']): 
                preco += 66 
       
       #print para usuario ver o sabor e o tamanho da pizza que ele prediu
        
        if sabor in ['ps','PS']:
                print(f'Você comprou uma pizza salgada do tamanho {tamanho}: R$ {preco}')
        
        elif sabor in ['pd','PD']:
                print(f'Você comprou uma pizza doce do tamanho {tamanho}: R$ {preco}')
        
        else:
              break
               

#acumulador de valores
        total+=preco
        
        

#validação da resposta do usuario (adicionar mais pedidos)

        continuar=input('Deseja pedir mais alguma coisa? (S/N) : ')
    
        if continuar in ['S','s']: 
            continue
        
        else:
              break

#print do valor da soma de tudo que foi pedido. 
print(f'O valor total a ser pago: R$ {total}')
