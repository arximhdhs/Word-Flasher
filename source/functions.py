import threading
from core import *

first=False
pointer=0
def init():
    global first
    first=False
    play_core()
    pointer=0

def play(btn_play,btn_pause,window):
    global pointer
    global first
    if first==False:
        if pointer==1:
            return 
        btn_play.config(bg="white")
        btn_pause.config(bg="red")
        t = threading.Thread(target=core,args=[window])
        t.start()
        pointer=1
        first=True
    else:
        if pointer==1:
            return 
        btn_play.config(bg="white")
        btn_pause.config(bg="red")
        pointer=1
        play_core()
        first=True

    return 

def pause(btn_pause,btn_play,window):
    global pointer
    if pointer==0:
        return
    pause_core() 
    btn_pause.config(bg="white")
    btn_play.config(bg="green")
    pointer=0
    return 


def add_word():
    t = threading.Thread(target=add_inter)
    t.start()
    return 
