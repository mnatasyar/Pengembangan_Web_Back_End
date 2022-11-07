import os

class Barang:
    list_barang = []
    list_histori = []

    def __init__(self, kode="", nama="", stok=0, harga = 0):
        self.kode = kode
        self.nama = nama
        self.stok = stok
        self.harga = harga
        # self.list_barang = []

    def input_barang(self):
        kode = input("Masukkan Kode barang = ")
        nama = input("Masukkan Nama barang = ")
        stok = input("Masukkan Stok barang = ")
        harga = input("Masukkan Harga barang = ")
        barang = Barang(kode, nama, stok,harga)
        self.list_barang.append(barang)
        input("Tekan sembarang tombol untuk melanjutkan ...")

    def penjualan_barang(self):
        kode = input("Masukkan Kode barang = ")
        barang = self.get_barang_by_code(kode)
        if (barang):
            stok = int(input("Masukkan Stok barang = "))
            if(stok >0 and stok <= int(barang.stok)):
                barang.stok =  int(barang.stok) - stok
                print("boleh jual")
            else:
                print("Barang tidak dapat dijual")

        else:
            print("Barang tidak ditemukan")
        input("Tekan sembarang tombol")
    
    def show_barang(self):
        for i in range (len(self.list_barang)):
            print(self.list_barang[i].__dict__)
        input("Tekan sembarang tombol untuk melanjutkan ...")

    def get_barang_by_code(self,kode):
        for i in range (len(self.list_barang)):
            if(self.list_barang[i].kode == kode):
                return self.list_barang[i]

    def get_index_barang_by_code(self,kode):
        idx = -1
        for i in range (len(self.list_barang)):
            if(self.list_barang[i].kode == kode):
                idx = i
                break
        return idx
    
    def edit_barang_by_kelas(self, kode, barang_baru):
        barang = self.get_barang_by_code(kode)
        if barang:
            barang.nama = barang_baru.nama
            barang.stok = barang_baru.stok
            barang.harga = barang_baru.harga
        return barang

    def edit_barang(self, kode, nama, stok, harga):
        barang = self.get_barang_by_code(kode)
        if barang:
            barang.nama = nama
            barang.stok = stok
            barang.harga = harga
        return barang

    def hapus_barang(self, kode):
        idx_barang = self.get_index_barang_by_code(kode)
        if idx_barang!= -1:
            self.list_barang.pop(idx_barang)
            print("Barang berhasil dihapus")
        else:
            print("Barang gagal dihapus")

    def pengeditan_barang(self):
        kode = input("Masukkan Kode barang = ")
        if (barang.get_barang_by_code(kode)):
            nama = input("Masukkan Nama barang = ")
            stok = input("Masukkan Stok barang = ")
            harga = input("Masukkan Harga barang = ")

            # Cara 1 : Edit dengan parameter berupa property
            # barang.edit_barang(kode, nama, stok, harga)

            # Cara 2 : Edit dengan parameter berupa class 
            barang_baru = Barang(kode,nama,stok,harga)
            barang.edit_barang_by_kelas(kode, barang_baru)

           
        else:
            print("Barang tidak ditemukan")
        input("Tekan sembarang tombol untuk melanjutkan ...")

    def penghapusan_barang(self):
        kode = input("Masukkan Kode barang Yang mau dihapus= ")
        if (barang.get_barang_by_code(kode)):
            barang.hapus_barang(kode)
        else:
            print("Barang gagal dihapus")
        input("Tekan sembarang tombol untuk melanjutkan ...")
while True:
    os.system('cls')
    print("1. Input Data Barang")
    print("2. Tampilkan Data Barang")
    print("3. Penjualan Barang")
    print("4. Edit Barang")
    print("5. Hapus Barang")
    print("6. Exit")
    pilihan = int(input("Masukkan Pilihan Anda : "))
    barang = Barang()
    if pilihan == 1:
        os.system('cls')
        barang.input_barang()
    if pilihan == 2:
        os.system('cls')
        barang.show_barang()
    elif pilihan == 3:
        os.system('cls')
        barang.penjualan_barang()
    elif pilihan == 4:
        os.system('cls')
        barang.pengeditan_barang()
    elif pilihan == 5:
        os.system('cls')
        barang.penghapusan_barang()
    elif pilihan == 6:
        quit()
    else:
        print(f"Pilihan yang tersedia 1-3, silakan coba kembali")
