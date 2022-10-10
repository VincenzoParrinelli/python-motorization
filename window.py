import tkinter as tk
from tkinter.filedialog import askopenfile
from selenium_utils import open_website, read_excel

def open_window():
        
    root = tk.Tk()
    
    canvas = tk.Canvas(root, width=500, height=350)
    
    canvas.grid(columnspan=3, rowspan=12)
    
    text = tk.Label(root, text="Seleziona un file excel da analizzare", font=("Arial", 16))
    
    text.grid(column=1, row=4)
    
    select_file_button = tk.Button(root, text="Apri il sito", command=lambda:open_website())
    
    select_file_button.grid(column=1, row=5)
    
    read_excel_button = tk.Button(root, text="Seleziona file...", bg="#FF2D00", command=lambda:select_excel(root))
    
    read_excel_button.grid(column=2, row=5)
    
    #*********INSERIRE CONTROLLO PAGINA TRAMITE URL
    start_button = tk.Button(root, text="Avvia automazione", command=lambda:read_excel())
    
    start_button.grid(column=3, row=5)
    
    root.mainloop()

 
        
def select_excel(root):
                
    file = askopenfile(parent=root, mode="rb", filetype=[("xlsx file", "*.xlsx")])
    
    if file:
         
        text_box = tk.Label(root, width=60, height=1, text=f"File selezionato: {file.name}")
        
        text_box.grid(column=1, row=7)

    
