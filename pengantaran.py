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
    print("|        Daftar Nama Pengantar         |")
    print("|--------------------------------------|")
    print("|    1. JNE                            |")
    print("|    2. JNT                            |")
    print("|    3. POS INDONESIA                  |")
    print("|    4. GRAB                           |")
    print("|    5. GOJEK                          |")
    print("|    6. LION PAKET                     |")
    print("|--------------------------------------|")

    Jenis_Kurir = input("Masukan jenis pengantaran (1/2/3/4/5/6): ")
    if Jenis_Kurir == "1":
        Jenis_Kurir = "JNE"
    elif Jenis_Kurir == "2":
        Jenis_Kurir = "JNT"
    elif Jenis_Kurir == "3":
        Jenis_Kurir = "POS INDONESIA"
    elif Jenis_Kurir == "4":
        Jenis_Kurir = "GRAB"
    elif Jenis_Kurir == "5":
        Jenis_Kurir = "GOJEK"
    elif Jenis_Kurir == "6":
        Jenis_Kurir = "LION PAKET"

    print("")
    print("|--------------------------------------|")
    print("|         Daftar Nama Pengantar        |")
    print("|--------------------------------------|")
    print("|    1. Asep                           |")
    print("|    2. Ujang                          |")
    print("|    3. Usep                           |")
    print("|    4. Bani                           |")
    print("|--------------------------------------|")

    Nama_Pengantar = input("Masukan Nama Pengantar (1/2/3/4): ")
    if Nama_Pengantar == "1":
        Nama_Pengantar = "Asep"
    elif Nama_Pengantar == "2":
        Nama_Pengantar = "Ujang"
    elif Nama_Pengantar == "3":
        Nama_Pengantar = "Usep"
    elif Nama_Pengantar == "4":
        Nama_Pengantar = "Bani"
        
    val = (Jenis_Kurir, Nama_Pengantar)
    cursor = db.cursor()
    sql = "INSERT INTO pengantaran (Jenis_Kurir, Nama_Pengantar) VALUES (%s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang anda pilih berhasil disimpan".format(cursor.rowcount))
 
def show_data(db):
  global Id_Pengantaran
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM pengantaran"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Data yang anda pilih tidak ditemukan")
  else:
    for row in results:
        Id_Pengantaran = row["Id_Pengantaran"]
        Jenis_Kurir = row["Jenis_Kurir"]
        Nama_Pengantar = row["Nama_Pengantar"]
        print(Id_Pengantaran, Jenis_Kurir, Nama_Pengantar)
        print("---------------------------------------")
        
 
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    print("|--------------------------------------|")
    Id_Pengantaran = input("pilih Id_Pengantaran: ")
    print("")
    print("|--------------------------------------|")
    print("|        Daftar Nama Pengantar         |")
    print("|--------------------------------------|")
    print("|    1. JNE                            |")
    print("|    2. JNT                            |")
    print("|    3. POS INDONESIA                  |")
    print("|    4. GRAB                           |")
    print("|    5. GOJEK                          |")
    print("|    6. LION PAKET                     |")
    print("|--------------------------------------|")

    Jenis_Kurir = input("Masukan jenis pengantaran (1/2/3/4/5/6): ")
    if Jenis_Kurir == "1":
        Jenis_Kurir = "JNE"
    elif Jenis_Kurir == "2":
        Jenis_Kurir = "JNT"
    elif Jenis_Kurir == "3":
        Jenis_Kurir = "POS INDONESIA"
    elif Jenis_Kurir == "4":
        Jenis_Kurir = "GRAB"
    elif Jenis_Kurir == "5":
        Jenis_Kurir = "GOJEK"
    elif Jenis_Kurir == "6":
        Jenis_Kurir = "LION PAKET"

    print("")
    print("|--------------------------------------|")
    print("|         Daftar Nama Pengantar        |")
    print("|--------------------------------------|")
    print("|    1. Asep                           |")
    print("|    2. Ujang                          |")
    print("|    3. Usep                           |")
    print("|    4. Bani                           |")
    print("|--------------------------------------|")

    Nama_Pengantar = input("Masukan Nama Pengantar (1/2/3/4): ")
    if Nama_Pengantar == "1":
        Nama_Pengantar = "Asep"
    elif Nama_Pengantar == "2":
        Nama_Pengantar = "Ujang"
    elif Nama_Pengantar == "3":
        Nama_Pengantar = "Usep"
    elif Nama_Pengantar == "4":
        Nama_Pengantar = "Bani"

    sql = "UPDATE pengantaran SET Jenis_Kurir = %s, Nama_Pengantar = %s WHERE Id_Pengantaran = %s"
    val = (Jenis_Kurir, Nama_Pengantar, Id_Pengantaran)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang dipilih berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  print("|--------------------------------------|")
  id_pengantaran = input("Pilih Id_Pengantaran: ")
  sql = "DELETE FROM pengantaran WHERE Id_Pengantaran= %s"
  val = (Id_Pengantaran,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data yang dipilih berhasil dihapus".format(cursor.rowcount))

print("|--------------------------------------|")
print("|           Data Pengiriman            |")
print("|--------------------------------------|") 
show_data(db)
print(" ")
print("|--------------------------------------|") 
print("|          Daftar Pengiriman           |")
print("|--------------------------------------|") 
print("|    A. Tambah Pengiriman              |")
print("|    B. Update Data Pengiriman         |")
print("|    C. Hapus Data Pengiriman          |")
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