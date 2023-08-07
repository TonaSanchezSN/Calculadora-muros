from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")    
raiz.resizable(1,1)
raiz.iconbitmap("icono.ico")
raiz.config(bg = "red")

frameUno = Frame()

frameUno.config(width =  "1920", height="1080")
frameUno.pack(fill = "both", expand = False)

hori = 30

tabla1Pesta1 = Label (frameUno, text = "Datos generales de la construcción",font= 'Calibri 11 bold').place(x = hori, y= 20)
concepto = Label (frameUno, text = "Concepto",font= 'Calibri 11 italic').place(x = hori,  y = 40)	
anchoEnX1 = Label (frameUno, text = "Ancho, dirección X (m)").place(x = hori, y= 60)	
largoEnY2 = Label (frameUno, text = "Largo, dirección Y (m)").place(x = hori, y= 80)
numDeniv3 = Label (frameUno, text = "Número de niveles").place(x = hori, y= 100)		
tipDeEst4 = Label (frameUno, text = "Tipo de estructura").place(x = hori, y= 120)		
zonaSis5 = Label (frameUno, text = "Zona sísmica").place(x = hori, y= 140)	
tipSuelo6 = Label (frameUno, text = "Tipo de suelo").place(x = hori, y= 160)
coefSis7 = Label (frameUno, text = "Coeficiente sísmico c").place(x = hori, y= 180)
facCompSis8 = Label (frameUno, text = "Factor de comportamiento sísmico  Q").place(x = hori, y= 200)
coefSisRed9 = Label (frameUno, text = "Coeficiente sísmico reducido").place(x = hori, y= 220)	
facRedCargaVer10 = Label (frameUno, text = "Factor de reducción de carga vertical (Fr)").place(x = hori, y= 240)	
facRes11 = Label (frameUno, text = "Factor de resistencia (FR)").place(x = hori, y= 260)	
facCar12 = Label (frameUno, text = "Factor de carga (F.C.)").place(x = hori, y= 280)

tabla2Pesta1 = Label (frameUno, text = "Propiedades de muro",font= 'Calibri 11 bold').place(x = hori, y= 305)
tipDeM13 = Label (frameUno, text = "Tipo de muro").place(x = hori, y= 325)
altura14 = Label (frameUno, text = "Altura, H (m)").place(x = hori, y= 345)	
espesor15 = Label (frameUno, text = "Espesor, t (m)").place(x = hori, y= 365)
resCompDisenoDeLaMamp116 = Label (frameUno, text = "Resistencia a la compresión para diseño de la" ).place(x = hori, y= 385)
resCompDisenoDeLaMamp1v117 = Label (frameUno, text ="mampostería, f'm (Kg/cm2)").place(x = hori, y= 405)
resCompDiaDisDeLaMamp218 = Label (frameUno, text = "Resistencia a la compresión diagonal para diseño").place(x = hori, y= 425)
resCompDiaDisDeLaMamp2v219 = Label (frameUno, text = "de la mampostería, v'm (Kg/cm2)").place(x = hori, y= 445)
peso20 = Label (frameUno, text = "Peso (Kg/m)").place(x = hori, y= 465)

tabla3Pesta1 = Label (frameUno, text = "Datos de castillos y losa",font= 'Calibri 11 bold').place(x = hori, y= 490)
ancho21 = Label (frameUno, text = "Ancho, a (m)").place(x = hori, y= 510)
largo22 = Label (frameUno, text = "Largo, b (m)").place(x = hori, y= 530)
resConComp23	= Label (frameUno, text = "Resistencia de concreto a compresión, f'c (Kg/cm2)").place(x = hori, y= 550)
esfFluenEspeAceRefuer124 =	Label (frameUno, text = "Esfuerzo de fluencia especificado del acero").place(x = hori, y= 570)
esfFluenEspeAceRefuer1v125 =	Label (frameUno, text = "de refuerzo, fy (Kg/cm2)").place(x = hori, y= 590)
areaAceTotal26 =	Label (frameUno, text = "Área del acero total, As (4#3 cm2)").place(x = hori, y= 610)


#Cuadros de Texto
entradaTxt = 300

entradaAnchoEnX1 = Entry(frameUno).place(x=entradaTxt, y=60)
entradaLargoEnY2 = Entry(frameUno).place(x=entradaTxt, y=80)
entradaNumDeniv3 = Entry(frameUno).place(x=entradaTxt, y=100)
entradatipDeEst4 = Entry(frameUno).place(x=entradaTxt, y=120)
entradaZonaSis5 = Entry(frameUno).place(x=entradaTxt, y=140)
entradaTipSuelo6 = Entry(frameUno).place(x=entradaTxt, y=160)
entradaCoefSis7 = Entry(frameUno).place(x=entradaTxt, y=180)
entradaFacCompSis8 = Entry(frameUno).place(x=entradaTxt, y=200)
entradaCoefSisRed9 = Entry(frameUno).place(x=entradaTxt, y=220)
entradaFacRedCargaVer10 = Entry(frameUno).place(x=entradaTxt, y=240)
entradaFacRes11 = Entry(frameUno).place(x=entradaTxt, y=260)
entradaFacCar12 = Entry(frameUno).place(x=entradaTxt, y=280)

entradaTipDeM13 = Entry(frameUno).place(x=entradaTxt, y=325)
entradaAltura14 = Entry(frameUno).place(x=entradaTxt, y=345)
entradaNumEspesor15 = Entry(frameUno).place(x=entradaTxt, y=365)
entradatipResCompDisenoDeLaMamp116 = Entry(frameUno).place(x=entradaTxt, y=385)
##entradaResCompDisenoDeLaMamp1v117 = Entry(frameUno).place(x=entradaTxt, y=405)
entradaResCompDiaDisDeLaMamp218 = Entry(frameUno).place(x=entradaTxt, y=425)
#entradaResCompDiaDisDeLaMamp2v219 = Entry(frameUno).place(x=entradaTxt, y=445)
entradaOeso20 = Entry(frameUno).place(x=entradaTxt, y=465)

entradaAncho21 = Entry(frameUno).place(x=entradaTxt, y=510)
entradaLargo22 = Entry(frameUno).place(x=entradaTxt, y=530)
entradaResConComp23 = Entry(frameUno).place(x = 305, y=550)
entradaEsfFluenEspeAceRefuer124 = Entry(frameUno).place(x=entradaTxt, y=570)
#entradaEsfFluenEspeAceRefuer1v125 = Entry(frameUno).place(x=entradaTxt, y=590)
entradaAreaAceTotal26 = Entry(frameUno).place(x=entradaTxt, y=610)


#funciones de los botones 

def calcular():

    try: 
        anchoEnX1 = entradaAnchoEnX1.get()
        largoEnY2 = entradaLargoEnY2.get()
        numDeniv3 = entradaNumDeniv3.get()
        tipDeEst4 = entradatipDeEst4.get()
        zonaSis5 =	entradaZonaSis5 .get()
        tipSuelo6	= entradaTipSuelo6.get()
        coefSis7 =	entradaCoefSis7.get()
        facCompSis8	= entradaFacCompSis8.get()
        coefSisRed9	= entradaCoefSisRed9.get()
        facRedCargaVer10 = entradaFacRedCargaVer10.get()
        facRes11 = entradaFacRes11.get()
        facCar12 = entradaFacCar12.get()
        tipDeM13 = entradaTipDeM13.get()
        tltura14 = entradaAltura14.get()
        numEspesor15 = entradaNumEspesor15.get()
        tipResCompDisenoDeLaMamp116	= entradatipResCompDisenoDeLaMamp116.get()
        #ResCompDisenoDeLaMamp1v117	= entradaResCompDisenoDeLaMamp1v117.get()
        resCompDiaDisDeLaMamp218 = entradaResCompDiaDisDeLaMamp218.get()
        #ResCompDiaDisDeLaMamp2v219	=entradaResCompDiaDisDeLaMamp2v219.get()
        oeso20 = entradaOeso20.get()
        ancho21	= entradaAncho21.get()
        largo22	= entradaLargo22.get()
        resConComp23 = entradaResConComp23.get()
        esfFluenEspeAceRefuer124 = entradaEsfFluenEspeAceRefuer124.get()
        #EsfFluenEspeAceRefuer1v125	= entradaEsfFluenEspeAceRefuer1v125.get()
        entradaAreaAceTotal26 = entradaAreaAceTotal26.get()
    except ValueError:
        pass


def borrar():

    entradaAnchoEnX1.delete(0, END),
    entradaLargoEnY2.delete(0, END),
    entradaNumDeniv3.delete(0, END),
    entradatipDeEst4.delete(0, END),
    entradatipDeEst4.delete(0, END),
    entradaZonaSis5.delete(0, END),
    entradaTipSuelo6.delete(0, END),
    entradaCoefSis7.delete(0, END),
    entradaFacCompSis8.delete(0, END),
    entradaCoefSisRed9.delete(0, END),
    entradaFacRedCargaVer10.delete(0, END),
    entradaFacRes11.delete(0, END),
    entradaFacCar12.delete(0, END),
    entradaTipDeM13.delete(0, END),
    entradaAltura14.delete(0, END),
    entradaNumEspesor15.delete(0, END),
    entradatipResCompDisenoDeLaMamp116.delete(0, END),
    #entradaResCompDisenoDeLaMamp1v117.delete(0, END),
    entradaResCompDiaDisDeLaMamp218.delete(0, END),
    #entradaResCompDiaDisDeLaMamp2v219.delete(0, END),
    entradaOeso20.delete(0, END),
    entradaAncho21.delete(0, END),
    entradaLargo22.delete(0, END),
    entradaResConComp23.delete(0, END),
    entradaEsfFluenEspeAceRefuer124.delete(0, END),
    #entradaEsfFluenEspeAceRefuer1v125.delete(0, END),
    entradaAreaAceTotal26.delete(0, END),


#Botonera
botoneraX = 450

botonCalcular = Button(frameUno, command = calcular, text = "Calcular").place (x= botoneraX, y=60)
botonBorrarTodo = Button(frameUno, command = borrar, text = "Borrar Todo").place (x= botoneraX, y=95)
botonExportar = Button(frameUno, text = "Exportar data a .txt").place (x= botoneraX, y=130)




raiz.mainloop()