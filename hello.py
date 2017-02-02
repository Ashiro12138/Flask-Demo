from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    return render_template("profile.html",username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/blog/')
@app.route('/blog/<int:page>')
def show_blog(page=1):
    return render_template("blog.html")

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run()