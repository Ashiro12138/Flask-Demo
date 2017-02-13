from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    method = request.method
    return render_template("forms.html",method=method)

if __name__ == "__main__":
    app.run()
