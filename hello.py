from flask import Flask,render_template,abort,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
from werkzeug import SharedDataMiddleware
import os

# UPLOAD_FOLDER = r'C:\Users\24618\Documents\AAA-Term 1\AAA-IPT\Python\PY35\Flask-Demo\uploads'
UPLOAD_FOLDER = os.getcwd()+r'\uploads'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','doc','docx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#http://flask.pocoo.org/docs/0.12/patterns/fileuploads/#uploading-files

app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

banList = [] #Insert IPs

@app.before_request
def limit_remote_addr():
    if request.remote_addr in banList:
        abort(403)  # Forbidden

@app.route('/')
def index():
    #return render_template("blog.html")
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/mess',methods=['GET','POST'])
def mess():
    if request.method == 'GET':
        return redirect(url_for('index'),code=301)
    title = request.form['title']
    post = request.form['post']
    return render_template('formResult.html',title=title,post=post)

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

@app.route('/post/')
@app.route('/post/<int:post_id>')
def show_post(post_id=1):
    return 'Post %d' % post_id

@app.route('/blog/')
@app.route('/blog/<int:page>')
def show_blog(page=1):
    return render_template("blog.html")

#For chat app, have a look at this:
#https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
#And this http://callmephilip.github.io/chatzilla/

@app.route('/chat',methods=['GET','POST'])
def chat():
    f = open(os.getcwd()+r'\chat\chat.txt')
    l = [i.strip() for i in f]
    txt = "\n".join(l)
    return render_template("chat.html",txt=txt)

@app.route('/chatSubmit',methods=["POST"])
def chat_submit():
    msg = request.form['msg']
    f = open(os.getcwd()+r'\chat\chat.txt','a')
    f.write("\n"+msg)
    f.close()
    return redirect(url_for("chat"),code=301)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#File upload function
#State: Disabled

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename): #Remove this line and indent the lines under it to allow all file types
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <p><input type=file name=file>
#          <input type=submit value=Upload>
#     </form>
#     '''

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

# @app.route('/upload',methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/uploads'+secure_filename(f.filename))

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0', port=port)
    # app.run(debug=True)
