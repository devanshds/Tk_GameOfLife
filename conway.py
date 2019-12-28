#Imports
from tkinter import *
import random
import threading

#Constants
ROWS=30
COLS=60
LABEL="Label(window, text ='0',fg='black', bg='black')"
INITIAL=[(random.randint(0,ROWS),random.randint(0,COLS)) for iter in range(int((ROWS*COLS)/4))]
ALIVE=".config(bg='white',fg='white',text='1')"
DEAD=".config(bg='black',fg='black',text='0')"


window=Tk()
window.title("Conway's Game Of Life")
window.configure(background='black')


for i in range(ROWS):
    for j in range(COLS):
        exec('lbl_'+str(i)+'_'+str(j)+'='+ LABEL)
        exec('lbl_'+str(i)+'_'+str(j)+'.'+'grid(row=i,column=j)')
        if (i,j) in INITIAL:
            exec('lbl_'+str(i)+'_'+str(j)+ALIVE)

def conway():
    def callback():
        for i in range(ROWS):
            for j in range(COLS):
                ALIVENEIGHBOURS=0
                for l in range(-1,2):
                        for m in range(-1,2):
                            try:
                                if eval('lbl_'+str(l+i)+'_'+str(m+j)+'["text"]=="1"'):
                                    ALIVENEIGHBOURS += 1
                            except:
                                pass
                ALIVENEIGHBOURS -= 1
                if eval('lbl_'+str(i)+'_'+str(j)+'["bg"]==("white")') and ALIVENEIGHBOURS < 2:
                    exec('lbl_'+str(i)+'_'+str(j)+ DEAD)
                elif eval('lbl_'+str(i)+'_'+str(j)+'["bg"]==("white")') and ALIVENEIGHBOURS > 3:
                    exec('lbl_'+str(i)+'_'+str(j)+ DEAD)
                elif eval('lbl_'+str(i)+'_'+str(j)+'["bg"]==("black")') and ALIVENEIGHBOURS == 3:
                    exec('lbl_'+str(i)+'_'+str(j)+ ALIVE)
        window.after(500,callback)
    t=threading.Thread(target=callback)
    t.start()

conway()


window.mainloop()
