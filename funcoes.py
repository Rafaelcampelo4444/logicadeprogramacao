#FUNÇÃO PARA MOSTRAR PARA O USUARIO AS OPÇÕES DE MADEIRA DISPONIVEL E PERGUNTAR QUAL TIPO DESEJA
#RETORNAR VALOR DA MADEIRA DEPENDENDO DE QUAL FOR SELECIONADA
def escolha_tipo ():
    #mostra a opção de madeira disponivel e pergunta e valida qual deseja.
    print('Entre com o tipo de madeira que você quer:')
    print('PIN - Tora de Pinho')
    print('PER - Tora de peroba')
    print('MOG - Tora de mogno')
    print('IPE - Tora de ipê')
    print('IMB - Tora de imbuia')
    madeira=input('>> (PIN/ PER / MOG / IPE / IMB):  ')
    while True:
        if madeira not in ['PIN','PER','MOG','IPE','IMB']:
            print('Entre com o tipo de madeira que você quer:')
            print('PIN - Tora de Pinho')
            print('PER - Tora de peroba')
            print('MOG - Tora de mogno')
            print('IPE - Tora de ipê')
            print('IMB - Tora de imbuia')
            print('Tipo de madeira invalida')
            madeira=input('>> (PIN/ PER / MOG / IPE / IMB):  ')
        else:
            break

    preco=00.00
   
    #preço de cada tipo de madeira
    if madeira == 'PIN':
        preco=150.40
    elif madeira == 'PER':
        preco= 170.20
    elif madeira == 'MOG':
        preco= 190.90
    elif madeira == 'IPE':
        preco= 210.10
    else:
        preco=220.70
    
    return preco


    
#Pergunta a quantidade de toras
#Retorna a quantidade de toras e o valor com o desconto aplicado.
def qtd_toras():

    preco=escolha_tipo()

#perguntar e valida quantas toras o usuario deseja
    while True:
             
        try:
            ntoras=int (input('Quantas toras você quer em m³ : '))
            
            
        except ValueError:
            print('Digite um caractere valido !')
            continue

        if ntoras > 2000:
            print('Por favor, digite uma quantidade que não ultrapasse 2000 toras.')
            continue
        else:
            break
#calcula o valor final levando em consideração o tipo de madeira, a quantidade e as regras de desconto dependendo da quantidade

    if ntoras < 100:
        depois_desconto=preco * ntoras
    elif ntoras >= 100 and ntoras < 500:
        desconto= (ntoras * preco * 4) / 100
        depois_desconto= (ntoras * preco) - desconto
    elif ntoras >= 500 and ntoras < 1000 :
        desconto= (ntoras * preco * 9) / 100
        depois_desconto= (ntoras * preco) - desconto
    else:
        desconto= (ntoras * preco * 16) / 100
        depois_desconto= (ntoras * preco) - desconto
            
        
    return depois_desconto


#Perguntar pelo serviço adicional de trasporte
#retornar apenas 1 das opções de trasporte 1 ,2 e 3
def transporte():
    print('Escolha o tipo de transporte de acordo com seu numero:')
    print('1 - Transporte Rodoviario - R$ 1000.00')
    print('2 - Transporte Ferroviário - R$ 2000.00')
    print('3 - Transporte Hidroviário - R$ 2500.00')
    t=input('>> ( 1, 2 ou 3 )')
#pergunta e valida o tipo de transporte que o usuario quer.
    while True:
        if t  not in ['1','2','3']:
            print ('tipo de trasporte invalido, digite 1, 2 ou 3')
            t=input('>>')
        else:
            break
    
    if t == '1': 
        valor_trasporte=1000.00
    elif t == '2':
        valor_trasporte=2000.00
    else:
        valor_trasporte=2500.00
        
    
    return valor_trasporte
