from openpyxl import load_workbook

def read_excel():
    
    wb = load_workbook("items.xlsx", data_only=True)
    sheet = wb["ELENCO CANDIDATI SEDUTA"]
    
    return sheet
    

        
    
   



 


    
  

