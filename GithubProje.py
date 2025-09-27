import sqlite3
from idlelib.colorizer import prog_group_name_to_tag

conn = sqlite3.connect("C:/Users/zeki/OneDrive/Belgeler/sqlite/Ogrenci.db")
Cursor = conn.cursor()

Cursor.execute("""CREATE TABLE IF NOT EXISTS Ogrenciler(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ad TEXT,
yas INTEGER
)  """)

a=input("Ogrencinin adi = ")
y=int(input("Yasinizi giriniz = "))

try:
    Cursor.execute("INSERT INTO Ogrenciler(ad,yas) VALUES(?,?)",(a,y))
    conn.commit()
    if Cursor.rowcount > 0:
        print("Ogrenci Basariyla Eklendi")
    else:
        print("Ogrenci Eklenemedi")
except Exception as e:
    print("Bir hata olustu :",e)

Cursor.execute("SELECT * FROM Ogrenciler")
for row in Cursor.fetchall():
    print(row)

conn.close()


