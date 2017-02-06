from flask import Flask,render_template,abort,request
import os
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
def numbers(wrong=0):
    total = ''
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            wrong=0
        except ValueError:
            wrong=1
            return render_template("numbers.html",wrong=wrong)
        result = num1 + num2
        return render_template("numbersResult.html",num1=num1,num2=num2,result=result)
    else:
        return render_template("numbers.html",wrong=wrong)

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
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)
