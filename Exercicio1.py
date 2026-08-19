# Texto de boas vindas ao usuario.  

print('Seja bem vindo ao sistema de Rafael Campelo Ferreira. ')   
print(53 * '-')   

 #Entrada de dados do cliente (Valor Base e porcentagem (idade))   

valor_base = float(input('Informe o valor Base do plano : R$ ')) 
Idade = float(input('Informe a idade do cliente :'))   

 #Calculo para obter o valor final do plano baseado na idade do cliente 

if Idade >= 0 and Idade < 19:   
    valor_final = (valor_base * 100) / 100 

elif Idade >= 19 and Idade < 29 :   
    valor_final = (valor_base * 150) / 100   

elif Idade >= 29 and Idade < 39 :   
    valor_final = (valor_base * 225) / 100  

elif Idade >= 39 and Idade < 49 :   
    valor_final = (valor_base * 240) / 100  

elif Idade >= 49 and Idade < 59 :   
    valor_final = (valor_base * 350) / 100 

else: 
    valor_final = (valor_base * 600) / 100 

 
#resultado final (mensal) dos calculos 

        
print(f'O valor mensal do plano é de: R$ {valor_final} ') 
