#creating the INDIAN FLAG using canvas
from tkinter import *

root =Tk()
C = Canvas (root,bg="black",
            height=500,width=500)


#oval = C.create_oval(80,30,200,150,fill="yellow")
#arc =C.create_arc(40,140,40,40,start=40,extent=20,fill="black")

rectanngel=C.create_rectangle(400,200,50,50,fill="orange",outline="black")#the upper section
rectanngel=C.create_rectangle(400,200,50,125,fill="white",outline="black")#the middle section
rectanngel=C.create_rectangle(400,200,50,280,fill="green",outline="black")#the lower section


oval = C.create_oval(300,200,150,125,fill="blue")#the ashoka chakra

C.pack()
mainloop()





 

     

