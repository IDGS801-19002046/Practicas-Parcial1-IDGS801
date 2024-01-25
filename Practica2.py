from flask import Flask,render_template,request


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

        
   
if __name__== "__main__":
    app.run(debug=True)

