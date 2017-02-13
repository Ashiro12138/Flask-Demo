from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    method = request.method
    if method == "GET":
        return render_template("forms.html")
    text1 = request.form["text1"]
    password1 = request.form["password1"]
    red = request.form.get("red")
    blue = request.form.get("blue")
    green = request.form.get("green")
    dic = {"green":green, "blue":blue, "red":red}
    choice = request.form["size"]

    return render_template("forms.html",
                            method=method,
                            text1=text1,
                            password1=password1,
                            dic=dic,
                            choice=choice,
                            )

if __name__ == "__main__":
    app.run(debug=True)
