import tkinter as tk
from tkinter.filedialog import askopenfile
from selenium_utils import open_website, automate

root = tk.Tk()

class Window:
    
    def __init__(self, master) :
        
        self.master = master
        
        canvas = tk.Canvas(master, width=500, height=350)
    
        canvas.grid(columnspan=3, rowspan=12)
    
        text = tk.Label(master, text="Seleziona un file excel da analizzare", font=("Arial", 16))
    
        text.grid(column=1, row=4)
        
        self.select_file_button = tk.Button(master, text="Apri il sito", command=lambda:open_website())
    
        self.select_file_button.grid(column=1, row=5)
    
        self.read_excel_button = tk.Button(master, text="Seleziona file...", bg="#FF2D00", command=lambda:self.select_excel())
    
        self.read_excel_button.grid(column=2, row=5)
    
        #*********INSERIRE CONTROLLO PAGINA TRAMITE URL
        self.start_button = tk.Button(master, text="Avvia automazione", command=lambda:automate(self))
    
        self.start_button.grid(column=3, row=5)
        
        
    def select_excel(self):
                
        self.file = askopenfile(parent=self.master, mode="rb", filetype=[("xlsx file", "*.xlsx")])
    
        if self.file:
         
            text_box = tk.Label(root, width=60, height=1, text=f"File selezionato: {self.file.name}")
        
            text_box.grid(column=1, row=7)
            
            
    def no_file_error():
        
        text_box = tk.Label(root, width=60, height=1, text="Errore! Nessun file selezionato")
        
        text_box.grid(column=1, row=8)

mainWindow = Window(root)    
    
root.mainloop()

      

    
