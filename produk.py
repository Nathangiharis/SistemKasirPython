import mysql.connector
import os
 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="UAS_PROKOMP2_CALMN"
)
 
def insert_data(db):
    print("")
    print("|--------------------------------------|")
    print("|            Daftar Produk             |")
    print("|--------------------------------------|")
    print("|    1. Batagor                        |")
    print("|    2. Siomay                         |")
    print("|    3. Es Jeruk                       |")
    print("|    4. Es Kopi Susu                   |")
    print("|    5. Sambel                         |")
    print("|--------------------------------------|")

    Nama_Produk = input("Masukan Pilihan Anda: ")
    if Nama_Produk == "1":
        Nama_Produk = "Batagor"
    elif Nama_Produk == "2":
        Nama_Produk = "Siomay"
    elif Nama_Produk == "3":
        Nama_Produk = "Es Jeruk"
    elif Nama_Produk == "4":
        Nama_Produk = "Es Kopi Susu"
    elif Nama_Produk == "5":
        Nama_Produk = "Sambel"
    
    val = (Nama_Produk,)
    cursor = db.cursor()
    sql = "INSERT INTO produk (Nama_Produk) VALUES (%s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang anda pilih berhasil disimpan".format(cursor.rowcount))
 
def show_data(db):
  global Id_Produk
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM produk"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Data yang anda pilih tidak ditemukan")
  else:
    for row in results:
        Id_Produk = row["Id_Produk"]
        Nama_Produk = row["Nama_Produk"]
        print(Id_Produk,"(",Nama_Produk,")")
        print("---------------------------------------")

def update_data(db):
    cursor = db.cursor()
    show_data(db)
    print("|--------------------------------------|")
    Nama_Produk = input("Pilih produk yang ingin diganti: ")
    print("")
    print("|--------------------------------------|")
    print("|            Daftar Produk             |")
    print("|--------------------------------------|")
    print("|    1. Batagor                        |")
    print("|    2. Siomay                         |")
    print("|    3. Es Jeruk                       |")
    print("|    4. Es Kopi Susu                   |")
    print("|    5. Sambel                         |")
    print("|--------------------------------------|")

    Nama_Produk = input("Masukan Pilihan Anda: ")
    if Nama_Produk == "1":
        Nama_Produk = "Batagor"
    elif Nama_Produk == "2":
        Nama_Produk = "Siomay"
    elif Nama_Produk == "3":
        Nama_Produk = "Es Jeruk"
    elif Nama_Produk == "4":
        Nama_Produk = "Es Kopi Susu"
    elif Nama_Produk == "5":
        Nama_Produk = "Sambel"

    sql = "UPDATE produk SET Nama_Produk = %s WHERE Id_Produk = %s"
    val = (Nama_Produk, Id_Produk)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang dipilih berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  print("|--------------------------------------|")
  Id_Tenant = input("Pilih Id_Produk: ")
  sql = "DELETE FROM produk WHERE Id_Produk= %s"
  val = (Id_Produk,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data yang dipilih berhasil dihapus".format(cursor.rowcount))

print(" ")
print("|--------------------------------------|")
print("|            Data Produk               |")
print("|--------------------------------------|") 
show_data(db)
print(" ")
print("|--------------------------------------|") 
print("|            Daftar Produk             |")
print("|--------------------------------------|") 
print("|    A. Tambah Produk                  |")
print("|    B. Update Data Produk             |")
print("|    C. Hapus Data Produk              |")
print("|    0. Keluar                         |")
print("| -------------------------------------|")
menu = input("Pilih menu (A/B/C): ")
 
#clear screen
os.system("clear")
 
if menu == "A":
    insert_data(db)
elif menu == "B":
    update_data(db)
elif menu == "C":
    delete_data(db)
elif menu == "0":
    exit()
else:
    print("Menu yang anda pilih salah, gunakan (A/B/C/0)")