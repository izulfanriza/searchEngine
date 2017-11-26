<<<<<<< HEAD
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField, validators
from stki_scripts.main import findSim

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword',[validators.DataRequired()])
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text_files/"
    res = findSim(keyword,path_corpus)
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    
    # render HTML
    return render_template('home.html', sform = sform, data = data)

@app.route('/text_files/<path:path>')
def opentext(path):
    fullpath = "./text_files/" + path
    resp = open(fullpath).read()
    return resp
    
if __name__=='__main__':
=======
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField, validators
from stki_scripts.main import findSim

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword', [validators.DataRequired()])
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text_files/"
    res = findSim(keyword, path_corpus)
    # res = {"title 1":0.3, "title 2":0.5, "title 3":1.3} # change the value here
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    
    # render HTML
    return render_template('home.html', sform = sform, data = data)

@app.route('/text_files/<path:path>')
def opentext(path):
    fullpath = "./text_files/" + path
    resp = open(fullpath).read()
    return resp
if __name__=='__main__':
>>>>>>> 38b67120c87b6c12abcb5bcb685e4e24f7f36668
    app.run(debug=True,port=5000)