from flask import Flask,request,render_template

app = Flask(__name__)

a2n = {
    "A+":15,"A":14,"A-":13,
    "B+":12,"B":11,"B-":10,
    "C+":9,"C":8,"C-":7,
    "D+":6,"D":5,"D-":4,
    "E+":3,"E":2,"E-":1,
}

n2a = {
    15:"A+",14:"A",13:"A-",
    12:"B+",11:"B",10:"B-",
    9:"C+",8:"C",7:"C-",
    6:"D+",5:"D",4:"D-",
    3:"E+",2:"E",1:"E-",
}

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template('index.html',method=request.method)
    try:
        score1 = request.form["score1"]
        score2 = request.form["score2"]
        score3 = request.form["score3"]
        score1 = a2n[score1]
        score2 = a2n[score2]
        score3 = a2n[score3]
        average = n2a[round((score1+score2+score3)/3)]
    except:
        return render_template('index.html',method=request.method,average=None)
    return render_template('index.html',method=request.method,average=average)


if __name__ == "__main__":
    app.run()
