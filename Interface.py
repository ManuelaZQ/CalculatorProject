from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.title("Calculadora Científica")
root.configure(background = 'white')
root.iconbitmap('C:/Users/manuz/Documents/Proyecto Final Curso Python/logoudea.ico')
root.resizable(width=False, height=False)
root.geometry("460x500")
calc = Frame(root)
calc.config(cursor='hand2')

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
 
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
 
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
 
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            try:
                self.total /= self.current
            except ZeroDivisionError:
                self.total = "Error: Zero Division"
        if self.op == "\u005e":
            self.total **=self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
 
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
 
    def Clear_Entry(self):
        self.result = False
        self.current = ""
        self.display(0)
        self.input_value = True
 
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0
 
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
 
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
 
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
 
    def squared(self):
        try:
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)
        except ValueError:
            self.display("Error: Negative Squared")
        
 
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
  
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def log(self):
        try:
            self.result = False
            self.current = math.log10(float(txtDisplay.get()))
            self.display(self.current)
        except ValueError:
            self.display("Error: Undefined Log")

    def ln(self):
        try:
            self.result = False
            self.current = math.log(float(txtDisplay.get()))
            self.display(self.current)
        except ValueError:
            self.display("Error: Undefined Ln")
 
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

 

 

       





txtDisplay = Entry(calc,
				font=('Helvetica', 20,'bold'),
				bg='black',
				fg='white',
				bd=30,
				width=25,
				justify=RIGHT)

txtDisplay.grid(row=0,
				column=0,
				columnspan=6,
				pady=1)

added_value = Calc()
txtDisplay.insert(0, "0")
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):

		# k is in this range to place the
	# button in that particular column
	for k in range(3):
		btn.append(Button(calc,
						width=3,
						height=1,
						bg='khaki4',
						fg='white',
						font=('Helvetica', 20, 'bold'),
						bd=10, text=numberpad[i]))

		# set buttons in row & column and
		# separate them with a padding of 1 unit
		btn[i].grid(row=j, column=k, pady=0)

		# put that number as a symbol on that button
		btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
		i += 1

btnClear = Button(calc, text=chr(67),
				width=3, height=1,
				bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
				command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(65)+chr(67),
					width=3, height=1,
					bg='cyan3',
					font=('Helvetica',
						20, 'bold'), bd=10,
					command=added_value.All_Clear_Entry).grid(row=1, column=1, pady=1)

btnsq = Button(calc, text="\u221A", width=3,
			height=1, bg='cyan3',
			font=('Helvetica', 20, 'bold'),
			bd=10,
            command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="\u002b", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

btnSub = Button(calc, text="\u2212", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
				command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMul = Button(calc, text="\u00d7", width=3, height=1,
				bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text="\u00f7", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=3,
				height=1, bg='khaki4', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=10, 
                command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=3,
			height=1, bg='cyan3',
			font=('Helvetica', 20, 'bold'),
			bd=10,
            command=added_value.mathPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=12,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.sum_of_total).grid(row=5, column=3, columnspan=3, pady=1)

btnPi = Button(calc, text="\u03c0", width=3,
			height=1, bg='cyan3',
			font=('Helvetica', 20, 'bold'),
			bd=10,
            command=added_value.pi).grid(row=1, column=4, pady=1)

btnCos = Button(calc, text="Cos", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.cos).grid(row=1, column=5, pady=1)

btntan = Button(calc, text="Tan", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.tan).grid(row=3, column=5, pady=1)

btnsin = Button(calc, text="Sin", width=3,
				height=1, bg='Cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.sin).grid(row=2, column=5, pady=1)

btnlog = Button(calc, text="log", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.log).grid(row=3, column=4, pady=1)

btnln = Button(calc, text="ln", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=added_value.ln).grid(row=4, column=4, pady=1)

btnExp = Button(calc, text="\u005e", width=3,
				height=1, bg='cyan3',
				font=('Helvetica', 20, 'bold'),
				bd=10,
                command=lambda: added_value.operation("\u005e")).grid(row=2, column=4, pady=1)


btnE = Button(calc, text="e", width=3,
			height=1, bg='cyan3', 
			font=('Helvetica', 20, 'bold'),
			bd=10,
            command=added_value.e).grid(row=4, column=5, pady=1)

#btnE.setStyleSheet("Button {border-radius:29.4px}")

lblDisplay = Label(root, text="Calculadora Científica",
				font=('Helvetica', 20),
				 fg='blue',bg='white', justify=CENTER)
lblDisplay.grid(row=6, columnspan=6)

calc.grid()
calc.mainloop()