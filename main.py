from flask import Flask,render_template,request

import forms,formsexm,forms2
import math,archivotxt


app=Flask(__name__)


@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def resul():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion = request.form.get("operacion")


        if operacion == "suma":
              return"La suma de {} + {} = {}".format(num1,num2,str(int(num1)+int(num2)))
        elif operacion == "resta":
              return"La resta de {} - {} = {}".format(num1,num2,str(int(num1)-int(num2)))
        elif operacion == "multiplicacion":
            return"La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
        elif operacion == "division":
            if num2 != 0:
                  return"La division de {} / {} = {}".format(num1,num2,str(int(num1)/int(num2)))
            else:
                return "Error: División por cero no permitida"
        else:
            return "Error: Operación no válida"
        
@app.route("/distancia2",methods=["GET", "POST"])
def distancia2():
    p1x= float
    p2x= float
    p1y= float
    p2y= float
    resultado = 0
    
    distancia = forms.UserForm(request.form)
    if  request.method =='POST':
        p1x= distancia.p1x.data
        p2x= distancia.p2x.data
        p1y=distancia.p1y.data
        p2y=distancia.p2y.data
        print('Px1: {}',format(p1x))
        print('Px2: {}',format(p2x))
        print('Py1: {}',format(p1y))
        print('Py2: {}',format(p2y))
        
        resultado = math.sqrt(((p1y - p1x) ** 2) + ((p2y - p2x) ** 2))
        print(resultado)
        
    return render_template("distancia.html",form=distancia,p1x=p1x,p2x=p2x,p1y=p1y,p2y=p2y,resultado = resultado)

@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    b1 = 0
    b2 = 0
    b3 = 0
    tol = 0
    color1 = ''
    color2 = ''
    color3 = ''
    color4 = ''
    val = 0
    minimo = 0
    maximo = 0
    c1=0
    c2=0
    c3=0
    c4=0

    resistencias = formsexm.Resistencias(request.form)
    if request.method == 'POST':
        b1 = resistencias.b1.data
        b2 = resistencias.b2.data
        b3 = resistencias.b3.data
        tol = resistencias.tol.data

        if int(b1) == 0:
            color1 = 'Negro'
        elif int(b1) == 1:
            color1 = 'Cafe'
        elif int(b1) == 2:
            color1 = 'Rojo'
        elif int(b1) == 3:
            color1 = 'Naranja'
        elif int(b1) == 4:
            color1 = 'Amarillo'
        elif int(b1) == 5:
            color1 = 'Verde'
        elif int(b1) == 6:
            color1 = 'Azul'
        elif int(b1) == 7:
            color1 = 'Violeta'
        elif int(b1) == 8:
            color1 = 'Gris'
        elif int(b1) == 9:
            color1 = 'Blanco'

        if int(b2) == 0:
            color2 = 'Negro'
        elif int(b2) == 1:
            color2 = 'Cafe'
        elif int(b2) == 2:
            color2 = 'Rojo'
        elif int(b2) == 3:
            color2 = 'Naranja'
        elif int(b2) == 4:
            color2 = 'Amarillo'
        elif int(b2) == 5:
            color2 = 'Verde'
        elif int(b2) == 6:
            color2 = 'Azul'
        elif int(b2) == 7:
            color2 = 'Violeta'
        elif int(b2) == 8:
            color2 = 'Gris'
        elif int(b2) == 9:
            color2 = 'Blanco'

        c3 = ""
        if int(b3) == 1:
            color3 = 'Negro'
            c3 = "black"
        elif int(b3) == 10:
            color3 = 'Cafe'
            c3 = "brown"
        elif int(b3) == 100:
            color3 = 'Rojo'
            c3 = "red"
        elif int(b3) == 1000:
            color3 = 'Naranja'
            c3 = "orange"
        elif int(b3) == 10000:
            color3 = 'Amarillo'
            c3 = "yellow"
        elif int(b3) == 100000:
            color3 = 'Verde'
            c3 = "green"
        elif int(b3) == 1000000:
            color3 = 'Azul'
            c3 = "blue"
        elif int(b3) == 10000000:
            color3 = 'Violeta'
            c3 = "purple"
        elif int(b3) == 100000000:
            color3 = 'Gris'
            c3 = "gray"
        elif int(b3) == 1000000000:
            color3 = 'Blanco'
            c3 = "white"

        c4 = ""
        if float(tol) == 0.05:
            color4 = 'Dorado'
            c4 = "goldenrod"
        elif float(tol) == 0.1:
            color4 = 'Plateado'
            c4 = "silver"

        x = str(b1) + str(b2)
        val = int(x) * int(b3)
        minimo =  float(val) - float(val) * float(tol)
        maximo = float(val) + float(val) * float(tol) 

        c1 = Color(int(b1))
        c2 = Color(int(b2))
        print("El elemento seleccionado es:" + tol)

    return render_template("resistencia.html", form=resistencias, b1=b1, b2=b2, b3=b3,
                           color1=color1, color2=color2, color3=color3, color4=color4, val=val,
                           tol=tol, maximo=maximo, minimo=minimo, c1 = c1, c2 = c2, c3 = c3, c4 = c4)
    
def Color(number):
    if number == 0:
        return "black"
    elif number == 1:
        return "brown"
    elif number == 2:
        return "red"
    elif number == 3:
        return "orange"
    elif number == 4:
        return "yellow"
    elif number == 5:
        return "green"
    elif number == 6:
        return "blue"
    elif number == 7:
        return "purple"
    elif number == 8:
        return "gray"
    elif number == 9:
        return "white"
    
@app.route("/diccionario", methods=['GET','POST'])
def diccionario():
    esp = ''
    ing = ''
    idioma=''
    buscar= ''
    
    diccionario_clase = forms2.UserForm(request.form)
    if request.method == 'POST'and diccionario_clase.validate():
        esp = diccionario_clase.esp.data 
        ing = diccionario_clase.ing.data
        idioma = diccionario_clase.idioma.data
        buscar = diccionario_clase.buscar.data
        obj=archivotxt.Diccionario()
        
        if request.form['submitbtn']=='leer':
            obj.buscar(idioma,buscar)
        if request.form['submitbtn']=='agregar':
            obj.buscar(ing,esp)
        
        
    return render_template("diccionario.html", form=diccionario_clase, ing=ing, esp = esp, idioma=idioma, buscar=buscar)
       
if __name__== "__main__":
    app.run(debug=True)