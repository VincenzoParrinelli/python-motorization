import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def open_website():
    driver = webdriver.Firefox()
    
    driver.get("https://www.ilportaledellautomobilista.it/web/portale-automobilista/loginspid")



def read_excel_and_insert_candidates():
    
    df = pd.read_excel("items.xlsx", usecols="G,J", skiprows=range(0,8))
    
    for i in range(len(df)):
      
        marca_operativa = df.iloc[i, 0]
        ora_esame = df.iloc[i, 1]
        
        # if there is a nan value exit from the program
        if pd.isnull(marca_operativa):
            return
        
        #automazione()
        

#def automazione()        
            
        
   
   

    

            