from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/sendmail",methods=["POST"])
def sendmail():
    name = request.form["full_name"]
    date = request.form["booking_date"]
    text = request.form["special_requirements"]
    return render_template("result.html",name=name,date=date,text=text)

if __name__ == "__main__":
    app.run()
