from sistema.menu import*
from sistema.gerenciador_classe import*
from sistema.excel import*


entrada = []
saida = []
fileentrada = "entry.xlsx"
filesaida = "exit.xlsx"

while True:

    fuc = ["ENTRADA | RECEITAS",
       "SAIDA",
       "RELATORIO",
       "SAIR"]
    opc = menu(fuc)


    
    match opc:
        
        case 1:
            #menu de cadastro entrada
            new_entry = registration_entry()
            entrada.append(new_entry.to_dict())
            salvarINexcel(entrada, fileentrada, "ENTRADA")
            entrada.clear()
        case 2:
            #menu de cadastro saida
            new_exit = exit_registration()
            saida.append(new_exit.to_dict())
            salvarINexcel(saida, filesaida, "SAIDA")
            saida.clear()
        case 3:
            #menu de relatorio
            pass
        case 4:
            break



    



    




