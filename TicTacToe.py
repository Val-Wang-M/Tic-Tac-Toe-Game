import tkinter
import tkinter.messagebox
click = True
count = 0
root = tkinter.Tk()
root.title('tictactoe game')



def bclick(b):
  global click,count
  if b["text"]==" "and click==True:
    b["text"]="X"
    click=False
    count+=1
    checkwin()
  elif b["text"]==" "and click==False:
    b["text"]="O"
    click=True
    count+=1
    checkwin()

def disableallButtons():
  b1.config(state=tkinter.DISABLED)
  b2.config(state=tkinter.DISABLED)
  b3.config(state=tkinter.DISABLED)
  b4.config(state=tkinter.DISABLED)
  b5.config(state=tkinter.DISABLED)
  b6.config(state=tkinter.DISABLED)
  b7.config(state=tkinter.DISABLED)
  b8.config(state=tkinter.DISABLED)
  b9.config(state=tkinter.DISABLED)


def checkwin():
  global winner 
  winner=False
  if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
    b1.config(bg="red")
    b2.config(bg="red")
    b3.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()

  elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
    b4.config(bg="red")
    b5.config(bg="red")
    b6.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
    b7.config(bg="red")
    b8.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
    b1.config(bg="red")
    b4.config(bg="red")
    b7.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
    b2.config(bg="red")
    b5.config(bg="red")
    b8.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
    b3.config(bg="red")
    b6.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
    b1.config(bg="red")
    b5.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
  elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
    b3.config(bg="red")
    b5.config(bg="red")
    b7.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! X wins!" )
    disableallButtons()
    
  #This one is check win for O 
  if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
    b1.config(bg="red")
    b2.config(bg="red")
    b3.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
    b4.config(bg="red")
    b5.config(bg="red")
    b6.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
    b7.config(bg="red")
    b8.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
    b1.config(bg="red")
    b4.config(bg="red")
    b7.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
    b2.config(bg="red")
    b5.config(bg="red")
    b8.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
    b3.config(bg="red")
    b6.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
    b1.config(bg="red")
    b5.config(bg="red")
    b9.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
    b3.config(bg="red")
    b5.config(bg="red")
    b7.config(bg="red")
    winner=True
    tkinter.messagebox.showinfo("Tic Tac Toe" , " Congratulations! O wins!" )
    disableallButtons()
  
  if count==9 and winner==False:
      b1.config(bg="grey")
      b2.config(bg="grey")
      b3.config(bg="grey")
      b4.config(bg="grey")
      b5.config(bg="grey")
      b6.config(bg="grey")
      b7.config(bg="grey")
      b8.config(bg="grey")
      b9.config(bg="grey")
      tkinter.messagebox.showinfo("Tic Tac Toe", " It's a tie.")
      disableallButtons()

  

#Do checkwin for O and the rest of X
    
b1=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b1))
b2=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b2))
b3=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b3))

b4=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b4))
b5=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b5))
b6=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b6))

b7=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b7))
b8=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b8))
b9=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b9))

#grid view
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

def reset():
  global b1,b2,b3,b4,b4,b5,b6,b7,b8,b9
  global click,count
  click=True
  count=0

  b1=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b1))
  b2=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b2))
  b3=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b3))

  b4=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b4))
  b5=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b5))
  b6=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b6))

  b7=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b7))
  b8=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b8))
  b9=tkinter.Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:bclick(b9))
  b1.grid(row=0,column=0)
  b2.grid(row=0,column=1)
  b3.grid(row=0,column=2)

  b4.grid(row=1,column=0)
  b5.grid(row=1,column=1)
  b6.grid(row=1,column=2)

  b7.grid(row=2,column=0)
  b8.grid(row=2,column=1)
  b9.grid(row=2,column=2)



my_menu=tkinter.Menu(root)
root.config(menu=my_menu)

options_menu=tkinter.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Reset game", command=reset)
#reset()
root.mainloop()
checkwin()
reset()

