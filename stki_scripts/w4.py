"""
author rochanaph
September 21 2017
"""
import w3, os, math

def bow(list_token):
    """
    fungsi untuk mengubah teks menjadi representasi numerik atau disebut vektor fitur.
    vektor fitur sederhana dapat berupa list dengan elemen numerik.
    :param list_token: input berupa list of token yang telah melalui pre-proses
    :return: vektor fitur bag of words
    """
    vocab = list(set(list_token)) # mencari kata yg unik
    bow_dict = {}  # membuat dictionary kosong untuk diisi nilai kata, jumlah kemunculan
    for item in vocab:
        bow_dict[item] = list_token.count(item) # key, value diisi kata, jumlah kemunculan
    return bow_dict

def sortdic(dic, isi, baris, descending=True, n=None):
    """
    fungsi untuk mengurutkan dictionary hasil representasi bag of words
    :param dic: dictionary key,value = string,int
    :param descending: parameter utk menentukan urutan menaik/menurun
    :param n: jumlah elemen yg ingin ditampilkan
    :return: dictionary bag of words yg sudah terurut berdasarkan value jumlah kata
    """
    # python 3
    # key = list(dic.keys())
    # val = list(dic.values())
    # python 2
    key = dic.keys()
    val = dic.values()
    isi = isi.values()
    baris = baris.values()

    
    key_ordered = [x for _, x in sorted(zip(val, key), reverse=descending)][:n]
    isi_ordered =  [x for _, x in sorted(zip(val, isi), reverse=descending)][:n]
    baris_ordered =  [x for _, x in sorted(zip(val, baris), reverse=descending)][:n]
    val_ordered = sorted(val, reverse=descending)[:n]

    ## python 3
    # return list(zip(key_ordered,val_ordered))
    # python 2
    return zip(key_ordered,val_ordered,isi_ordered,baris_ordered) [:n]



def l2_normalizer(vector):
    """ 
    fungsi untuk normalisasi L2 terhadap vektor dalam matrix
    :param vector:
    :return:
    """
    denom = sum([item**2 for item in vector])
    return [(item / math.sqrt(denom)) for item in vector]

def matrix(list_of_bow, normalized=False):
    """
    membuat matrix representasi bag of words.
    baris dari matrix sejumlah banyaknya dictionary bow.
    sedangkan kolom dari matrix sejumlah banyaknya vocab unik dari semua bow.
    :param list_of_bow: list yg berisi bbrp dictionary bow
    :return: matrix representasi bow
    """
    # menyimpan vocab unik terurut abjad dari semua bow
    vocab_all = []
    jumlah_artikel = len(list_of_bow)
    for item in list_of_bow:
        vocab_all.extend(item.keys())
    vocab_all = sorted(list(set(vocab_all)))

    # membuat matriks kosong dengan ukuran jumlah bow x jumlah vocab unik
    matrix_result = []
    for i in range(jumlah_artikel):
        matrix_result.append([])

    # append jumlah kata utk msg2 artikel dengan urutan menurut vocab unik terurut abjad
    for j in range(jumlah_artikel):
        for kata in vocab_all:
            if kata not in list_of_bow[j].keys():
                matrix_result[j].append(0)
            else:
                matrix_result[j].append(list_of_bow[j][kata])

    # apabila parameter normalized False, return matrix
    # apabila parameter normalized True, lakukan normalisai L2 pada matrix, return matrix
    if not normalized:
        return matrix_result

    else:
        for i in range(len(matrix_result)):
            matrix_result[i] = l2_normalizer(matrix_result[i])
        return matrix_result