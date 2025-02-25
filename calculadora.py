from tkinter import * # importa a biblioteca Tkinter, que vamos precisar para criar a interface gráfica

# função que é chamada quando um botão é clicado
def on_button_click(number):

    global equation_text

    equation_text = equation_text + str(number)

    equation_label.set(equation_text)

# função que é chamada quando o botão de igual é clicado
def calculation():
    
    global equation_text
    
    try:    
        total = str(eval(equation_text))
    
        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:
        equation_label.set('Erro')

    except SyntaxError:
        equation_label.set('Erro')

# função que é chamada quando o botão de limpar é clicado
def clear():

    global equation_text

    equation_text = ''

    equation_label.set(equation_text)

# função que é chamada quando o botão de voltar é clicado
def back_button_click():

    global equation_text

    equation_text = equation_text[:-1]

    equation_label.set(equation_text)


window = Tk() # cria a raiz Tk

w = 350 # largura para a raiz Tk
h = 470 # altura para a raiz Tk

# aqui, recebemos a altura e a largura do nosso ecrã
ws = window.winfo_screenwidth() # largura do ecrã
hs = window.winfo_screenheight() # altura do ecrã

# calcula a posição x e y do centro do nosso ecrã
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# define a posição da janela para o centro do ecrã 
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.title("Calculadora") # título da janela

equation_text = '' # o texto da equação começa vazio
equation_label = StringVar() # a variável que contém o texto da equação


# todas as definições de botões e etc.

label = Label(window, textvariable=equation_label, font=('Arial', 20), bg='lightgray', width=22, height=2)
label.pack()

space = Label(window, text='', font=('Arial', 20), width=22, height=1)
space.pack()

frame = Frame(window)
frame.pack()

button_1 = Button(frame, text='1', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(1))
button_1.grid(row=0, column=0)

button_2 = Button(frame, text='2', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(2))
button_2.grid(row=0, column=1)

button_3 = Button(frame, text='3', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(3))
button_3.grid(row=0, column=2)

button_4 = Button(frame, text='4', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(4))
button_4.grid(row=1, column=0)

button_5 = Button(frame, text='5', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(5))
button_5.grid(row=1, column=1)

button_6 = Button(frame, text='6', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(6))
button_6.grid(row=1, column=2)

button_7 = Button(frame, text='7', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(7))
button_7.grid(row=2, column=0)

button_8 = Button(frame, text='8', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(8))
button_8.grid(row=2, column=1)

button_9 = Button(frame, text='9', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(9))
button_9.grid(row=2, column=2)

button_0 = Button(frame, text='0', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(0))
button_0.grid(row=3, column=1)

button_plus = Button(frame, text='+', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('+'))
button_plus.grid(row=0, column=3)

button_minus = Button(frame, text='-', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('-'))
button_minus.grid(row=1, column=3)

button_multiply = Button(frame, text='*', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('*'))
button_multiply.grid(row=2, column=3)

button_divide = Button(frame, text='/', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('/'))
button_divide.grid(row=3, column=3)

button_equal = Button(frame, text='=', font=('Arial', 20), width=3, height=1, command=calculation)
button_equal.grid(row=3, column=2)

button_decimal = Button(frame, text='.', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('.'))
button_decimal.grid(row=3, column=0)

button_clear = Button(window, text='Limpar', font=('Arial', 20), width=11, height=1, command=clear)
button_clear.pack()

button_back = Button(window, text='←', font=('Arial', 20), width=11, height=1, command=back_button_click)
button_back.pack()

button_parentesis_open = Button(frame, text='(', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('('))
button_parentesis_open.grid(row=0, column=4)

button_parentesis_close = Button(frame, text=')', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click(')'))
button_parentesis_close.grid(row=1, column=4)

button_power = Button(frame, text='^', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('**'))
button_power.grid(row=2, column=4)

button_mod = Button(frame, text='%', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('%'))
button_mod.grid(row=3, column=4)

window.mainloop() # inicia a janela