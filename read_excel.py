import pandas as pd

def read_excel():
    
    
    df = pd.read_excel("items.xlsx", usecols="G,J", skiprows=range(0,9))
    
    print(df)
    
    # wb = load_workbook("items.xlsx", data_only=True)
    # sheet = wb["ELENCO CANDIDATI SEDUTA"]
    
    # for i in range(22):
    
    #     marca_operativa = sheet.cell(i + 10, 7).value
        
    #     print(marca_operativa)
    

    

        
    
   



 


    
  

