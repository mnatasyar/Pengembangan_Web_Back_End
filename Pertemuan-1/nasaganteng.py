#  THE COMPOSITE PATTERN

from abc import ABC, abstractmethod

class KegiatanKampus (ABC):
    @abstractmethod
    def return_price(self):
        pass

class Biaya(KegiatanKampus):
    def __init__(self, contents):
        self.contents = contents
    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price

class BiayaPendaftaran(KegiatanKampus):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.price

class BiayaUkt(KegiatanKampus):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.price

class BiayaTrainning(KegiatanKampus):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.price

class BiayaPenginapan(KegiatanKampus):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.price

class BiayaKonsumsi(KegiatanKampus):
    def __init__(self, price):
        self.price = price
    def return_price(self):
        return self.price

if __name__ == "__main__":
    biaya_daftar = []
    print ("Biaya Pendaftaran= Rp. 200.000")
    biaya_daftar.append(BiayaPendaftaran(200000))
    biaya_daftar_1 = Biaya(biaya_daftar)

    ukt_awal = []
    ukt_awal.append(biaya_daftar_1)
    print ("Biaya Ukt\t= Rp. 1.500.000")
    ukt_awal.append(BiayaUkt(1500000))
    print("Uang MPT :")
    print ("\t- Biaya Trainning\t= Rp. 100.000")
    ukt_awal.append(BiayaTrainning(100000))
    print ("\t- Biaya Penginapan\t= Rp. 200.000")
    ukt_awal.append(BiayaPenginapan(200000))
    print ("\t- Biaya Konsumsi\t= Rp. 150.000")
    ukt_awal.append(BiayaKonsumsi(150000))
    ukt_awal2 = Biaya(ukt_awal)
    
print("BIAYA TOTAL SEMUANYA ADALAH : Rp." + str(ukt_awal2.return_price()))
