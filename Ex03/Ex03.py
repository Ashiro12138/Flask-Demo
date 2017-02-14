from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/person",methods=["GET","POST"])
def person():
    if request.method == "GET":
        redirect(url_for('index'),code=301)
    return render_template("person.html")

@app.route("/forum",methods=["GET","POST"])
def forum():
    if request.method == "GET":
        redirect(url_for('index'),code=301)
    return render_template("forum.html")


if __name__ == "__main__":
    app.run(debug=True)
