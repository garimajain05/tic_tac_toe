from tkinter import *
count=0
fr=Tk()
fr.title("TicTacToe")
fr.geometry("300x300")

def work(b):
    global count
    count+=1
    b['text']="X"    
    if count%2==0:
        b['text']="O"
    b['state']=DISABLED    
    if (b1['text']=="X" and b2['text']=="X" and b3['text']=="X") or (b4['text']=="X" and b5['text']=="X" and b6['text']=="X") or (b7['text']=="X" and b8['text']=="X" and b9['text']=="X"):
        print("X wins")
    elif (b1['text']=="X" and b4['text']=="X" and b7['text']=="X") or (b2['text']=="X" and b5['text']=="X" and b8['text']=="X") or (b3['text']=="X" and b6['text']=="X" and b9['text']=="X"):
        print("X wins")
    elif (b1['text']=="X" and b5['text']=="X" and b9['text']=="X") or (b3['text']=="X" and b5['text']=="X" and b7['text']=="X"):
        print("X wins")
    elif (b1['text']=="O" and b2['text']=="O" and b3['text']=="O") or (b4['text']=="O" and b5['text']=="O" and b6['text']=="O") or (b7['text']=="O" and b8['text']=="O" and b9['text']=="O"):
        print("O wins")
    elif (b1['text']=="O" and b4['text']=="O" and b7['text']=="O") or (b2['text']=="O" and b5['text']=="O" and b8['text']=="O") or (b3['text']=="O" and b6['text']=="O" and b9['text']=="O"):
        print("O wins")
    elif (b1['text']=="O" and b5['text']=="O" and b9['text']=="O") or (b3['text']=="O" and b5['text']=="O" and b7['text']=="O"):
        print("O wins")
b1=Button(fr,text='',command=lambda:work(b1))
b1.place(x=0,y=0,width=100,height=100)
b2=Button(fr,text='',command=lambda:work(b2))
b2.place(x=100,y=0,width=100,height=100)
b3=Button(fr,text='',command=lambda:work(b3))
b3.place(x=200,y=0,width=100,height=100)

b4=Button(fr,text='',command=lambda:work(b4))
b4.place(x=0,y=100,width=100,height=100)
b5=Button(fr,text='',command=lambda:work(b5))
b5.place(x=100,y=100,width=100,height=100)
b6=Button(fr,text='',command=lambda:work(b6))
b6.place(x=200,y=100,width=100,height=100)

b7=Button(fr,text='',command=lambda:work(b7))
b7.place(x=0,y=200,width=100,height=100)
b8=Button(fr,text='',command=lambda:work(b8))
b8.place(x=100,y=200,width=100,height=100)
b9=Button(fr,text='',command=lambda:work(b9))
b9.place(x=200,y=200,width=100,height=100)
fr.mainloop()