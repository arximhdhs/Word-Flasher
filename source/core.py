from tkinter import *
import time
import random as rd
from random import randrange
from tkinter.font import Font
from pydub import AudioSegment
from pydub.playback import play
import requests
import os.path
from os import path
import sys



play_or = 1
ret=0

def add_word_sub(eng,trans):
    l_eng = eng.get()
    l_trans = trans.get()
    if l_eng!="" and l_trans!="":
        f = open("../words", "a")
        f.write(l_eng+"="+"\n")
        f.write(l_trans+"\n")
        f.close()
        eng.delete(0,END)
        trans.delete(0,END)
        mp1 = "../audio/" +l_eng +".mp3"
        mp2 = "../audio/" +l_trans +".mp3"
        url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q="+l_eng+"&tl=en&total=1&idx=0&textlen="+str(len(l_eng))
        r1 = requests.get(url, allow_redirects=True)
        open(mp1, 'wb').write(r1.content)
        url = "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q="+l_trans+"&tl=el&total=1&idx=0&textlen="+str(len(l_trans))
        r1 = requests.get(url, allow_redirects=True)
        open(mp2, 'wb').write(r1.content)
        sound = AudioSegment.from_mp3(mp1) +  AudioSegment.from_mp3(mp2) 
        sound.export(mp1,format="mp3")
    return 

def display_the_word(string,window):
    global ret
    if ret==1:
        return
    root = Tk()
    root.option_add("*Font", "courier")
    root.title("Time to learn some English you punk")
    root.configure(background='white')
    root.geometry("1000x400")
    myFont = Font(family="Times New Roman", size=8)
    
    title = Label(text=string,font=("Times New Roman",50),master=root)
    title.configure(background='white')
    title.pack()
    
    root.after(5000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    
    root.mainloop()

def core(window):
    global play_or
    global ret
    index=0
    while 1:
        if ret==1:
            return
        if play_or==0:
            while 1:
                if ret==1:
                    return
                if play_or!=0:
                    break
                time.sleep(0.2)
        sleep_time=randrange(10)
        f = open("../words", "r")
        
        f_tester=f.readline()
        synolo=[]
        while f_tester!='':
            helper=f.readline()
            f_tester=f_tester+helper
            synolo.append(f_tester.split("="))
            f_tester=f.readline()
        # while f_tester
        # txt = f.readline()
        # k=[]
        index+=1
        if index==len(synolo):
            index=0
        string = synolo[index][0]+ " = " + synolo[index][1]
        print(synolo[index][0])


        if path.exists("../audio/" + synolo[index][0] + ".mp3"):
            sound = AudioSegment.from_mp3("../audio/" + synolo[index][0] + ".mp3")

            play(sound)



        display_the_word(string,window)
        if ret==1:
            return
        time.sleep(sleep_time)

    
def pause_core():
    global play_or
    play_or=0
    return

def play_core():
    global play_or
    play_or=1
    return

def close():
    global ret
    ret =1


def add_inter():
    global ret
    if ret==1:
        return
    root = Tk()
    root.option_add("*Font", "courier")
    root.title("Add a new word")
    root.configure(background='#18354c')
    root.geometry("600x150")
    root.columnconfigure([0,1], minsize=300, weight=1)
    root.rowconfigure(0, minsize=60, weight=1)
    root.rowconfigure(1, minsize=100, weight=1)


    frame_eng = Frame(master=root,bg="#18354c")
    lbl_eng = Label(master=frame_eng,text="English",font=("Times",24),bg="#18354c",fg="white")
    ent_eng = Entry(master=frame_eng,width=30,font=("Times New Roman",12))
    lbl_eng.grid(row=0,column=0)
    ent_eng.grid(row=1,column=0)

    frame_eng.columnconfigure(0, minsize=300, weight=1)



    frame_trans = Frame(master=root,bg="#18354c")
    lbl_trans = Label(master=frame_trans,text="Tranlation",font=("Times",24),bg="#18354c",fg="white")
    ent_trans = Entry(master=frame_trans,width=30,font=("Times New Roman",12))
    lbl_trans.grid(row=0,column=0)
    ent_trans.grid(row=1,column=0)

    frame_trans.columnconfigure(0, minsize=300, weight=1)

    btn_submit = Button(master=root,text="Submit",bg="green",font=("Times",24),fg="white",padx=10,pady=10,command= lambda: add_word_sub(ent_eng,ent_trans))
    btn_submit.grid(row=1,sticky="n",columnspan=2)

    frame_eng.grid(row=0,column=0)
    frame_trans.grid(row=0,column=1)


    root.mainloop()



