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
    print("|           Daftar Pelanggan           |")
    print("|--------------------------------------|")
    print("|    1. Adit Solin Soccer              |")
    print("|    2. Asep Julian                    |")
    print("|    3. Mamang Garut                   |")
    print("|    4. Nathan Ramadhan                |")
    print("|    5. Ujang Salto                    |")
    print("|--------------------------------------|")

    Nama_Pelanggan = input("Masukkan Nama Pelanggan: ")
    if Nama_Pelanggan == "1":
        Nama_Pelanggan = "Adit Solin Soccer"
    elif Nama_Pelanggan == "2":
        Nama_Pelanggan = "Asep Julian"
    elif Nama_Pelanggan == "3":
        Nama_Pelanggan = "Mamang Garut"
    elif Nama_Pelanggan == "4":
        Nama_Pelanggan = "Nathan Ramadhan"
    elif Nama_Pelanggan == "5":
        Nama_Pelanggan = "Ujang Salto"
    
    print("")
    print("|--------------------------------------|")
    print("|            Daftar Lokasi             |")
    print("|--------------------------------------|")
    print("|    1. Jabodetabek                    |")
    print("|    2. Jawa Barat                     |")
    print("|--------------------------------------|")

    Lokasi_Pelanggan = input("Masukkan Lokasi Pelanggan (1/2): ")
    if Lokasi_Pelanggan == "1":
        Lokasi_Pelanggan = "Jabodetabek"
    elif Lokasi_Pelanggan == "2":
        Lokasi_Pelanggan = "Jawab Barat"

    val = (Nama_Pelanggan, Lokasi_Pelanggan)
    cursor = db.cursor()
    sql = "INSERT INTO pelanggan (Nama_Pelanggan, Lokasi_Pelanggan) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang anda pilih berhasil disimpan".format(cursor.rowcount))
 
 
def show_data(db):
  global Id_Pelanggan
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM pelanggan"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Data yang anda pilih tidak ditemukan")
  else:
    for row in results:
        Id_Pelanggan = row["Id_Pelanggan"]
        Nama_Pelanggan = row["Nama_Pelanggan"]
        Lokasi_Pelanggan = row["Lokasi_Pelanggan"]
        print(Id_Pelanggan, Nama_Pelanggan, Lokasi_Pelanggan)
        print("---------------------------------------")
 
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    print("|--------------------------------------|")
    Id_Pelanggan = input("Pilih Id_Pelanggan: ")
    print("")
    print("|--------------------------------------|")
    print("|           Daftar Pelanggan           |")
    print("|--------------------------------------|")
    print("|    1. Adit Solin Soccer              |")
    print("|    2. Asep Julian                    |")
    print("|    3. Mamang Garut                   |")
    print("|    4. Nathan Ramadhan                |")
    print("|    5. Ujang Salto                    |")
    print("|--------------------------------------|")

    Nama_Pelanggan = input("Masukkan Nama Pelanggan: ")
    if Nama_Pelanggan == "1":
        Nama_Pelanggan = "Adit Solin Soccer"
    elif Nama_Pelanggan == "2":
        Nama_Pelanggan = "Asep Julian"
    elif Nama_Pelanggan == "3":
        Nama_Pelanggan = "Mamang Garut"
    elif Nama_Pelanggan == "4":
        Nama_Pelanggan = "Nathan Ramadhan"
    elif Nama_Pelanggan == "5":
        Nama_Pelanggan = "Ujang Salto"
    
    print("")
    print("|--------------------------------------|")
    print("|            Daftar Lokasi             |")
    print("|--------------------------------------|")
    print("|    1. Jabodetabek                    |")
    print("|    2. Jawa Barat                     |")
    print("|--------------------------------------|")

    Lokasi_Pelanggan = input("Masukkan Lokasi Pelanggan (1/2): ")
    if Lokasi_Pelanggan == "1":
        Lokasi_Pelanggan = "Jabodetabek"
    elif Lokasi_Pelanggan == "2":
        Lokasi_Pelanggan = "Jawa Barat"

    sql = "UPDATE pelanggan SET Nama_Pelanggan = %s, Lokasi_Pelanggan = %s WHERE Id_Pelanggan = %s"
    val = (Nama_Pelanggan, Lokasi_Pelanggan, Id_Pelanggan)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang dipilih berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  show_data(db)

  Id_Pelanggan = input("Pilih Id_Pelanggan: ")
  sql = "DELETE FROM pelanggan WHERE Id_Pelanggan=%s"
  val = (Id_Pelanggan,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data yang dipilih berhasil dihapus".format(cursor.rowcount))
 
print("|--------------------------------------|")
print("|           Data Pelanggan             |")
print("|--------------------------------------|") 
show_data(db)
print(" ")
print("|--------------------------------------|") 
print("|           Daftar Pelanggan           |")
print("|--------------------------------------|") 
print("|    A. Tambah Pelanggan               |")
print("|    B. Update Data Pelanggan          |")
print("|    C. Hapus Data Pelanggan           |")
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