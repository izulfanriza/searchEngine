"""
author rochanaph
August 20 2017
"""

## list
list = [ 'abcd', 786 , 2.23, 'john', 70.2, 123 ]
tinylist = [123, 'john']
#
# # append
# resapp = []
# for item in list*2:
#     resapp.append(item)
# print (resapp)
#
# # extend
# restend = []
# for item in [list,tinylist]:
#     restend.extend(item)
# print (restend)

# comprehension
print ([item for item in list if item not in tinylist])
# normal for
new = []
for item in list:
    new.append(item)
for item in tinylist:
    while item in new:
        new.remove(item)
print new

## function
# define
def hello():
    print("Hello, World!")
hello()

# parameter
def add_numbers(x, y, z): # x, y, z adalah parameter
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

add_numbers(1, 2, 3)

# keyword argument dan default
def profile_info(username, followers, num=5000):    # username, followers adalah parameter keyword argument
    print("Username: " + username)                  # num adalah default keyword argument
    print("Followers: " + str(followers))
    print("Salary: " + str(followers*num))

profile_info(username="rochana", followers=1000 )   # tidak masalah utk keyword argument yg memiliki nilai default utk tidak inputkan value

# function dengan condition dan for
def ngram(str, n=2):
    listof = str.split()
    result = []
    for i in range(len(listof)-(n-1)):
        if i != len(listof)-(n-1):
            res = []
            for x in range(n):
                res.append(listof[i + x])
            fin = " ".join(res)
            result.append(fin)
    return result
print (ngram("saya makan bakso bulat pingpong"))


## conditional
threshold = 70
nilai = int(raw_input("inputkan nilai: "))
kuis = int(raw_input("inputkan nilai kuis: "))
if nilai < threshold:
    if kuis != 0:               # baris 71-74 if else, 1 kondisi
        print "boleh remidi"    # baris 70-74 nested if, setelah memenuhi kondisi1 dicek lagi kondisi selanjutnya
    else:
        print (str(nilai)+" gagal")
elif nilai == threshold:
    print "boleh remidi"
else:
    print "lulus dengan nilai: " + str(nilai) # baris 70-78 if elif else, > 1 kondisi


# ## loop
# # break
# number = 0
# for number in range(10):
#    number = number + 1
#    if number == 5:
#       break    # break here
#    print('Number is ' + str(number))
# print('Out of loop')
#
# # continue
# number = 0
# for number in range(10):
#    number = number + 1
#    if number == 5:
#       continue    # continue here
#    print('Number is ' + str(number))
# print('Out of loop')
#
# # pass
# number = 0
# for number in range(10):
#    number = number + 1
#    if number == 5:
#       pass    # pass here
#    print('Number is ' + str(number))
# print('Out of loop')

#
#
# # pertanyaan titi tentang membuat counter
# i = 0               # init i
# for x in range(5):  # x yg diiterasi
#     print x*i
#     i+=2            # init i berubah nilainya
#
# print "----"
# for i in range(5):  # i yg diiterasi
#     print i*2
#     i+=2            # i nggak bisa diupdate valuenya, krn nerusin iterasi
#
# # pertanyaan titi tentang input boolean
# # sepertinya tdk ada buitin function yg bener2 bisa detect value bool, harus ditambahkan condition sendiri
# print "----"
# res = []
# for i in range(6):
#     value = raw_input()
#     if value == "True" or value == "1":
#         res.append( bool(value))
#     else:
#         res.append( bool(""))
# print res