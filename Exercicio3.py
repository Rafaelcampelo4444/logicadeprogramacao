print('Bem vindo a Madereira do Rafael Campelo Ferreira')
# FUNÇÕES PRESENTES NO ARQUIVO funcoes.py
from funcoes import escolha_tipo
from funcoes import qtd_toras
from funcoes import transporte

escolha_tipo

#identificação de cada função
qtd=qtd_toras()
trasporte=transporte()
#variavel e preint do valor final a ser pago
soma_tudo= trasporte + qtd

print (f'valor final a ser pago: {soma_tudo} R$')
