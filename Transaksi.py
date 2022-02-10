import mysql.connector
import os
 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="UAS_PROKOMP2_CALMN"
)
 
def insert_data(db):
    print(" ")
    print("|--------------------------------------|")
    print("|              Daftar Nama             |")
    print("|--------------------------------------|") 
    print("|    1. Nathan                         |")
    print("|    2. Carmel                         |")
    print("|    3. Angel                          |")
    print("|    4. Matthew                        |")
    print("|    5. Laras                          |")
    print("|--------------------------------------|") 

    Nama_Lengkap = input("Masukkan Nama Pelanggan: ")
    if Nama_Lengkap == "1":
        Nama_Lengkap = "Nathan"
    elif Nama_Lengkap == "2":
        Nama_Lengkap = "Carmel"
    elif Nama_Lengkap == "3":
        Nama_Lengkap = "Angel"
    elif Nama_Lengkap == "4":
        Nama_Lengkap = "Matthew"
    elif Nama_Lengkap == "5":
        Nama_Lengkap = "Laras"

    print("")
    print("|--------------------------------------|")
    print("|             Daftar Produk            |")
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

    print("")
    print("|--------------------------------------|")
    print("|            Jumlah Pesanan            |")
    print("|--------------------------------------|")
    print("|    1. Satuan                         |")
    print("|    2. Selusin                        |")
    print("|    3. Sekuintal                      |")
    print("|--------------------------------------|")

    Jumlah_Pesanan = input("Masukkan Pilihan Anda: ")
    if Jumlah_Pesanan == "1":
        Jumlah_Pesanan = "Satuan"
    elif Jumlah_Pesanan == "2":
        Jumlah_Pesanan = "Selusin"
    elif Jumlah_Pesanan == "3":
        Jumlah_Pesanan = "Sekuintal"

    val = (Nama_Lengkap, Nama_Produk, Jumlah_Pesanan)
    cursor = db.cursor()
    sql = "INSERT INTO Transaksi (Nama_Lengkap, Nama_Produk, Jumlah_Pesanan) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang anda pilih berhasil disimpan".format(cursor.rowcount))
 
def show_data(db):
  global Id_Transaksi
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM transaksi"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Data yang anda pilih tidak ditemukan")
  else:
    for row in results:
        Id_Transaksi = row["Id_Transaksi"]
        Nama_Lengkap = row["Nama_Lengkap"]
        Nama_Produk = row["Nama_Produk"]
        Jumlah_Pesanan = row["Jumlah_Pesanan"]
        print(Id_Transaksi, Nama_Lengkap, Nama_Produk, Jumlah_Pesanan)
        print("---------------------------------------")
 
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    print("|--------------------------------------|")
    Id_Transaksi = input("Pilih Id_Transaksi: ")
    print(" ")
    print("|--------------------------------------|")
    print("|         Daftar Nama Pelanggan        |")
    print("|--------------------------------------|") 
    print("|    1. Nathan                         |")
    print("|    2. Carmel                         |")
    print("|    3. Angel                          |")
    print("|    4. Matthew                        |")
    print("|    5. Laras                          |")
    print("|--------------------------------------|") 

    Nama_Lengkap = input("Masukkan Nama Pelanggan: ")
    if Nama_Lengkap == "1":
        Nama_Lengkap = "Nathan"
    elif Nama_Lengkap == "2":
        Nama_Lengkap = "Carmel"
    elif Nama_Lengkap == "3":
        Nama_Lengkap = "Angel"
    elif Nama_Lengkap == "4":
        Nama_Lengkap = "Matthew"
    elif Nama_Lengkap == "5":
        Nama_Lengkap = "Laras"
    
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

    print("")
    print("|--------------------------------------|")
    print("|            Jumlah Pesanan            |")
    print("|--------------------------------------|")
    print("|    1. Satuan                         |")
    print("|    2. Selusin                        |")
    print("|    3. Sekuintal                      |")
    print("|--------------------------------------|")

    Jumlah_Pesanan = input("Masukkan Jumlah Pesanan: ")
    if Jumlah_Pesanan == "1":
        Jumlah_Pesanan = "Satuan"
    elif Jumlah_Pesanan == "2":
        Jumlah_Pesanan = "Selusin"
    elif Jumlah_Pesanan == "3":
        Jumlah_Pesanan = "Sekuintal"

    sql = "UPDATE transaksi SET Nama_Lengkap = %s, Nama_Produk = %s, Jumlah_Pesanan = %s WHERE Id_Transaksi = %s"
    val = (Nama_Lengkap, Nama_Produk, Jumlah_Pesanan, Id_Transaksi)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang dipilih berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  print("|--------------------------------------|")
  Id_Transaksi = input("Pilih Id_Transaksi: ")
  sql = "DELETE FROM transaksi WHERE Id_Transaksi=%s"
  val = (Id_Transaksi,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data yang dipilih berhasil dihapus".format(cursor.rowcount))

print(" ")
print("|--------------------------------------|")
print("|           Data Transaksi             |")
print("|--------------------------------------|") 
show_data(db)
print(" ")
print("|--------------------------------------|") 
print("|           Daftar Transaksi           |")
print("|--------------------------------------|") 
print("|    A. Tambah Transaksi               |")
print("|    B. Update Data Transaki           |")
print("|    C. Hapus Data Transaksi           |")
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