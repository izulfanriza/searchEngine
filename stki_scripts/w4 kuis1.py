"""
author rochanaph
September 21 2017
"""
import os
import w3, w4

"""------------------BB------------------"""
## 1 mensederhanakan list of lists
def unlist(lista):
    res = []
    for item in lista:
        if type(item) != list:
            res.append(item)
        else:
            res.extend(unlist(item))
    return res
# print unlist([1,25,["a",["a","b"]],38,38,"c"])

## 2 cek palindrom
def palindrom1(text):
    tengah = len(text)/2
    if text[:tengah] == text[:-(tengah+1)]:
        print text, " merupakan palindrom"
    else:
        print text, " bukan palindrom"

def palindrom2(text):
    if "".join(reversed(text)) == text:
        print text, " merupakan palindrom"
    else:
        print text, " bukan palindrom"

# palindrom2("tamat")

## 3 membuat kombinasi kata menjadi frasa
def kombinasi(str):
    clean = w3.prepro_base(str) #pre-pro tanpa step stemming dan remove stopwords
    words = clean.split()
    res = []
    for i in range(0,len(words)-1):
        res.append(words[i]+" "+words[i+1])
    return res
def kombinasi2(str):
    clean = w3.prepro_base(str) #pre-pro tanpa step stemming dan remove stopwords
    words = clean.split()
    n = len(words)
    res = []
    for i in range(0,n-1):
        res.append(" ".join([words[i], words[i+1]]))
    return res

# print kombinasi("saya makan bakso bulat pingpong makan bakso")
# print kombinasi2("saya makan bakso bulat pingpong makan bakso")

## 4 melakukan bow pada frasa
# print w4.bow(kombinasi("saya makan bakso bulat pingpong makan bakso"))
# print w4.bow(kombinasi2("saya makan bakso bulat pingpong makan bakso"))


"""------------------AA------------------"""
# AA 2a
path = './text files/'
list_files = ["ed.txt","en.txt","lf.txt","ot.txt","tk.txt"]  # simpan nama file ke list

def read_to_dict(list_files):
    dic = {}
    for item in list_files:                         # untuk setiap file di dalam list files
        with open(path+item, 'r') as file:
            dic[item] = w3.preprotext(file.read())  # nama file sebagai key
    return dic                                      # hasil pre processing sbg value dlm dictionary dic

# print read_to_dict(list_files)

"""------------------AB------------------"""
## 1
def flip(lista):
    res = []
    n = int(len(lista)/2)
    res.extend(lista[n:])
    res.extend(lista[:(n)+1])
    return res
# print flip([1, 2, 3, 5, 10, 20])

## 2
def unik(lista):
    res = []
    for item in lista:
        if item not in res:
            res.append(item)
    return res

print unik(['saya', 'makan', 'besar', 'juga', 'makan', 'snack', 'besar'])
print list(set(['saya', 'makan', 'besar', 'juga', 'makan', 'snack', 'besar']))

## 3
path = "./text files"
list_of_files = os.listdir(path)
artikel_per_kategori = {}

for item in list_of_files:
    if item.endswith(".txt"):
        with open(path + "/" + item, 'r') as file:  # path lengkap dengan nama file

            if item[:2] not in list(artikel_per_kategori.keys()):
                artikel_per_kategori[item[:2]] = file.read()
            else:
                artikel_per_kategori[item[:2]] = artikel_per_kategori[item[:2]] + file.read()

print list(artikel_per_kategori.keys())
print artikel_per_kategori['en']
