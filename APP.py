import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="UAS_PROKOMP2_CALMN"
)

def insert_data (db):
    Nama_Lengkap = input("Masukkan Nama Lengkap: ")
    Nama_Produk = input("Masukkan produk: ")
    Jumlah_Pesanan = input ("Masukkan jumlah pesanan: ")
    val = (Nama_Lengkap, Nama_Produk, Jumlah_Pesanan)
    cursor = db.cursor()
    sql = "INSERT INTO transaksi (Id_Transaksi, Nama_Lengkap, Nama_Produk, Jumlah_Pesanan) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print ("{} Pesanan berhasil disimpan".format(cursor.rowcount))

def show_data(db):
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM transaksi"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for row in results:
        Id_Transaksi = row["Id_transaksi"]
        Nama_Lengkap = row["nama_pelanggan"]
        Nama_Produk = row["nama_produk"]
        Jumlah_pesanan = row["total_pesanan"]
        print(Id_Transaksi,"-", Nama_Lengkap,"-", Nama_Produk,"-",Jumlah_pesanan)
 
def update_data(db):
  cursor = db.cursor()

  show_data(db)
  Id_Transaksi = input("pilih id transaksi: ")
  Nama_Lengkap = input("Nama baru: ")
  Nama_Produk = input("Produk baru: ")
  Jumlah_pesanan = input("Jumlah Pesanan baru: ")
 
  sql = "UPDATE transaksi_pesanan SET nama_pelanggan=%s, nama_produk=%s,total_pesanan=%s WHERE id_transaksi=%s"
  val = (Nama_Lengkap, Nama_Produk,Jumlah_pesanan, Id_Transaksi)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  
  show_data(db)
  Id_Transaksi = input("pilih Id_Transaksi> ")
  sql = "DELETE FROM transaksi_pesanan WHERE Id_Transaksi=%s"
  val = (Id_Transaksi,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))
 
print("=== Daftar Transaksi Pesanan ===\n")
show_data(db)
print(" ")
print("A. Tambah Pesanan")
print("B. Edit Pesanan")
print("C. Hapus Pesanan")
print("0. Keluar")
print("------------------")
menu = input("Pilih menu(A/B/C): ")
 
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
    print("Menu salah!")
