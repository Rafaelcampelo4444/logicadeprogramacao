import copy
#print de boas vindas ao programa.(main)
print('Bem vindo a Lista de contatos do Rafael Campelo Ferreira')
#variaveis que vão ser usadas ao longo do programa (main)
boa= ('Bem vindo a Lista de contatos do Rafael Campelo Ferreira')
traco=len(boa)
id_global=5583997
proximo_id=0
#lista que vai ser usada nas 3 funções presentes no codigo. (main)
lista_contatos=[]




#função cadastro contato
def cadastrar_contato(id):
    print(20 * '-' + ' Menu de cadastro ' + '-'* 20)
   
    #entrada de dados para o cadastro do usuario na lista_contatos 
    nome=input('Por favor entre com o nome do contato: ')
    atividade=input('Por favor entre com a atividade do contato: ')
    telefone=input('Por favor entre com telefone do contato: ')
    
    #dicionario que vai ser colocado dentro de lista_contatos dependendo do que o usuario preencher anteriormente em nome, atividade e telefone
    dados={

        "id_global":id,
        "r_nome": nome,
        "r_atividade": atividade,
        "r_telefone": telefone,
        }
    #parte que vai copiar dados preenchidos para a lista_contatos
    lista_contatos.append(dados.copy())
#função para consultar contatos que estão armazenados na lista_contatos
def consultar_contato():  
   
#apresentação de opções disponiveis
    print('Escolha a opção desejada: ')   
    print('1 - Consultar todos' )
    print('2 - Consultar por ID' )
    print('3 - Consultar Consultar por setor' )
    print('4 - Retornar ao Menu' )
    r_menu=input('>>')
    
    #condição implementada dependendo do que o usuario vai preencher em input
    #menu 1 dentro de consultar contatos
    if r_menu == '1':
        print('-' * 12)
        #Faz a leitura dos elementos da lista e printa na tela
        for contato in lista_contatos:
            print(f"id: {contato['id_global']}")
            print(f"nome: {contato['r_nome']}")
            print(f"atividade: {contato['r_atividade']}")
            print(f"telefone: {contato['r_telefone']}")

            print('-' * 12)
    
    #Consulta de informações só que levando em consideração o ID da pessoa
    #menu 1 dentro de consultar contatos
    #validação de dados para garantir que o usuario informe apenas numeros
    elif r_menu == '2':
        try:
            id_busca = int(input('Informe o ID do contato: '))
        
        except ValueError:
            print('ID inválido. Use apenas números.')
            return
    #busca na lista levando em consideração o que foi preenchido no input id_busca
        encontrado = None
        for contato in lista_contatos:
            if contato["id_global"] == id_busca:
                encontrado = contato
                break
    #Se for encontrado o elemento encontrado na lista vai ser executado esse if abaixo e vai ser exibida as informações do usuario conforme foi preenchido seu id
    #E caso não obedeça o if  vai ser exibida a mensagem que o contato não foi encontrado 
        if encontrado:
            print('-' * 12)
            print(f"id: {encontrado['id_global']}")
            print(f"nome: {encontrado['r_nome']}")
            print(f"atividade: {encontrado['r_atividade']}")
            print(f"telefone: {encontrado['r_telefone']}")
            print('-' * 12)
        else:
            print("Contato não encontrado.")

    #consulta por profissão 
    elif r_menu == '3':
        #Usuario vai preencher a atividade que vai ser buscada
        atividade_busca = input("Informe a atividade/profissão: ").strip().lower()
        #Aqui é feita varredura na lista para ver se o que foi preenchido vai ser encontrado
        encontrados_atividade = []
        for contato in lista_contatos:
            if contato["r_atividade"].lower() == atividade_busca:
                encontrados_atividade.append(contato)
        #E então se o que foi preenchido for encontrado vai ser executado os prints com as informações dos usuarios que estão relacionados a aquela atividade
        if encontrados_atividade:
            print('-' * 12)
            for contato in encontrados_atividade:
                print(f"id: {contato['id_global']}")
                print(f"nome: {contato['r_nome']}")
                print(f"atividade: {contato['r_atividade']}")
                print(f"telefone: {contato['r_telefone']}\n")
                print('-' * 12)
        #caso não seja encontrado vai ser executado esse print e vai retornar ao menu principal    
        else:
            print("Nenhum contato encontrado para essa atividade.")

#função para remover usuario
def remover_contato():
    # busca na lista levando em consideração o que foi preenchido no input id_busca_id
    # e também vai ser validado se o que apessoapreencheu e um numero se não for vai dar id invalido e vai perguntar novamente
    try:
            id_busca_id = int(input('Digite o ID do contato que você dedeja remover: '))
        
    except ValueError:
            print('ID inválido. Use apenas números: ')
            return
    #Aqui é buscado o dicionario que tem id_global igual ao que foi preenchido anteriormente nessa função
    encontrado = None
    for contato in lista_contatos:
        if contato["id_global"] == id_busca_id:
            encontrado = contato
            break
    #se for encontrado vai remover ele agora se não for vai dar a mensagem que não foi encontrado.
    if encontrado:
        lista_contatos.remove(encontrado)
        print(f"Contato com ID {id_busca_id} removido com sucesso!")
    else:
        print(f"Nenhum contato encontrado com o ID {id_busca_id}.")
        

#Codigo principal (main)
#laço para que o usuario seja forçado a digitar somente as opções 1,2,3 e 4.
while True:
    print (traco * '-')
    print(20 * '-' + ' Menu Principal ' + '-'* 20)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato(S)')
    print('3 - Remover Contato')
    print('4 - Sair')
    
    m_principal=input('>>')
    
            
    #condições que vão acontecer dependendo do que o usuario preencher em m_principal (dependendo do que for preenchido o menu vai te direcionar para uma função).
    if m_principal == '1':
       novo_id = id_global + proximo_id
       cadastrar_contato(novo_id)
       proximo_id += 1
    elif m_principal == '2':
        consultar_contato()

    elif m_principal == '3':
        remover_contato()
                
    elif m_principal == '4':
        print('você encerrou o programa')
        break
    else:
        print('Opção invalida, tente novamente !')
