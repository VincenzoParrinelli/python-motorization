from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from read_excel import read_excel
from window import main_window

##main_window()

sheet = read_excel()

for i in range(22):
    
    val = sheet.cell(i + 10, 7).value
        
    print(val)
        

input("Premere invio per chiudere il programma...")

# driver = webdriver.Firefox()

# driver.get("https://google.it")

# driver.find_element(By.CLASS_NAME, "QS5gu.sy4vM").click()

# google_input = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")

# google_input.send_keys("Zafa Puppo" + Keys.ENTER)
