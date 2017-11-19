"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os, sys

reload(sys)  
sys.setdefaultencoding('utf8')

def findSim(keyword, path):

    # membuat dictionary articles
    # membaca semua file .txt yang berada di direktori path(text files)
    # kemudian dimasukan kedalam dictionary articles dengan nama item/index(nama dokumen)
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    kata_kunci = 'keyword_index'
    articles[kata_kunci] = w3.prepro_base(keyword)

    #menyimpan baris pertama dari dokumen dan menyimpannya dalam dictionary
    isi_doc = {}
    for isi in os.listdir(path):
     if isi.endswith(".txt"):
         with open(path + isi,'r') as file:
             isi_doc[isi] = file.read()

    # membuat list list_of_bow
    # yang kemudian dimasukan token-token unik di setiap dokumennya
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # membuat matrix tiap-tiap dokumen dengan token unik dari semua dokumen
    matrix_akhir = w4.matrix(list_of_bow)

    # mencari id/urutan keyword_index
    # membuat dictionary presentase untuk semua dokumen
    id_keyword = articles.keys().index(kata_kunci)
    presentase = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != kata_kunci:
            presentase[key] = w5.cosine(matrix_akhir[id_keyword], vektor)

    #mencari baris dalam suati dokumen yang relevan dengan keyword
    baris = []
    c = w3.prepro_base(keyword)
    a = c.split()
    for item in os.listdir(path):
        if item.endswith(".txt"):
            files = open(path + item, 'r')
            for i in a:
                for line in files:
                    if i in w3.tokenize(w3.prepro_base(line)): baris.append(line)

    return w4.sortdic(presentase, isi_doc, baris, descending=True)


