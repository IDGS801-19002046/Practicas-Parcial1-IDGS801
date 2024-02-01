from flask import Flask,render_template,request

import forms
import math


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

        
if __name__== "__main__":
    app.run(debug=True)