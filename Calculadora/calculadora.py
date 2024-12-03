from tkinter import Tk, Frame, Label, Entry, Text, Button, StringVar

raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(0, 0)

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
res = 0
reset_pantalla = False

num1 = 0
count_resta = 0
count_multi = 0
count_div = 0

# ------------------ PANTALLA ------------------ |

num_pantalla = StringVar()

pantalla = Entry(miFrame, textvariable=num_pantalla)
pantalla.grid(row=1, column=1, padx=3, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# ------------------ FUNCIONES ------------------ |

def numero_pulsado(num):
    global reset_pantalla

    if reset_pantalla is not False:
        num_pantalla.set(num)
        reset_pantalla = False
    else:
        num_pantalla.set(num_pantalla.get() + str(num))


def suma(num):
    global operacion
    global res
    global reset_pantalla

    res += int(num)
    operacion = "suma"
    reset_pantalla = True
    num_pantalla.set(res)


def resta(num):
    global operacion
    global res
    global reset_pantalla
    global num1
    global count_resta

    if count_resta == 0:
        num1 = int(num)
        res = num1
    else:
        if count_resta == 1:
            res = num1 - int(num)
        else:
            res = int(res) - int(num)
        num_pantalla.set(res)
        res = num_pantalla.get()

    count_resta += 1
    operacion = "resta"
    reset_pantalla = True


def multiplica(num):
    global operacion
    global res
    global reset_pantalla
    global num1
    global count_multi

    if count_multi == 0:
        num1 = int(num)
        res = num1
    else:
        if count_multi == 1:
            res = num1 * int(num)
        else:
            res = int(res) * int(num)
        num_pantalla.set(res)
        res = num_pantalla.get()

    count_multi += 1
    operacion = "multiplicacion"
    reset_pantalla = True


def divide(num):
    global operacion
    global res
    global reset_pantalla
    global num1
    global count_div

    if count_div == 0:
        num1 = float(num)
        res = num1
    else:
        if count_div == 1:
            res = num1 / float(num)
        else:
            res = float(res) / float(num)
        num_pantalla.set(res)
        res = num_pantalla.get()

    count_div += 1
    operacion = "division"
    reset_pantalla = True


def resultado():
    global res
    global operacion
    global count_resta
    global count_multi
    global count_div

    if operacion == "suma":
        num_pantalla.set(res + int(num_pantalla.get()))
        res = 0
    elif operacion == "resta":
        num_pantalla.set(res - int(num_pantalla.get()))
        res = 0
        count_resta = 0
    elif operacion == "multiplicacion":
        num_pantalla.set(res * int(num_pantalla.get()))
        res = 0
        count_multi = 0
    elif operacion == "division":
        num_pantalla.set(res / int(num_pantalla.get()))
        res = 0
        count_div = 0


# ------------------ FILA 1 ------------------ |

boton7 = Button(miFrame, text="7", width=3, command=lambda: numero_pulsado(7))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numero_pulsado(8))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numero_pulsado(9))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3,
    command=lambda: divide(num_pantalla.get()))
botonDiv.grid(row=2, column=4)

# ------------------ FILA 2 ------------------ |

boton4 = Button(miFrame, text="4", width=3, command=lambda: numero_pulsado(4))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numero_pulsado(5))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numero_pulsado(6))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="x", width=3,
    command=lambda: multiplica(num_pantalla.get()))
botonMult.grid(row=3, column=4)

# ------------------ FILA 3 ------------------ |

boton1 = Button(miFrame, text="1", width=3, command=lambda: numero_pulsado(1))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numero_pulsado(2))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numero_pulsado(3))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3,
    command=lambda: resta(num_pantalla.get()))
botonRest.grid(row=4, column=4)

# ------------------ FILA 4 ------------------ |

boton0 = Button(miFrame, text="0", width=3, command=lambda: numero_pulsado(0))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda: numero_pulsado(","))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=3,
    command=lambda: suma(num_pantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()
