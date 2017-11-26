from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField, validators
from stki_scripts.main import findSim
import urllib2,time

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='dendiGanteng'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword', [validators.DataRequired()])
    search = SubmitField('Search')

#deklarasi variabel global
awal = time
akhir = time
durasi = time

def searchTask(form):
    global durasi,awal,akhir #akses variabel global
    keyword = form.keyword.data
    path_corpus = "./text_files/"

    awal = time.time() #set globvar awal
    res = findSim(keyword, path_corpus)
    akhir = time.time() #set globvar akhir

    durasi = akhir - awal #set global durasi
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')
    c = 0
    # get response 
    data = {}
    data1 = durasi
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    for item in data:
        if item[1] != 0.0:
            c+=1
    # render HTML
    return render_template('home.html', sform = sform, data = data, data1=data1, counter=c)

@app.route('/text_files/<path:path>')
def opentext(path):
    fullpath = "./text_files/" + path
    resp = open(fullpath).read()
    return resp
if __name__=='__main__':
    app.run(debug=True,port=5000)