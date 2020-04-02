from tkinter import *
expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if __name__=="__main__":
    gui=Tk()
    gui.configure(background="light grey")
    gui.title("Calculator")
    gui.geometry("312x220")
    equation=StringVar()
    expression_field=Entry(gui,textvariable=equation)
    expression_field.grid(columnspan=4,ipadx=100,ipady=5)
    equation.set('')
    clear=Button(gui,text='C',fg='black',bg='grey',command=clear,height=2,width=10)
    clear.grid(row=3,column=0)
    divide=Button(gui,text='/',fg='black',bg='grey',command=lambda:press("/"),height=2,width=10)
    divide.grid(row=3,column=1)
    multiply=Button(gui,text='*',fg='black',bg='grey',command=lambda:press("*"),height=2,width=10)
    multiply.grid(row=3,column=3)
    button7=Button(gui,text='7',fg='black',bg='grey',command=lambda:press(7),height=2,width=10)
    button7.grid(row=4,column=0)
    button8=Button(gui,text='8',fg='black',bg='grey',command=lambda:press(8),height=2,width=10)
    button8.grid(row=4,column=1)
    button9=Button(gui,text='9',fg='black',bg='grey',command=lambda:press(9),height=2,width=10)
    button9.grid(row=4,column=2)
    button4=Button(gui,text='4',fg='black',bg='grey',command=lambda:press(4),height=2,width=10)
    button4.grid(row=5,column=0)
    button5=Button(gui,text='5',fg='black',bg='grey',command=lambda:press(5),height=2,width=10)
    button5.grid(row=5,column=1)
    button6=Button(gui,text='6',fg='black',bg='grey',command=lambda:press(6),height=2,width=10)
    button6.grid(row=5,column=2)
    button1=Button(gui,text='1',fg='black',bg='grey',command=lambda:press(1),height=2,width=10)
    button1.grid(row=6,column=0)
    minus=Button(gui,text='-',fg='black',bg='grey',command=lambda:press("-"),height=2,width=10)
    minus.grid(row=4,column=3)
    plus=Button(gui,text='+',fg='black',bg='grey',command=lambda:press("+"),height=2,width=10)
    plus.grid(row=5,column=3)
    equal=Button(gui,text='=',fg='black',bg='grey',command=equalpress,height=2,width=10)
    equal.grid(row=6,column=3)
    button3=Button(gui,text='3',fg='black',bg='grey',command=lambda:press(3),height=2,width=10)
    button3.grid(row=6,column=2)
    button2=Button(gui,text='2',fg='black',bg='grey',command=lambda:press(2),height=2,width=10)
    button2.grid(row=6,column=1)
    button0=Button(gui,text='0',fg='black',bg='grey',height=2,command=lambda:press(0),width=10)
    button0.grid(row=3,column=2)

    gui.mainloop()
