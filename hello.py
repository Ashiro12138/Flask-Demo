from flask import Flask,render_template,abort,request
app = Flask(__name__)

banList = [] #Insert IPs

@app.before_request
def limit_remote_addr():
    if request.remote_addr in banList:
        abort(403)  # Forbidden

@app.route('/')
def index():
    #return "Welcome to the index"
    #return render_template("blog.html")
    return render_template('form.html')

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    return render_template("profile.html",username=username)

@app.route('/numbers',methods=['GET','POST'])
def numbers():
    total = ''
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        return "The sum of {} and {}".format(num1,num2) + " is {}".format(str(num1+num2))
    else:
        return render_template("numbers.html")

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/blog/')
@app.route('/blog/<int:page>')
def show_blog(page=1):
    return render_template("blog.html")

@app.route('/mess',methods=['POST'])
def mess():
    title = request.form['title']
    mess = request.form['post']
    return "<h1>"+title+"</h1>"+"<br>"+"<p>"+mess+"</p>"

@app.route('/chat/')
def chat():
    return "Chat in develop"

if __name__ == "__main__":
    app.run(debug=True)
