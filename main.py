# Using tkinter 

import tkinter as tk
import ctypes

root = tk.Tk()
myappid = 'mynameisthesolomon'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root.iconbitmap('code.ico')
root.mainloop()

# Using customtkinter 

import customtkinter as ctk
import ctypes

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
myappid = 'mynameisthesolomon'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root.iconbitmap('code.ico')
root.title("Minha App com CustomTkinter")
root.geometry("400x300")
root.mainloop()