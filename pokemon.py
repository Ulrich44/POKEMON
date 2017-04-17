## Se importan las librerias

from tkinter import *
from sys import setrecursionlimit
import random

## De la libreria "SYS" nada mas utilizamos esta funcion para
## no nos afecte el limite de recursividad

setrecursionlimit(999999999)

## Creamos la ventana

ventana = Tk()

## Esta parte lo unico que hace es colocar el juego en el
## centro de la pantalla de la computadora

ventana.update_idletasks()
ancho = ventana.winfo_screenwidth() - 560
alto = ventana.winfo_screenheight() - 560
ventana.geometry("%dx%d%+d%+d" % (560, 560, ancho / 2, alto / 2))

## Asiganamos los puntos de salida de "ASH"
## Son simplemente puntos en la ventana

x_ini = 260
y_ini = 480

## Variable que funciona como limites de ventana segun el
## lugar donde se encuentre  "ASH"

limit_Y_UP = 120  ## Se asigna el limite superior
limit_Y_DOWN = 490  ## Se asigna el limite inferior
limit_X_LEFT = 20  ## Se asigna el limite izquierdo
limit_X_RIGHT = 500  ## Se asigna el limite derecho

## Asignamos la primera posicion de "ASH"
## Las posiciones de "ASH" son simples imagenes que se cargan
## Segun al tecla que se preciona, las cuales estan en la carpeta del archivo.py

ash = PhotoImage(file="ash_up.gif")

## Asignamos la imagen de fondo
## Al igual que "ASH", mi idea inical, es que el fondo cambie segun la posicion de "ASH"

fondo = PhotoImage(file="lab_oak.gif")
num_fondo = 1

## Aqui se coloca en la ventana del juego, el primer fondo y la poscicion inical de "ASH"
label_FONDO = Label(ventana, image=fondo).place(x=0, y=0)
label_ASH = Label(ventana, image=ash).place(x=x_ini, y=y_ini)

## Esta es en si, la funcion principal, en esta parte ocurren
##Todos los cambios segun los eventos que sucedan en pantalla o teclado

def mover(ash):
    global x_ini, y_ini, fondo, num_fondo, limit_Y_UP, limit_Y_DOWN, limit_X_LEFT, limit_X_RIGHT  ## Se llama a las variables globales
    label_FONDO = Label(ventana, image=fondo).place(x=0,
                                                    y=0)  ## Se actualiza el fondo primero para que quede detras de los demas elementos
    label_ASH = Label(ventana, image=ash).place(x=x_ini, y=y_ini)  ## Se acutlza la posicion de "ASH"
    print(str(x_ini), str(
        y_ini))  ## Esto lo coloco simplemente para poder ver donde esta #ASH# y asi poder ir colocando las posiciones ya sea de otros elemntos o restricciones para "ASH" como limite de pantalla
    x_ini = 260
    y_ini = 480

    if x_ini == 260 and y_ini == 490 and num_fondo == 1:  ## Este if cambia el fondo hacia afuera del laboratorio
        limit_Y_UP = 30  ## Se actualiza el nuevo limite superior
        limit_Y_DOWN = 490  ## Se actualiza el nuevo limite inferior
        limit_X_LEFT = 20  ## Se actualiza el nuevo limite izquierdo
        limit_X_RIGHT = 500  ## Se actualiza el nuevo limite derecho
        num_fondo = 2
        fondo = PhotoImage(
            file="afueras.gif")  ## Como lo dije anteriormente, el fondo es solo una imagen, aqui se cambia si "ASH" se acerca a la puerta
        x_ini = 380  ## Se asignan los nuevos puntos de aparicion para que salga del laboratorio
        y_ini = 340  ## Se asignan los nuevos puntos de aparicion para que salga del laboratorio
        label_FONDO = Label(ventana, image=fondo).place(x=0,
                                                        y=0)  ## Se actualiza el fondo primero para que quede detras de los demas elementos
        label_ASH = Label(ventana, image=ash).place(x=x_ini, y=y_ini)  ## Se acutlza la posicion de "ASH"
    if x_ini == 380 and y_ini == 330 and num_fondo == 2:  ## Este if cambia el fondo hacia afuera del laboratorio
        limit_Y_UP = 120  ## Se actualiza el nuevo limite superior
        limit_Y_DOWN = 490  ## Se actualiza el nuevo limite inferior
        limit_X_LEFT = 20  ## Se actualiza el nuevo limite izquierdo
        limit_X_RIGHT = 500  ## Se actualiza el nuevo limite derecho
        num_fondo = 1
        fondo = PhotoImage(
            file="lab_oak.gif")  ## Como lo dije anteriormente, el fondo es solo una imagen, aqui se cambia si "ASH" se acerca a la puerta
        x_ini = 260  ## Se asignan los nuevos puntos de aparicion para que salga del laboratorio
        y_ini = 480  ## Se asignan los nuevos puntos de aparicion para que salga del laboratorio
        label_FONDO = Label(ventana, image=fondo).place(x=0,
                                                        y=0)  ## Se actualiza el fondo primero para que quede detras de los demas elementos
        label_ASH = Label(ventana, image=ash).place(x=x_ini, y=y_ini)  ## Se acutlza la posicion de "ASH"

    ventana.mainloop()  ## De momento es una funcio recursiva, es un problema pero no super de que otra forma hacer que todo funcionara bien


### Este modulo actualiza la posicion de "ASH" 10
### pixeles hacia arriba y cambia la imagen para una
### animacion de movimiento

def change(evento):
    global y_ini, limit_Y_UP
    if y_ini != limit_Y_UP:
        y_ini -= 10
    ash = PhotoImage(file="ash_up.gif")
    mover(ash)


### Este modulo actualiza la posicion de "ASH" 10
### pixeles hacia arriba y cambia la imagen para una
### animacion de movimiento

def change2(evento):
    global y_ini, limit_Y_DOWN
    if y_ini != limit_Y_DOWN:
        y_ini += 10
    ash = PhotoImage(file="ash_down.gif")
    mover(ash)


### Este modulo actualiza la posicion de "ASH" 10
### pixeles hacia arriba y cambia la imagen para una
### animacion de movimiento

def change3(evento):
    global x_ini, limit_X_LEFT
    if x_ini != limit_X_LEFT:
        x_ini -= 10
    ash = PhotoImage(file="ash_left.gif")
    mover(ash)


### Este modulo actualiza la posicion de "ASH" 10
### pixeles hacia arriba y cambia la imagen para una
### animacion de movimiento

def change4(evento):
    global x_ini, limit_X_RIGHT
    if x_ini != limit_X_RIGHT:
        x_ini += 10
    ash = PhotoImage(file="ash_right.gif")
    mover(ash)


ventana.bind_all("<Up>", change)  ## Detecta cuando se presiona la tecla arriba
ventana.bind_all("<Down>", change2)  ## Detecta cuando se presiona la tecla abajo
ventana.bind_all("<Left>", change3)  ## Detecta cuando se presiona la tecla izquierda
ventana.bind_all("<Right>", change4)  ## Detecta cuando se presiona la tecla derecha

ventana.mainloop()  ## Da incio al programa





