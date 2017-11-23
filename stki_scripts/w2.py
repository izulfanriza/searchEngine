# """
# author rochanaph
# August 20 2017
# """
#
# # read
path = './text files/bk.txt'
artikel = open(path,'r')
rd = artikel.read()
artikel.close()

artikel = open(path,'r')
rl = artikel.readline()
artikel.close()

artikel = open(path,'r')
rls = artikel.readlines()
artikel.close()

print "1, ", rd
print "2, ", rl
print "3, ", rls
# print "4, ", wl

# langsung close
with open(path,'r') as file:
    print file.readlines()[:3]

# write
new_path = './text files/bk_new.txt'
new_artikel = open(new_path,'w')
new_artikel.write("ini line baru write dr python."+"\n")
new_artikel.close()

artikel = open(new_path,'r')
wl = artikel.readlines()
artikel.close()

with open(new_path,'w') as file:
    file.write("ini line baru write dr python." + "\n")


# string manipulation
print rd
print rd.lower() # melowerkan karakter dlm string
print rd.upper() # mengupperkan karakter
print rd.split(".") # memecah string berdasarkan separator, defaultnya spasi
print "&".join(rd.split()) # menggabungkan semua string dalam list dengan karakter tertentu
print rd.replace(" ","(spasi)") # find-replace parameter kiri dengan parameter kanan
print len(rd) # jumlah karakter

import os
path = './text files'
print os.listdir(path) # melist semua nama file dalam path
articles = {}
for item in os.listdir(path):
    if item.endswith(".txt"):
        with open(path + "/" + item, 'r') as file:  # path lengkap dengan nama file
            articles[item] = file.readline()
print articles
print articles["lf.txt"]

print "^".join("saya suka bakso")
print "^".join(["saya" ,"suka" ,"bakso"])
