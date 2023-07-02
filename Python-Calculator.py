from tkinter import *

root = Tk()
root.title('Calculadora')

#estilos
root.configure(background='white')

display_style = {'background': 'white', 'foreground': 'black', 'font':("arial", 14)}

button_style = {'background': 'lightgray', 'foreground': 'black', 'font':("arial", 12), 'width':5}

#entrada
display = Entry(root, display_style)
display.grid(row=1, columnspan=6,sticky=W+E)

#funcion entrada
i=0

def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1
def get_operation(operator):
    global i
    operator_length=len(operator)
    display.insert(i, operator)
    i+=operator_length
def clear_display():
    display.delete(0, END)
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        display.delete(0, END)
        display.insert(0, display_new_state)
    else:
        display.delete(0, END)

#funcion calcular
def calculate():
    display_state = display.get()
    try:
        math_expression = compile(display_state, 'calculadora.py', 'eval')
        result = eval(math_expression)
        clear_display()
        display.insert(0,result)
    except:
        clear_display()
        display.insert(0,"")

#numeros
Button(root, text='1',command=lambda:get_numbers(1),**button_style).grid(row=2, column=0,sticky=W+E)
Button(root, text='4',command=lambda:get_numbers(4),**button_style).grid(row=3, column=0,sticky=W+E)
Button(root, text='7',command=lambda:get_numbers(7),**button_style).grid(row=4, column=0,sticky=W+E)
Button(root, text='2',command=lambda:get_numbers(2),**button_style).grid(row=2, column=1,sticky=W+E)
Button(root, text='5',command=lambda:get_numbers(5),**button_style).grid(row=3, column=1,sticky=W+E)
Button(root, text='8',command=lambda:get_numbers(8),**button_style).grid(row=4, column=1,sticky=W+E)
Button(root, text='3',command=lambda:get_numbers(3),**button_style).grid(row=2, column=2,sticky=W+E)
Button(root, text='6',command=lambda:get_numbers(6),**button_style).grid(row=3, column=2,sticky=W+E)
Button(root, text='9',command=lambda:get_numbers(9),**button_style).grid(row=4, column=2,sticky=W+E)
Button(root, text='0',command=lambda:get_numbers(0),**button_style).grid(row=5, column=1,sticky=W+E)

#funciones
Button(root, text='AC',command=lambda:clear_display(),**button_style).grid(row=5, column=0,sticky=W+E)
Button(root, text='🠔',command=lambda:undo(),**button_style).grid(row=2, column=4,sticky=W+E,columnspan=2)
Button(root, text='=',command=lambda:calculate(),**button_style).grid(row=5, column=4,sticky=W+E,columnspan=2)

#operadores
Button(root, text='%',command=lambda:get_operation('%'),**button_style).grid(row=5, column=2,sticky=W+E)
Button(root, text='+',command=lambda:get_operation('+'),**button_style).grid(row=2, column=3,sticky=W+E)
Button(root, text='-',command=lambda:get_operation('-'),**button_style).grid(row=3, column=3,sticky=W+E)
Button(root, text='*',command=lambda:get_operation('*'),**button_style).grid(row=4, column=3,sticky=W+E)
Button(root, text='/',command=lambda:get_operation('/'),**button_style).grid(row=5, column=3,sticky=W+E)
Button(root, text='Exp',command=lambda:get_operation('**'),**button_style).grid(row=3, column=4,sticky=W+E)
Button(root, text='^2',command=lambda:get_operation('**2'),**button_style).grid(row=3, column=5,sticky=W+E)
Button(root, text='(',command=lambda:get_operation("("),**button_style).grid(row=4, column=4,sticky=W+E)
Button(root, text=')',command=lambda:get_operation(")"),**button_style).grid(row=4, column=5,sticky=W+E)

root.mainloop()