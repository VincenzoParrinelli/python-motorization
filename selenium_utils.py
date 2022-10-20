import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
    
    for i in range(len(df)):
      
        marca_operativa = df.iloc[i, 0]
        ora_esame = df.iloc[i, 1]
        
        # se il valore è nan ritorna dalla funzione
        if pd.isnull(marca_operativa):
            return
        
        insert_candidate(marca_operativa, ora_esame)
        

#***********INSERIRE EXPLICIT WAIT (WebDriverWait, expected_conditions)************
#***********CONTROLLO ERROR VIEW SECONDA TAB ************
def insert_candidate(marca_operativa, ora_esame):
    
    marca_operativa_input = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "Read_initAction_richiestaView_richiestaFrom_marcaOperativa"))) 
    
    # inserisci marca operativa e premi invio
    marca_operativa_input.send_keys(marca_operativa, Keys.ENTER)
    
    # se il messaggio di errore è presente torna indietro ed elabora un'altra marca operativa
    try:
        
        WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div")))
        
        driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
        
        print("errore", f"{marca_operativa}\n")
    
    except:
        
        try:

            WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "/html/body/h1"))) 
            
            driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
            
            print(f"Internal Server Error\n")
            
        except:
        
            # prendi prima lettera del cognome     
            cognome_input = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "Read_paging_richiestaView_cognome"))) 
        
            cognome = cognome_input.get_attribute("value")
        
            print(f"{cognome}\n")
        
            # prendi codice statino 
            codice_statino_input = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "Read_paging_richiestaView_richiestaFrom_numeroFRToView")))
        
            codice_statino = codice_statino_input.get_attribute("value")
            
            print(f"{codice_statino}\n") 
            
            # spostati nell'altra tab******
            driver.switch_to.window(driver.window_handles[1])
            
            # se il messaggio di errore è presente torna indietro ed elabora un'altra marca operativa
            # try:
                
            #     WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div")))
                
            #     indietro_btn = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_button_value_backFromNew")))
                
            #     indietro_btn.click()
                
            #     driver.switch_to.window(driver.window_handles[0])
            
          
            nuovo_candidato_button = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DettaglioDisponibilitaSessioneEsameEP_button_value_newCandidato"))) 
            
            nuovo_candidato_button.click()
            
            # inserisci codice statino nell'input
            disponibilita_sessione_esame_input_codice_statino = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_disponibilitaSessioneEsameEPView_prenotazioneCandidatoEP_theRichiestaEmissioneDocumentoAbilitazioneEP_codiceFoglioRosa"))) 
            
            disponibilita_sessione_esame_input_codice_statino.send_keys(codice_statino)
            
            # inserisci cognome nell'input
            disponibilita_sessione_esame_input_cognome = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_disponibilitaSessioneEsameEPView_prenotazioneCandidatoEP_theRichiestaEmissioneDocumentoAbilitazioneEP_thePersonaFisica_descrizioneCognomePersonaFisica")))
        
            disponibilita_sessione_esame_input_cognome.send_keys(cognome[0])
            
            # seleziona turno in base all'ora esame
            turno_esaminatore_select_button = Select(WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_disponibilitaSessioneEsameEPView_prenotazioneCandidatoEP_turnoEsaminatore"))))
            #fascia_oraria_selected_text = Select(driver.find_element(By.ID, "DisponibilitaSessioneEsameEP_disponibilitaSessioneEsameEPView_disponibilitaSessioneEsameEPFrom_theDisponibilitaEsaminatoreEP_indicatoreFasciaOrariaEsaminatore")).first_selected_option
            
            if ora_esame == 8 or ora_esame == 14:
                
                turno_esaminatore_select_button.select_by_value("1")
            
            elif ora_esame == 9 or ora_esame == 15:
                
                turno_esaminatore_select_button.select_by_value("2")
                
            elif ora_esame == 10:
                
                turno_esaminatore_select_button.select_by_value("3")
                
            elif ora_esame == 11:
                
                turno_esaminatore_select_button.select_by_value("4")  
            
            elif ora_esame == 12:
                
                turno_esaminatore_select_button.select_by_value("5")  
            
            elif ora_esame == 13:
                
                turno_esaminatore_select_button.select_by_value("6")  
                

            conferma_button = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_button_value_conferma")))  
            
            conferma_button.click() 
            
            try:
                WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.CLASS_NAME, "errori")))
                
                indietro_btn = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_button_value_backFromNew")))
                
                indietro_btn.click()
                
                driver.switch_to.window(driver.window_handles[0])
                
                driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca") 
                
            except:
                
                indietro_button = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.ID, "DisponibilitaSessioneEsameEP_button_value_undoFromDelete")))
                
                indietro_button.click()
                
                driver.switch_to.window(driver.window_handles[0])
            
                # vai alla pagina precedente dopo aver elaborato i dati
                driver.get("https://www.ilportaledellautomobilista.it/RichiestaPatenti/richiesta/Read_initAction.action?pageStatus=SEARCH&MENU=Ricerca")
            
        
   
   
     
    #wait.until(ec.text_to_be_present_in_element((By.XPATH, "/html/body/h1", text="")))
  
    #error = driver.find_element(By.XPATH, "/html/body/h1").get_attribute("Internal Server Error")
    

            