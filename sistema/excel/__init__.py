import pandas as pd 
import os 


def salvarINexcel(lista, file, txt):

    if not lista:
        print("Nenhum dado para salvar")
        return
    
    df = pd.DataFrame(lista)

    if os.path.exists(file):
        df_existente = pd.read_excel(file)
        df = pd.concat([df_existente, df], ignore_index=True)
    
    df.to_excel(file, index=False)
    print(f"{txt}: Salvo com sucesso")


