# -*- coding: utf-8 -*-
"""DSE_Veri_Bilimi_Eğitimi_2_Hafta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KLTI1dsmud0svP3QGeFqHc-dPj-hnHvO

# Listeler
"""

List<int> liste1=new List<int>();

liste2=["Fethi",7,True,2.7]

liste2

len(liste2) #length

type(liste2)

print(type(liste2[0]))
print(type(liste2[1]))

liste1 = ["2", 1, True]

liste1

type(liste1)

type(liste1[0])

"""# Karakter Dizileri (Strings) ve İndeskleme (Indexing)"""

stringDeger="Fethi"
type(stringDeger)

hello = 'Hello'
world = "World"

print(hello)
print(type(hello))

isim="Fethi?*'., /123290"

len(isim)

print(len(hello))
print(world, len(world))
#print(f"world {len(world)}")

"""
c char
s string
d decimal
"""
#C dili
#world2 = '%s %d %s' % (world, len(world),hello)
print('%s %d %s' % (world, len(world), hello))

print(1.0+2)

print(world +" "+ str(len(world)))
#World+ +5=World 5

print(world+": " + str(len(world)))
print(world,str(len(hello)))
print(world + " " + str(len(world)))
#World: 5

print(hello)

liste=[1,2,"Fethi",True,7]

print(liste[4])
"""n elemanlı bi listem varsa sonuncu elemanı n-1
5 elemanlı bi listem varsa sonuncu elemanı 4"""

liste

print(type(liste[2])) # -> str
print(type(liste[1])) # -> int

liste

"""print(liste[4])
print(liste[-1])
print(liste[-5])
print(liste[0])"""
print(len(liste))

# İndekslemeler

liste2

#75 - > 0 <-> 74  standart indeksleme
#75 - > -1  <-> -75 tersine indeksleme

isim="Fethi"

"""
F   -   0
e   -   1
t   -   2
h   -   3
i   -   4
"""

ornek[74]
#ornek[-2]

isim[2]

5 - 1

ornek="abc"*25
ornek

print(ornek[74]==ornek[-1])

Fethi

F -   -5
i -    4

hello

print(hello[0])
print(hello[1])

world= "World"

print(world)

W - 0 <-> -5
o - 1 <-> -4
r - 2 <-> -3
l - 3 <-> -2 
d - 4 <-> -1

print(world[-1])
print(world[-3])

print("a"+" b")
print(1+4)
print("7"+4)

world[-6]

"""
print(fethi[-6])

print(fethi[-6]==fethi[0])
"""
fethi = " fethi" 
len(fethi)

" fethi"

print(fethi[1])

print(fethi[-2])

fethi[-10]

fethi[-6]
print("f")

print(fethi[-1])

print(hello)

print(fethi)
list(fethi)

list(8)

list(hello)

# Slicing

isim="Fethi"

isim

F e t h i

"""
Index sınır dışında olsa bile çalışmasının sebebi:

ndeksleme, tek bir öğeyi döndürür, ancak slicing bir aralık dizisini döndürür. Dolayısıyla, var olmayan bir indeks üzerinde indeksleme yaptığınızda 
döndürülecek bir şey yoktur. Ancak bir diziyi sınırların dışında dilimlediğinizde, yine de boş bir dizi döndürebilirsiniz.

"""
isim[6:12]

isim="Fethi Tekyaygil"

#isim[0:12]
isim[:12]

len(isim)

isim

isim[5:]

isim[5:]

isim[:]
#cepte

#slicing -> kesme (parça alma)
hello[2:4]  # [x:y] --> x ten y. karaktere kadar al ama y. karakteri alma.

list(world)

world[1:4]

print(world[1:5])

print(world[1:])

print(world[0:3])

print(world[:3])

print(world[:])

list(world)

"""slicing'te işlem soldan sağa indeks numaralarıyla yapılır"""

isim="Fethi Tekyaygil"

F e t h i

isim[-3:-1]

isim[5:-1]

Tekyaygi

isim[5:len(isim)-1]

len(isim)-1

Fethi Tekyaygil

print(world[-3:-1])

print(hello)

hello[:4]

hello[:]

Hello

"""
tip dönüşümü yapacaksanız
class-tip(dönüştüreceğiniz değer)
"""



list(range(0,11,2))

r=range(110,-10,-10)
list(r)

sayilarListesi=list(range(110,-10,-10))
sayilarListesi

l1=range(21)

list(l1)

list(l1[::-5])

ciftler=l1[7::5]
list(ciftler)

import random


sayilar=range(101)

rastgele1=random.choice(sayilar)
print(rastgele1)

rastgele2=random.randint(0,100)
print(rastgele2)

?random.randint()

sayilarListesi

ciftler=sayilarListesi[::5]
ciftler

sayilarListesi[::-1]

hello[::-1]

print(world)

print(world[:-3])
print(world[:2])

print(hello)

hello[2:5]

world[2:4:1]   # [başlangıç:bitiş:step_sayısı]
world[2:4]

liste1=[1,2,3,4,5]
liste1[::2]

city = "istanbul"
city[0:6:2]

itn

import random
listeSahin=list(range(0,101))

r1=random.choice(listeSahin)

listeSahin.remove(r1)

?random.choice()

city

"t" in city

"y" in city

"anb" in city

for ch in ["s","n","l"]:
  print(ch in city)

"S" in city

type(2)

n = 10
str(n)

s = '13'
print(type(s))
s=int(s)
print(type(s))

s = 'ist'
int(s)

m = 8
print(type(m))
m=float(m)
print(m)

ai = 'artificial' + ' ' + 'intelligence'
print(ai)

"""# String Operasyonları"""

word = 'Fethi Tekyaygil'

word.capitalize()

word.upper()

word.lower()

word

word=word.lower().replace("t",'F')

word=word.replace("a","e")

word

word.lower().replace("t","F")

?word.replace()

?str

?ml2.replace

ml2="machine learning"
ml2_yeni=ml2.replace("a","e").replace("l","i")
print(ml2_yeni)

word

Kullanıcı Adı: "fethi" != "fethi"
Şifre: " 123"

word2 = "          artificial general      intelligence    "
print(word2.strip())
len(word2.strip())

?input

sayi=input("Bana sayı ver: ")
sayi=int(sayi)
sayi+=1
print(sayi)

y = input("Please enter a city name: ")  #input her zaman string alır

print(y)
print(type(y))

x = int(input("Please enter an integer: "))
print(x)
print(type(x))

month = 12
day = 365

print('Bir yıl', month, 'ay,', day, 'gündür.', sep =' ') #seperator ayırtaç ayırıcı
print('Bir yıl ', month, ' ay, ', day, ' gündür.', sep ='')

print("Bir yıl " + str(month) + " ay, " + str(day) + " gündür.")