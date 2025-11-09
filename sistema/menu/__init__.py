from sistema.menu.uteis import*
from sistema.gerenciador_classe import*


def menu(lista):
    ''' Função para criar menu 
    arg: lista
    return: opção da lista selecionada'''

    cabecalho('FINANCEIRO')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m) \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaint('\033[32mOPÇÃO: \033[m')
    return opc

def registration_entry():

    cabecalho('ENTRADA')
    
    tipo = input("TIPO FIXA/VARIAVEL: ")
    data = input("DATA DD/MM/AAAA: ")
    fonte = input("FONTE: ")
    valor = input("VALOR: R$")

    return entry(tipo, data, fonte, valor)

def exit_registration():

    cabecalho('SAIDA')

    tipo = input("TIPO FIXA/VARIAVEL: ")
    data = input("DATA DD/MM/AAAA: ")
    metodo = input("METODO: ")
    status = input("STATUS: ")
    fonte = input("FONTE: ")
    valor = input("VALOR: R$")

    return exit(tipo, data, metodo, status, fonte, valor)



    



    