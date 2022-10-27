#!/usr/bin/python3
from select import select
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from dotenv import load_dotenv
from selenium_utils import open_website, automate
import os
import random

load_dotenv()

class Window:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk(master)
        self.main_window.configure(
            cursor="arrow",
            height=300,
            relief="flat",
            width=400)
        self.frame1 = ttk.Frame(self.main_window)
        self.frame1.configure(height=300, width=400)
        self.login_label = tk.Label(self.frame1)
        self.login_label.configure(
            anchor="n",
            font="TkDefaultFont",
            justify="left",
            text='Password')
        self.login_label.place(anchor="center", x=120, y=150)
        self.password_entry = tk.Entry(self.frame1)
        self.password_to_string = tk.StringVar()
        self.password_entry.configure(
            borderwidth=0,
            justify="left",
            relief="flat",
            show="*",
            takefocus=False,
            textvariable=self.password_to_string)
        self.password_entry.place(anchor="center", x=220, y=150)
        self.password_entry.bind("<1>", self.callback, add="")
        self.login_btn = tk.Button(self.frame1)
        self.login_btn.configure(
            cursor="hand2",
            justify="left",
            relief="flat",
            text='Login')
        self.login_btn.place(anchor="center", x=200, y=200)
        self.login_btn.configure(command=self.validate_password)
        self.login_btn.bind("<Enter>", self.callback, add="")
        self.insert_password_message = tk.Message(self.frame1)
        self.insert_password_message.configure(
            cursor="arrow",
            font="TkFixedFont",
            text='Inserisci Password.',
            width=200)
        self.insert_password_message.place(anchor="center", x=200, y=100)
        self.frame1.pack(side="top")
        self.frame2 = ttk.Frame(self.main_window)
        self.frame2.configure(height=300, width=400)
        self.start_button = tk.Button(self.frame2)
        self.start_button.configure(
            cursor="hand2", state="disabled", text='Avvia')
        self.start_button.place(
            anchor="center",
            height=25,
            relwidth=0.0,
            relx=0.0,
            width=100,
            x=200,
            y=160)
        self.start_button.configure(command=lambda:automate(self))
        self.select_excel_input = tk.Button(self.frame2)
        self.select_excel_input.configure(text="Seleziona File Excel", command=lambda:self.select_excel())
        self.select_excel_input.place(width=200, x=100, y=110)

        self.frame2.pack(side="top")
        self.main_window.pack_propagate(0)

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass

    def validate_password(self):
        password = self.password_entry.get()
        
        program_password = os.getenv("PROGRAM_PASSWORD") or random.getrandbits(128)
        
        #if password is invalid show error message
        if(password != program_password):
            
            self.invalid_password_error = tk.Label(self.frame1)
            self.invalid_password_error.configure(text="Errore, password errata", fg="red")
            self.invalid_password_error.place(width=200, x=100, y=110)

            return
        
        open_website()
        
        #if error message is shown destroy it
        if hasattr(self, "invalid_password_error"):
            self.invalid_password_error.destroy()
        
        #close login form    
        self.frame1.destroy()   
            
   
    def select_excel(self):
                
        self.file = askopenfile(parent=self.frame2, mode="rb", filetype=[("xlsx file", "*.xlsx")])
    
        if self.file:
         
            text_box = tk.Label(self.frame2)
            text_box.configure(text=f"File selezionato: {self.file.name}")
            text_box.place(width=400, x=0, y=80)
            
            self.start_button.configure(state="active")
                    
        
        
