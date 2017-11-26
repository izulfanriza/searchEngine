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
    app.run(debug=True,port=5000)