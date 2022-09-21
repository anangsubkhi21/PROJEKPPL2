#fungsi garisnya guys
def garis1():
    print ("=======================")

def garis2():
    print ("---------------------")

# Perpus Kosong untuk menyimpan buku
buku = []

#fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        print ("Buku kosong om!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print  ("[{}]] {}".format (indeks))
            garis1()

#fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("inputan ID buku : "))
    if indeks > len(buku):
        print("ID SALAH")
        garis2()
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("Buku berhasil dirubah!")
        garis1()

#fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("Judul buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku Berhasil ditambah!")
    garis1()

    #fungsi delete buku
    def delete_buku():
        show_buku()
        indeks = int(input("inputkan ID Buku : "))
        if indeks > len(buku):
            print ("ID SALAH")
        else:
            buku.remove(buku[indeks])
            garis1()
            print ("Buku berhasil dihapus!")
            garis2()

#Menu untuk tampilkan perpus
def show_menu():
    print("\n")
    print("-Selamat datang di perpus-")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih menu : >"))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("upss salah")

#tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()