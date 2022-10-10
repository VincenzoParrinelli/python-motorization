from lib2to3.pgen2 import driver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

def open_website():
    
    driver.get("https://www.ilportaledellautomobilista.it/web/portale-automobilista/loginspid")


def read_excel():
    
    df = pd.read_excel("items.xlsx", usecols="G,J", skiprows=range(0,8))
    
    driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
    
    for i in range(len(df)):
      
        marca_operativa = df.iloc[i, 0]
        ora_esame = df.iloc[i, 1]
        
        # se il valore è nan ritorna dalla funzione
        if pd.isnull(marca_operativa):
            return
        
        insert_candidate(marca_operativa, ora_esame)
        

def insert_candidate(marca_operativa, ora_esame):
    
    time.sleep(2)
    
    marca_operativa_input = driver.find_element(By.ID, "Read_initAction_richiestaView_richiestaFrom_marcaOperativa") 
    
    # inserisci marca operativa e premi invio
    marca_operativa_input.send_keys(marca_operativa, Keys.ENTER)
    
    # prendi prima lettera del cognome     
    cognome_input = driver.find_element(By.ID, "Read_paging_richiestaView_cognome") 
    
    cognome = cognome_input.get_attribute("value")
    
    print(cognome)
    
    # prendi codice statino 
    codice_statino_input = driver.find_element(By.ID, "Read_paging_richiestaView_richiestaFrom_numeroFRToView") 
    
    codice_statino = codice_statino_input.get_attribute("value")
    
    print(codice_statino) 
    
    # vai alla pagina precedente dopo aver preso i dati
    driver.back()
    
       
        
   
   

    

            