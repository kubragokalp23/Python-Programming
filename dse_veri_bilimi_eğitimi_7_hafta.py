# -*- coding: utf-8 -*-
"""DSE_Veri_Bilimi_Eğitimi_7_Hafta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zle28AUsshkMMDFNZokNiIfQa3CsE2QN

# Dosya İşlemleri
"""

#Dosya açmak
# w write. -  dosya yoksa oluşturur ve açar varsa sadece açar
# r read

file = open("dosya.txt", "w", encoding='utf-8')

file.write("Python eğitimi çok harika!")

#dosyayı kapatıyoruz
file.close()

# Flaglar: 
# https://www.programiz.com/python-programming/file-operation

file = open("dosya.txt","w",encoding="utf-8")
file.write("İlk Satırım!\n")
file.write("İkinci Satırım!")
file.close()

try: 
  f = open("dosya.txt","asda")
finally:
  f.close()

"""## read"""

file = open("dosya.txt","r",encoding="utf-8")
print(file.read())
file.close()

file = open("dosya.txt","r",encoding="utf-8")
for line in file:
  print(line,end="")

file.close()

file = open("dosya.txt","r")
for line in file:
  print(line,end = '')


file.close()

file = open("dosya.txt","r")
print(file.readline())
print(file.readline())
file.close()

file = open("dosya.txt","r")
print(file.readlines())

file.close()

"""## write"""

file = open("dosya.txt","w+")
file.writelines(["İlk Satırım 3\n","İlk Satırım 4"])
print(file.readlines())
file.close()

file = open("dosya.txt","w+")
file.writelines(["İlk Satırım 3","\nİlk Satırım 4"])
print(file.tell())
file.seek(0)
print(file.readlines())
file.close()

file = open("dosya.txt","a",encoding="utf-8") #append
file.write("\nSon eklediğim satırım")
file.close()

"""## with"""

with open("dosya.txt", "a+", encoding="utf-8") as file2:
  file2.seek(10)
  file2.write("Sonradan Eklendi")
  file2.seek(0)
  print(file2.read()[:2])

"""# Veritabanı İşlemleri"""

import sqlite3

baglanti = sqlite3.connect("obs.db")

if(baglanti):
  cursor = baglanti.cursor()

#User oluştur

cursor.execute("DROP TABLE IF EXISTS Users;")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(100) NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Policy BIT NOT NULL
);
''') #Policy = 1 Öğrenci, 0 Öğretmen

#Lesson oluştur
cursor.execute("DROP TABLE IF EXISTS Lessons;")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Lessons(
  Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Code VARCHAR(10) UNIQUE NOT NULL
);
''')

# Student oluştur
cursor.execute("DROP TABLE IF EXISTS StudentLessonRelations;")
cursor.execute('''
CREATE TABLE IF NOT EXISTS StudentLessonRelations(
  UserId INT NOT NULL,
  LessonId INT NOT NULL,

  FOREIGN KEY (UserId) REFERENCES Users(Id),
  FOREIGN KEY (LessonId) REFERENCES Lessons(Id),
  UNIQUE(UserId, LessonId)
);
''')

# Lecturer oluştur
cursor.execute("DROP TABLE IF EXISTS LecturerLessonRelations;")
cursor.execute('''
CREATE TABLE IF NOT EXISTS LecturerLessonRelations(
  UserId INT NOT NULL,
  LessonId INT NOT NULL,

  FOREIGN KEY (UserId) REFERENCES Users(Id),
  FOREIGN KEY (LessonId) REFERENCES Lessons(Id),
  UNIQUE(UserId, LessonId)
);
''')

baglanti.commit()

#user ekle
cursor.execute('''
INSERT INTO Users(Username, Password, Name, Surname, Policy) 
VALUES('fethitekyaygil','123','Fethi','Tekyaygil',1);
''')

cursor.execute('''
INSERT INTO Users(Username, Password, Name, Surname, Policy) 
VALUES('tahatekyaygil','123','Taha','Tekyaygil',1);
''')


cursor.execute('''
INSERT INTO Users(Username, Password, Name, Surname, Policy) 
VALUES('hıdırsevinc','123','Hıdır','Sevinç',0);
''')

cursor.execute('''
INSERT INTO Users(Username, Password, Name, Surname, Policy) 
VALUES('yesimcalik','123','Yeşim','Çalık',0);
''')

cursor.execute('''
INSERT INTO Users(Username, Password, Name, Surname, Policy) 
VALUES('seferkurnaz','123','Sefer','Kurnaz',0);
''')


baglanti.commit()

# ders ekle
cursor.execute('''
INSERT INTO Lessons (Name,Code)
VALUES ('Python Programlama 101','PY101');
''')

cursor.execute('''
INSERT INTO Lessons (Name,Code)
VALUES ('Python Programlama 102','PY102');
''')

cursor.execute('''
INSERT INTO Lessons (Name,Code)
VALUES ('Matematik 101','MAT101');
''')

baglanti.commit()

cursor.execute("SELECT * FROM Users WHERE Policy = 0")

cursor.fetchall()

cursor.execute("SELECT * FROM Lessons")

cursor.fetchall()

# lecturer ekle
cursor.execute('''
INSERT INTO LecturerLessonRelations(UserId, LessonId)
VALUES(3,1);
''')

cursor.execute('''
INSERT INTO LecturerLessonRelations(UserId, LessonId)
VALUES(4,2);
''')

cursor.execute('''
INSERT INTO LecturerLessonRelations(UserId, LessonId)
VALUES(5,3);
''')

baglanti.commit()

cursor.execute("SELECT * FROM Users WHERE Policy = 1")
cursor.fetchall()

# student ekle
cursor.execute('''
INSERT INTO StudentLessonRelations(UserId, LessonId)
VALUES(1,1);
''')

cursor.execute('''
INSERT INTO StudentLessonRelations(UserId, LessonId)
VALUES(2,2);
''')

baglanti.commit()

cursor.execute('''
SELECT * FROM Users u
JOIN StudentLessonRelations slr 
ON u.Id = slr.UserId
''')

cursor.fetchall()

cursor.execute('''
SELECT u.Name,u.Surname,l.Code, u2.Name, u2.Surname FROM Users as u 
JOIN StudentLessonRelations as s ON u.Id = s.UserId
JOIN LecturerLessonRelations as llr ON llr.LessonId=s.LessonId
JOIN Lessons l ON l.Id=s.LessonId
JOIN Users as u2 ON llr.UserId = u2.Id
''')

cursor.fetchall()

cursor.execute("SELECT * FROM Users WHERE Name = 'Hıdır'")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Lessons WHERE Code = 'PY101'")
print(cursor.fetchall())


cursor.execute("SELECT * FROM LecturerLessonRelations WHERE UserId = 3")
print(cursor.fetchall())

cursor.execute('''
SELECT u.Name, u.Surname,l.Code FROM Users u 
JOIN LecturerLessonRelations llr ON u.Id = llr.UserId
JOIN Lessons l ON l.Id = llr.LessonId WHERE u.Id=3''')

cursor.fetchall()

cursor.execute('''
SELECT * FROM Users as u
JOIN LecturerLessonRelations as llr
ON u.Id = llr.UserId
JOIN Lessons as l
ON llr.LessonId = L.Id
''')

cursor.fetchall()

cursor.execute('''
SELECT u.Name,u.Surname,l.Name FROM Users as u
JOIN LecturerLessonRelations as llr
ON u.Id = llr.UserId
JOIN Lessons as l
ON llr.LessonId = L.Id
''')

print(cursor.fetchall())
"""
print(cursor.fetchone())
print(cursor.fetchone())
"""

cursor.execute('''
SELECT u.Name,u.Surname,l.Name FROM Users as u
JOIN LecturerLessonRelations as llr
ON u.Id = llr.UserId
JOIN Lessons as l
ON llr.LessonId = L.Id
''')

print(cursor.fetchone())
print(cursor.fetchone())

cursor.execute('''
SELECT u.Name,u.Surname,l.Name FROM Users as u
JOIN LecturerLessonRelations as llr
ON u.Id = llr.UserId
JOIN Lessons as l
ON llr.LessonId = L.Id
''')

print(cursor.fetchmany(1))

cursor.execute('''
SELECT * FROM Users
''')
print(cursor.fetchmany(2))

cursor.execute('''
SELECT * FROM Users
''')

for record in cursor:
  print(record)

username = input("Please your username: ")
password = input("Please your password: ")

cursor.execute('''
  SELECT * FROM Users WHERE username = ? AND password = ?
''',(username,password))

cursor.fetchall()