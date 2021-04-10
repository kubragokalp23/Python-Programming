# -*- coding: utf-8 -*-
"""DSE_Veri_Bilimi_Eğitimi_3_Hafta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fKFUDS7g0P7MdG4QAN39bFXtzX5v67WI

# List Comprehensions
"""

#Örnek Senaryo: Bir listedeki çift sayıları getirelim
listem=list(range(10))

listem

ciftsayiListem=[]
for sayi in listem:
  if sayi % 2 == 0:
    ciftsayiListem.append(sayi)

ciftsayiListem

ciftsayiListem=[i for i in listem if i % 2 == 0]
ciftsayiListem

ciftsayiListem2=[i for i in listem if i % 2 == 0 or i % 3 == 0 if i > 5 ]
ciftsayiListem2

"""# Yardımcı Metotlar"""

#map

def f1(x):
  return x**2

lambda x: x**2

liste1=[1,2,3,4,5,6]

list(map(lambda x: x**2,liste1))

liste=[1,2,3]
print(list(map(lambda x: x**2,liste)))

kiyasListesi1=[1,3,5,7]
kiyasListesi2=[4,2,5,9,11,23,2,4]

list(map(lambda x,y: x if x>y else y,kiyasListesi1,kiyasListesi2))

# print(list(map(lambda x,y: x if x<y else y,kiyasListesi1,kiyasListesi2)))

"""

---

"""

# zip

zipListe1=[1,2,3,4]
zipListe2=["A","B","C","Ç","D"]
zipListe3=["F","T"]

#print(list(zip(zipListe1,zipListe2)))

list(zip(zipListe1,zipListe2,zipListe3))

for i,s in list(zip(zipListe1,zipListe2)):
  print(f'{i}. harf: {s}')

"""

---

"""

# reduce

sayilar=[1,2,6,6,22,76,2,12,7]

from functools import reduce

reduce(lambda x,y: x if x>y else y,sayilar)

"""

---

"""

# filter

kisiler = ['Sinan', 'Erdinç', 'Mehmet']
tarihler = [2018, 2017, 2020]

zipped=zip(kisiler,tarihler)
# list(zipped)
list(filter(lambda eleman:2018<=eleman[1]<=2020,zipped))[0]

list(zipped)



"""#Sözlükler (Dictionary)"""

#json
#Kişi json
"""
{
    "isim":"Fethi",
    "yas":24
 "dersler":[]
}
"""


"""
<isim>Fethi</isim>
<yas>24</Yas>
"""



d = {}
"isim"-"fethi"
"soyisim"-"tekyaygil"
"yaş"-24
1-"okunan okul sayısı"
"isim2"-"fethi"

print(d)

liste1={}

#{"Key":"Value"}
d = {"Course":"Python", "Week":3}
print(d)

print(d["Week"])

print(d["Week"])

d2 = {"Game":"Silent Hill 2", "Music":"Promise" }

d2

d2["Characters"] = ["James Sunderland","Maria","Angela Orosco"]

d2
#print(d2)

d2["Music"] = "Promise Reprise"

print(d2.keys())

list(d2.values())[2]

d2.items()

[print(i) for i in d2.keys()]

print(d)

for v in d.values():
  print(v)


[print(i) for i in d.values()]

d2.items()

for key,value in d2.items():
  print(key,value)

d.items()

for k,v in d.items():
  if v == 2:
    print(k)

print(d)

d["a"] = [3,4,5]
d

d={"course":"Turkish","course":"German"}
d

d.keys()

d.pop("course")
d

del d["course"]

d

len(d)

"German" in d

"a" in d

"python" in d

"a" in d.values()

d2

d2.get("artificial")

print(d2.get("asli"))

d2

del d2["deep"]
d2

d4 = {"insan":2, "kedi":4, "örümcek":8}
"""
for i in d4:
  ayak = d4[i]
  print("%s canlısının %d adet ayağı bulunur" % (i,ayak))
  print(str(i) + " canlısının " + str(ayak) +" adet ayağı bulunur.")
  """

for key,value in d4.items():
  print("%s canlısının %d adet ayağı vardır" % (key,value))

import math as m
f=m.floor(18.7)
f
c=m.ceil(18.7)
c
"""
i=17
flo=float(i)
flo
"""

d4 = {"insan":2, "kedi":4, "örümcek":8}
for i in d4:
  print(i)

d4 = {"insan":2, "kedi":4, "örümcek":8}

for i,ayak in d4.items():
  print(str(i) + " canlısının " + str(ayak) +" adet ayağı bulunur.")

ilceler = {"İstanbul":["Bostancı", "Beşiktaş", "Kadıköy"], 
           "Ankara":["Çankaya", "Gölbaşı", "Kızılcahamam"],
           "İzmir":["Çeşme","Bornova","Foça"]}

ilceler["İstanbul"]

type(ilceler)

type(ilceler["Ankara"])

ilceler["İzmir"]

ilceler["İzmir"][1:3]

ilceler["İzmir"][2]

#listeden sözlük oluşturma
0-1-2-3-4-5-6-7-8
sayilar = list(range(9))
"""
{"key":"value"}
continue
"""
cift_kare = {x: x**2 for x in sayilar if x % 2 == 0}

print(cift_kare)

"""#Kümeler (Sets)"""

bosSet={}

type(bosSet)

bosSet=set()

d={"key":"value"}

s = {"python", 5,6,8,5,6,"abc", "python"}
s

liste=[0,1,2,2,1,1,1,1,"Fethi",1,False,True] # -> True: 1 False: 0

list(set(liste))

bos2 = {}
type(bos2)

s2 = set(["python", 5,6,8,5,6,"abc", "python"])
print(s2)

an = set("ananas")
print(an)

[1,2,3]

y = {"a","b",[1,2,3],5,6}
print(y)

s2

6 in s2

s2[0]

9 in s2

len(s2)

list.append
list[4]=""

dict["yeni"]=yenival

s2

s2.add("ai")
len(s2)

s2.remove("ai")

s2.add("ai")
print(s2)
len(s2)

s2.remove("ai")
print(s2)

s2.pop()

from math import sqrt #squareroot karekök


#import math

print(sorted(list({sqrt(x) for x in list(range(10))})))

"""# Demetler(Tuples)"""

bosDemet=()
type(bosDemet)

demet = (1,2,3,4,5)
print(demet)
print(type(demet))

lDemet=list(demet)
lDemet.append("F")
demet=tuple(lDemet)
demet

demet[1]

del demet

{}
set()

demet2 = ()  #boş bir listeyi de, liste = [] olarak tanımlayabiliyorduk.
type(demet2)

girisBilgileri=("kAdi","sifre")

demet=(1,2,3,5,"Fethi")

demet

print(demet[3])

demet[-2]

demet[:4:2]

dm3 = ("asli", 5, 8, "eylul")
dm3.index("eylul")

dm3.count(5)

dm4 = ("elma","armut","çilek")

dm4[0] = "kiraz"

print(dm4)

dm4.remove("armut")

# demetlerin anahtar olduğu bir sözlük oluşturalım.

sozluk = {(x, x+1): x for x in range(10)}
print(sozluk)

demet5 = (5,6)

print(type(demet5))

sozluk[demet5]

sozluk[(3,4)]