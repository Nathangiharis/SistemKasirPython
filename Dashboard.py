def br(dashboard):
    t = '' 
    for a in range(50):
        t += dashboard
    print(t)
 
def show_menu():
    print(" ")
    print("|--------------------------------------|")
    print("|       DASHBOARD MACN PEKANBARU       |")
    print("|--------------------------------------|")
    print("|   1. Tenant                          |")
    print("|   2. Pelanggan                       |")
    print("|   3. Produk                          |")
    print("|   4. Transaksi                       |")
    print("|   5. Pengantaran                     |")
    print("|--------------------------------------|")
    print(" ")
    i = int(input("Tentukan pilihan anda yang diinginkan (1/2/3/4/5): "))
    print("|--------------------------------------|")
 
    if (i == 1): import tenant
    elif (i == 2): import pelanggan
    elif (i == 3): import produk
    elif (i == 4): import Transaksi
    elif (i == 5): import pengantaran
 
    print("|--------------------------------------|")
if __name__ == "__main__":
    while(True):
        show_menu()