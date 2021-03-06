# -*- coding: utf-8 -*-
"""DSE_Veri_Bilimine_Giriş_Proje_Eğitimleri.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O0uybSeH5zUxQRji67A-gjYYt53KSaUh
"""

#Öğrenci Bilgilendirme Sistemi

"""Öğrenciler
  Dersler -> Notlar -> Midterm -> Final
  Sınıflara Göre Ders Ortalaması
  Bölüm,
  Devamsızlık Bilgisi,
  Giriş Yılı

1. Kullanıcılar

2. Dersler

3. Notlar

## Veritabanı
"""

import sqlite3

baglanti = sqlite3.connect("obs.db")

class SqlQueries():
  def __init__(self, sqlQueries,operation="r"):
    self.sqlQueries = sqlQueries
    self.operation = operation

class SqlQuery():
  def __init__(self,query,parameters=()):
    self.query=query
    self.parameters=parameters

class DbOperations():
  def __init__(self,baglanti):
    self.baglanti=baglanti
    self.cursor = baglanti.cursor()

  def ExecuteSql(self,sql_queries):
    try:
      for sql_query in sql_queries.sqlQueries:
        self.cursor.execute(sql_query.query,sql_query.parameters)
      if sql_queries.operation == "r":
        return self.cursor.fetchall()
      else:
        self.baglanti.commit()
    except Exception as e:
      print(str(e))
      """
  def GetUsers(self):
    print(self.ExecuteSql(SqlQueries([SqlQuery("SELECT * FROM Users")])))

  def GetDepartments(self):
    print(self.ExecuteSql(SqlQueries([SqlQuery("SELECT * FROM Departments")])))
    """

class DbCreateOps(DbOperations):
  def __init__(self,baglanti):
    super().__init__(baglanti)


  def InitializeDatabase(self):
    self.CreateDepartmentsTable()
    self.CreateUsersTable()
    self.CreateLessonsTable()
    self.CreateGradesTable()


  def CreateUsersTable(self):
    query='''
      CREATE TABLE IF NOT EXISTS Users(
      Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      Name VARCHAR(30) NOT NULL,
      Surname VARCHAR(30) NOT NULL,
      Username VARCHAR(60) UNIQUE NOT NULL,
      Password VARCHAR(40) NOT NULL,
      DepartmentId INTEGER NOT NULL,
      Policy BIT NOT NULL,

      FOREIGN KEY(DepartmentId) REFERENCES Departments(Id) 
      );
      '''
      
    sql_query = SqlQuery(query=query)
    sql_queries = SqlQueries([sql_query],operation="c")

    self.ExecuteSql(sql_queries) #Policy = 1 Öğrenci , Policy = 0 Öğretmen
      
  def CreateLessonsTable(self):
    query = '''
      CREATE TABLE IF NOT EXISTS Lessons(
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name VARCHAR(50) NOT NULL UNIQUE,
        Code VARCHAR(10) NOT NULL UNIQUE,
        Midterm1Effect INTEGER NOT NULL,
        Midterm2Effect INTEGER NOT NULL,
        FinalEffect INTEGER NOT NULL,
        DepartmentId INTEGER NOT NULL,


        FOREIGN KEY(DepartmentId) REFERENCES Departments(Id) 
      );
    '''

    sql_query = SqlQuery(query=query)
    sql_queries = SqlQueries([sql_query],operation="c")
    self.ExecuteSql(sql_queries)


  def CreateDepartmentsTable(self):
    query = '''
    CREATE TABLE IF NOT EXISTS Departments(
      Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      Name VARCHAR(50) UNIQUE NOT NULL
    );
    '''

    sql_query = SqlQuery(query=query)
    sql_queries = SqlQueries([sql_query],operation="c")
    self.ExecuteSql(sql_queries)

  def CreateGradesTable(self):
    query = '''
      CREATE TABLE IF NOT EXISTS Grades(
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

        UserId INTEGER NOT NULL,
        LessonId INTEGER NOT NULL,

        Midterm1 INTEGER NULL,
        Midterm2 INTEGER NULL,
        Final INTEGER NULL,
        ExtraNote INTEGER NULL,

        GeneralGrade INTEGER NULL,

        FOREIGN KEY(UserId) REFERENCES Users(Id),
        FOREIGN KEY(LessonId) REFERENCES Lessons(Id)
      );
    '''
    
    sql_query = SqlQuery(query=query)
    sql_queries = SqlQueries([sql_query],operation="c")
    self.ExecuteSql(sql_queries)

class DbInsertOps(DbOperations):
  def __init__(self,baglanti):
    super().__init__(baglanti)

  def InitializeRecords(self):
    self.InsertDepartmentRecords()
    self.InsertUserRecords()
    self.InsertLessonRecords()
    self.InsertGradeRecords()


  def GetDepartmentIdsForInsert(self):
      ce_sql_query = SqlQuery(query = "SELECT Id FROM Departments WHERE Name = ?", parameters=("Computer Engineering",))
      ie_sql_query = SqlQuery(query = "SELECT Id FROM Departments WHERE Name = ?", parameters=("Industrial Engineering",))
      me_sql_query = SqlQuery(query = "SELECT Id FROM Departments WHERE Name = ?", parameters=("Mechanical Engineering",))

      ce_id = self.ExecuteSql(SqlQueries([ce_sql_query]))[0]
      ie_id = self.ExecuteSql(SqlQueries([ie_sql_query]))[0]
      me_id = self.ExecuteSql(SqlQueries([me_sql_query]))[0]

      return (ce_id,ie_id,me_id)

  def GetLessonIdsForInsert(self):
    py101_id_query = SqlQuery("SELECT Id FROM Lessons WHERE Code = ?",("PY101",))
    py102_id_query = SqlQuery("SELECT Id FROM Lessons WHERE Code = ?",("PY102",))
    mat101_id_query = SqlQuery("SELECT Id FROM Lessons WHERE Code = ?",("MAT101",))
    ye101_id_query = SqlQuery("SELECT Id FROM Lessons WHERE Code = ?",("YE101",))

    py101_id = self.ExecuteSql(SqlQueries([py101_id_query]))[0][0]
    py102_id = self.ExecuteSql(SqlQueries([py102_id_query]))[0][0]
    mat101_id = self.ExecuteSql(SqlQueries([mat101_id_query]))[0][0]
    ye101_id = self.ExecuteSql(SqlQueries([ye101_id_query]))[0][0]

    return (py101_id, py102_id, mat101_id, ye101_id)


  def GetUserIdsForInsert(self):
    fethitekyaygil_id_query = SqlQuery("SELECT Id FROM Users WHERE username = ?",("fethitekyaygil",))
    tahatekyaygil_id_query = SqlQuery("SELECT Id FROM Users WHERE username = ?",("tahatekyaygil",))
    enesagdag_id_query = SqlQuery("SELECT Id FROM Users WHERE username = ?",("enesagdag",))
    muratozcan_id_query = SqlQuery("SELECT Id FROM Users WHERE username = ?",("muratozcan",))

    fethitekyaygil_id = self.ExecuteSql(SqlQueries([fethitekyaygil_id_query]))[0][0]
    tahatekyaygil_id = self.ExecuteSql(SqlQueries([tahatekyaygil_id_query]))[0][0]
    enesagdag_id = self.ExecuteSql(SqlQueries([enesagdag_id_query]))[0][0]
    muratozcan_id = self.ExecuteSql(SqlQueries([muratozcan_id_query]))[0][0]

    return (fethitekyaygil_id,tahatekyaygil_id,enesagdag_id,muratozcan_id)


  def InsertUserRecords(self):
      
      ce_id, ie_id, me_id = self.GetDepartmentIdsForInsert()

      query_list=[]
      
      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Fethi','Tekyaygil','fethitekyaygil','123',?,1)
      ''',(ce_id)))

      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Taha','Tekyaygil','tahatekyaygil','123456',?,1)
      ''',(ce_id)))

      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Enes','Ağdağ','enesagdag','123432',?,1)
      ''',(ie_id)))
      
      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Murat','Özcan','muratozcan','123213',?,1)
      ''',(me_id)))
      
      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Hıdır','Sevinç','hidirsevinç','123333',?,0)
      ''',(ce_id)))
      
      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Yeşim','Çalık','yesimcalik','1233334',?,0)
      ''',(ie_id)))

      query_list.append(SqlQuery('''
      INSERT INTO Users(Name,Surname,Username,Password,DepartmentId,Policy)
      VALUES ('Sefer','Kurnaz','seferkurnaz','1233331212',?,0)
      ''',(me_id)))
      
      
      self.ExecuteSql(SqlQueries(query_list,operation="i")) #i = insert

  def InsertDepartmentRecords(self):
      query_list=[]

      query_list.append(SqlQuery('''
      INSERT INTO Departments(Name) VALUES('Computer Engineering');
      '''))

      query_list.append(SqlQuery('''
      INSERT INTO Departments(Name) VALUES('Industrial Engineering');
      '''))

      query_list.append(SqlQuery('''
      INSERT INTO Departments(Name) VALUES('Mechanical Engineering');
      '''))

      self.ExecuteSql(SqlQueries(query_list,operation="i"))


  def InsertLessonRecords(self):
      ce_id, ie_id, me_id = self.GetDepartmentIdsForInsert()

      query_list=[]

      query_list.append(SqlQuery('''
      INSERT INTO Lessons(Name,Code,Midterm1Effect,Midterm2Effect,FinalEffect,DepartmentId)
      VALUES ('Python Programlama 1','PY101','30','35','35',?)
      ''', (ce_id)))

      query_list.append(SqlQuery('''
      INSERT INTO Lessons(Name,Code,Midterm1Effect,Midterm2Effect,FinalEffect,DepartmentId)
      VALUES ('Python Programlama 2','PY102','40','25','35',?)
      ''',(ce_id)))


      query_list.append(SqlQuery('''
      INSERT INTO Lessons(Name,Code,Midterm1Effect,Midterm2Effect,FinalEffect,DepartmentId)
      VALUES ('Matematik 101','MAT101','20','25','55',?)
      ''',(me_id)))


      query_list.append(SqlQuery('''
      INSERT INTO Lessons(Name,Code,Midterm1Effect,Midterm2Effect,FinalEffect,DepartmentId)
      VALUES ('Yöneylem 101','YE101','30','35','35',?)
      ''',(ie_id)))

      self.ExecuteSql(SqlQueries(query_list,operation="i"))

  def InsertGradeRecords(self):
      py101_id, py102_id, mat101_id, ye101_id = self.GetLessonIdsForInsert()
      fethitekyaygil_id, tahatekyaygil_id, enesagdag_id, muratozcan_id = self.GetUserIdsForInsert()

      query_list=[]

      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(fethitekyaygil_id, py101_id)))
      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(fethitekyaygil_id, mat101_id)))
      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(tahatekyaygil_id, py102_id)))
      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(muratozcan_id, ye101_id)))
      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(muratozcan_id, mat101_id)))
      query_list.append(SqlQuery("INSERT INTO Grades (UserId,LessonId) VALUES(?,?)",(enesagdag_id, ye101_id)))

      self.ExecuteSql(SqlQueries(query_list,"i"))

class DbGetOps(DbOperations):
  def __init__(self,baglanti):
    super().__init__(baglanti)

  def GetUsers(self):
    return self.ExecuteSql(
        SqlQueries(
            [SqlQuery("SELECT * FROM Users")],operation="r"))
    
  def GetLessons(self):
    return self.ExecuteSql(
        SqlQueries(
            [SqlQuery("SELECT * FROM Lessons")],operation="r"))
    
  def GetDepartments(self):
    return self.ExecuteSql(
        SqlQueries(
            [SqlQuery("SELECT * FROM Departments")],operation="r"))
    
  def GetGrades(self):
    return self.ExecuteSql(
        SqlQueries(
            [SqlQuery("SELECT * FROM Grades")],operation="r"))

db_create_ops = DbCreateOps(baglanti)

db_insert_ops = DbInsertOps(baglanti)

db_create_ops.InitializeDatabase()

db_insert_ops.InitializeRecords()

db_get_ops = DbGetOps(baglanti)

db_get_ops.GetGrades()

db_get_ops.GetDepartments()

db_get_ops.GetLessons()

""" ## Backend ve Business"""

class User():
  def __init__(self,id,name,surname,username,password,departmentId,policy):
    self.id = id
    self.name = name
    self.surname = surname
    self.username = username
    self.password = password
    self.departmentId = departmentId
    self.policy = policy

class UserManager(DbOperations):
  def __init__(self,baglanti):
    super().__init__(baglanti)

  def CheckUsernamePasswordValidation(self,username,password):
    return self.ExecuteSql(
        SqlQueries(
            [SqlQuery("SELECT * FROM Users WHERE Username = ? AND Password = ?",parameters=(username,password))],operation="r"
        )
    )

  def GetUserLessons(self,userId):
    user_lessons = self.ExecuteSql(
        SqlQueries(
            [SqlQuery('''SELECT l.Name, l.Code FROM Grades as g 
            JOIN Lessons as l ON g.LessonId = l.Id
            WHERE g.UserId = ?
            ''',(userId,))]
        )
    )

    return [f"{lesson[0]} ({lesson[1]})" for lesson in user_lessons]


  def MapUser(self,user_list_value):
    return User(user_list_value[0],
                user_list_value[1],
                user_list_value[2],
                user_list_value[3],
                user_list_value[4],
                user_list_value[5],
                user_list_value[6])

  def MapUsers(self,user_list_values):
    user_list=[]

    for user_list_value in user_list_values:
      user_list.append(self.MapUser(user_list_value))

    return user_list

"""## UI"""

def UIKullaniciyiSelamla(adSoyad):
  print(f'Hoşgeldin {adSoyad}!')

def UIKullaniciIslemleri(userId):
  secim=input("Yapmak istediğiniz işlemi seçin! \n* Dersleri görmek için 1\n* Notları görmek için 2\n ")
  if secim == "1":
    print(UIOgrenciDersleriGoruntule(userId))
  elif secim == "2":
    UIOgrenciDersNotlariGoruntule()

def UIOgrenciDersleriGoruntule(userId):
  global user_manager

  print(user_manager.GetUserLessons(userId))

"""1. Tüm derslerin notlarını görüntüleyecek
2. Tek dersin notlarını görüntüleyecek

# App
"""

hak=3
ogrenciNo = None
sifre = None
girisYapanOgrenci = None
ogrenciDerslerVeNotlar = []
notuOlanDersler = []
user_manager = UserManager(baglanti)

while hak>0:
  if hak<=0:
    print("Çok fazla hatalı deneme yaptınız lütfen öğrenci işleriyle iletişime geçin!")
    exit()

  kullaniciAdi=input("Kullanıcı Adı: ")
  sifre=input("Şifre: ")

  girisYapanOgrenciSorguListesi = user_manager.CheckUsernamePasswordValidation(kullaniciAdi,sifre)

  if len(girisYapanOgrenciSorguListesi) > 0:
    girisYapanOgrenci = girisYapanOgrenciSorguListesi[0]
    logged_user = user_manager.MapUser(girisYapanOgrenci)
    break
  else:
    hak-=1
    continue
  



UIKullaniciyiSelamla(f"{logged_user.name} {logged_user.surname}")
UIKullaniciIslemleri(logged_user.id)

"""
  ogrenciDerslerVeNotlar = UIBaslangictaOgrenciDersVeNotlariniGetir(ogrenciNo) #tüm dersleri getirsin
  notuOlanDersler = UIBaslangictaOgrenciNotuOlanDersleriGetir()
  UIKullaniciyiSelamla(girisYapanOgrenci["AdiSoyadi"])
  UIKullaniciIslemleri()
"""