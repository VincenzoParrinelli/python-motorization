from traceback import print_tb
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

def open_website():
    
    driver.get("https://www.ilportaledellautomobilista.it/web/portale-automobilista/loginspid")


def automate(self):
    
    # try(a):   
    #     pass
    
    # if self.file:
    #     print("aasasa")
 
    df = pd.read_excel(self.file, usecols="G,J", skiprows=range(0,8))
    
    driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
    
    driver.implicitly_wait(3) 
    
    for i in range(len(df)):
      
        marca_operativa = df.iloc[i, 0]
        ora_esame = df.iloc[i, 1]
        
        # se il valore è nan ritorna dalla funzione
        if pd.isnull(marca_operativa):
            return
        
        driver.implicitly_wait(2)
        
        insert_candidate(marca_operativa, ora_esame)
        

def insert_candidate(marca_operativa, ora_esame):
    
    marca_operativa_input = driver.find_element(By.ID, "Read_initAction_richiestaView_richiestaFrom_marcaOperativa") 
    
    # inserisci marca operativa e premi invio
    marca_operativa_input.send_keys(marca_operativa, Keys.ENTER)
    
    # se è presente un errore non elaborare la richiesta
    
    try:
        #error dialog box
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div")
        
        driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
        
        print("errore", marca_operativa)
        
    except:
        
        # prendi prima lettera del cognome     
        cognome_input = driver.find_element(By.ID, "Read_paging_richiestaView_cognome") 
    
        cognome = cognome_input.get_attribute("value")
    
        print(cognome)
    
        # prendi codice statino 
        codice_statino_input = driver.find_element(By.ID, "Read_paging_richiestaView_richiestaFrom_numeroFRToView") 
    
        codice_statino = codice_statino_input.get_attribute("value")
    
        print(codice_statino) 
    
        # vai alla pagina precedente dopo aver preso i dati
        driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
       
        
   
   

    

            