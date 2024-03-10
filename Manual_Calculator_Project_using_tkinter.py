# Creating a calculator using tkinter

# to import tkinter
from tkinter import *

expression = "" 


# Function to update expression  in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# to add the strings(concatination) 
	expression = expression + str(num) 

	# updating using the set method
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used  for handling the errors like zero  division error etc. 


	try: 

		global expression

		# eval function evaluate the expression  and str function convert the result  into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialize the expression variable  by empty string 
		expression = "" 

	# if error is generate then it is handled by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function for  clearing the contents of the entry box
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


if __name__ == "__main__": 
	# creating a gui window 
	gui = Tk() 

	# to set the background cpolur ogf the whole calculator
	gui.configure(background="blue") 

	# the title if the claculator
	gui.title(" Manual_Calculator_ ") 

	# setting the size of the calculator
	gui.geometry("300x380") 

	# StringVar() is the variable class 

	equation = StringVar() 

	# creating the text for the entry box for showing the exprssion 
	
	expression_field = Entry(gui, textvariable=equation) 

	# # grid method is used or placing the widgets at particular position in table 
	
	expression_field.grid(columnspan=300, ipadx=50,ipady=10)

	# for creating and placing it at patricular location
	 
	button1 = Button(gui, text=' 1 ', fg='black', bg='orange', 
					command=lambda: press(1), height=4, width=8) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='orange', 
					command=lambda: press(2), height=4, width=8) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='orange', 
					command=lambda: press(3), height=4, width=8) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
					command=lambda: press(4), height=4, width=8) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
					command=lambda: press(5), height=4, width=8) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
					command=lambda: press(6), height=4, width=8) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
					command=lambda: press(7), height=4, width=8) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
					command=lambda: press(8), height=4, width=8) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
					command=lambda: press(9), height=4, width=8) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='green', 
					command=lambda: press(0), height=4, width=8) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='orange', 
				command=lambda: press("+"), height=4, width=8) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='white', 
				command=lambda: press("-"), height=4, width=8) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='white', 
					command=lambda: press("*"), height=4, width=8) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='green', 
					command=lambda: press("/"), height=4, width=8) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='green', 
				command=equalpress, height=4, width=8) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='green', 
				command=clear, height=4, width=8) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='red', bg='blue', 
					command=lambda: press('.'), height=4, width=8) 
	Decimal.grid(row=6, column=0) 
	# for runing the loop
	gui.mainloop() 
