from tkinter import filedialog
import tkinter as tk    
from functions import *
from tkinter.ttk import *
from core import close

#when the x button in clicked
def on_closing(window):
    close()
    window.destroy()
#when the x button in clicked

window = tk.Tk()
window.title("Time to learn some English you punk!")
# window.iconbitmap(r'./images/icon.ico')
window.configure(bg='white')

window.rowconfigure(0, minsize=200, weight=1)
window.rowconfigure(1, minsize=400, weight=1)




fr_menu = tk.Frame(window)
fr_play_pause = tk.Frame(window)


btn_add = tk.Button(fr_menu, text="Add a new word",font=("Times",24),pady=20,padx=100,bg="#18354c",fg="white")
btn_erase = tk.Button(fr_menu, text="Erase a word",font=("Times",24),pady=20,padx=100,bg="#18354c",fg="white")
btn_settings = tk.Button(fr_menu, text="Settings",font=("Times",24),pady=20,padx=100,bg="#18354c",fg="white")

btn_add.config(command= lambda: add_word())

btn_add.grid(row=0,column=0)
btn_erase.grid(row=0,column=1)
btn_settings.grid(row=0,column=2)

photo_play = tk.PhotoImage(file = r"./images/play.png") 
photo_pause = tk.PhotoImage(file = r"./images/pause.png")

btn_play = tk.Button(fr_play_pause, image =photo_play ,pady=60,padx=100,bg="green",fg="white")
btn_pause = tk.Button(fr_play_pause, image =photo_pause,text="Pause",pady=60,padx=100,bg="white",fg="white")

init()
btn_play.config(command= lambda: play(btn_play,btn_pause,window))
btn_pause.config(command= lambda: pause(btn_pause,btn_play,window))


btn_play.grid(row=0,column=0)
btn_pause.grid(row=0,column=1)



fr_menu.grid(row=0,column=0,sticky="nw")
fr_play_pause.grid(row=1,column=0,sticky="n")




window.protocol("WM_DELETE_WINDOW",lambda : on_closing(window))
window.mainloop()



