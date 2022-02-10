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
    print("|            Daftar Tenant             |")
    print("|--------------------------------------|")
    print("|    1. Batagor Bandung                |")
    print("|    2. Jahe Palembang                 |")
    print("|    3. Asinan Kopo                    |")
    print("|    4. Jahe Garut                     |")
    print("|    5. Manisan Bogor                  |")
    print("|--------------------------------------|")

    Nama_Tenant = input("Masukan Pilihan Anda: ")
    if Nama_Tenant == "1":
        Nama_Tenant = "Batagor Bandung"
    elif Nama_Tenant == "2":
        Nama_Tenant = "Jahe Palembang"
    elif Nama_Tenant == "3":
        Nama_Tenant = "Asinan Kopo"
    elif Nama_Tenant == "4":
        Nama_Tenant = "Jahe Garut"
    elif Nama_Tenant == "5":
        Nama_Tenant = "Manisan Bogor"
    
    print(" ")
    print("|--------------------------------------|")
    print("|          Daftar Pembelian            |")
    print("|--------------------------------------|")
    print("|    1. Online                         |")
    print("|    2. Offline                        |")
    print("|--------------------------------------|")

    Jenis_Penjualan = input("Jenis Pembelian: ")
    if Jenis_Penjualan == "1":
        Jenis_Penjualan = "Online"
    elif Jenis_Penjualan == "2":
        Jenis_Penjualan = "Offline"
    
    print(" ")
    print("|--------------------------------------|")
    print("|           Daftar Lokasi              |")
    print("|--------------------------------------|")
    print("|    1. Jabodetabek                    |")
    print("|    2. Jawa Barat                     |")
    print("|--------------------------------------|")
   
    Lokasi_Penjualan = input("Lokasi Penjualan: ")
    if Jenis_Penjualan == "1":
        Jenis_Penjualan = "Jabodetabek"
    elif Jenis_Penjualan == "2":
        Jenis_Penjualan = "Jawa Barat"

    val = (Nama_Tenant, Jenis_Penjualan, Lokasi_Penjualan)
    cursor = db.cursor()
    sql = "INSERT INTO tenant (Nama_Tenant, Jenis_Penjualan, Lokasi_Penjualan) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("=======================================")
    print("{} Data yang anda pilih berhasil disimpan".format(cursor.rowcount))
 
 
def show_data(db):
  global Id_Tenant
  cursor = db.cursor(dictionary=True)
  sql = "SELECT * FROM tenant"
  cursor.execute(sql)
  results = cursor.fetchall()
       
  if cursor.rowcount < 0:
    print("Data yang anda pilih tidak ditemukan:")

  else:
    for row in results:
        Id_Tenant = row["Id_Tenant"]
        Nama_Tenant = row["Nama_Tenant"]
        Jenis_Penjualan = row["Jenis_Penjualan"]
        Lokasi_Penjualan = row["Lokasi_Penjualan"]
        print(Id_Tenant, Nama_Tenant, Jenis_Penjualan,"(",Lokasi_Penjualan,")")
        print("---------------------------------------")
 
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    print("|--------------------------------------|")
    Id_Tenant = input("Pilih Id_Tenant: ")
    print(" ")
    print("|--------------------------------------|")
    print("|            Daftar Tenant             |")
    print("|--------------------------------------|")
    print("|    1. Batagor Bandung                |")
    print("|    2. Jahe Palembang                 |")
    print("|    3. Asinan Kopo                    |")
    print("|    4. Jahe Garut                     |")
    print("|    5. Manisan Bogor                  |")
    print("|--------------------------------------|")

    Nama_Tenant = input("Masukkan daftar tenant yang diinginkan: ")
    if Nama_Tenant == "1":
        Nama_Tenant = "Batagor Bandung"
    elif Nama_Tenant == "2":
        Nama_Tenant = "Jahe Palembang"
    elif Nama_Tenant == "3":
        Nama_Tenant = "Asinan Kopo"
    elif Nama_Tenant == "4":
        Nama_Tenant = "Jahe Garut"
    elif Nama_Tenant == "5":
        Nama_Tenant = "Manisan Bogor"
    
    print(" ")
    print("|--------------------------------------|")
    print("|          Daftar Pembelian            |")
    print("|--------------------------------------|")
    print("|    1. Online                         |")
    print("|    2. Offline                        |")
    print("|--------------------------------------|")

    Jenis_Penjualan = input("Masukkan Jenis Pembelian: ")
    if Jenis_Penjualan == "1":
        Jenis_Penjualan = "Online"
    elif Jenis_Penjualan == "2":
        Jenis_Penjualan = "Offline"
    
    print(" ")
    print("|--------------------------------------|")
    print("|           Daftar Lokasi              |")
    print("|--------------------------------------|")
    print("|    1. Jabodetabek                    |")
    print("|    2. Jawa Barat                     |")
    print("|--------------------------------------|")
   
    Lokasi_Penjualan = input("Masukkan Lokasi Penjualan: ")
    if Jenis_Penjualan == "1":
        Jenis_Penjualan = "Jabodetabek"
    elif Jenis_Penjualan == "2":
        Jenis_Penjualan = "Jawa Barat"

    sql = "UPDATE tenant SET Nama_Tenant = %s, Jenis_Penjualan = %s, Lokasi_Penjualan = %s WHERE Id_Tenant = %s"
    val = (Nama_Tenant, Jenis_Penjualan, Lokasi_Penjualan, Id_Tenant)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data yang dipilih berhasil diubah".format(cursor.rowcount))
 
def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  print("|--------------------------------------|")
  Id_Tenant = input("Pilih id Nama_Tenant: ")
  sql = "DELETE FROM tenant WHERE Id_Tenant= %s"
  val = (Id_Tenant,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data yang dipilih berhasil dihapus".format(cursor.rowcount))

print(" ")
print("|--------------------------------------|")
print("|            Data Tenant               |")
print("|--------------------------------------|") 
show_data(db)
print(" ")
print("|--------------------------------------|") 
print("|            Daftar Tenant             |")
print("|--------------------------------------|") 
print("|    A. Tambah Tenant                  |")
print("|    B. Update Data Tenant             |")
print("|    C. Hapus Data Tenant              |")
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