from abc import ABC, abstractmethod

class absHasil(ABC):
    @abstractmethod
    def hasil():
        pass
    
class AbsHasil(ABC):
    @abstractmethod
    def hasil():
        pass

class Mahasiswa(absHasil):
    banyakMahasiswa = 0
    def __init__(self, nim, nama, prodi, jenisKelamin, noHp):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp
        self.banyakMahasiswa += 1

    def hasil(self):
        print("-------------------")
        print(f"Nim = {self.nim}")
        print(f"Nama = {self.nama}")
        print(f"Prodi = {self.prodi}")
        print(f"jenisKelamin = {self.jenisKelamin}")
        print(f"No. HP = {self.noHp}")
        print("-------------------\n")

class Dosen(AbsHasil):
    banyakDosen = 0
    def __init__(self, nip, nama, jabatan, jenisKelamin, noHp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp
        self.banyakDosen += 1

    def hasil(self):
        ("-------------------")
        print(f"Nip = {self.nip}")
        print(f"Nama = {self.nama}")
        print(f"Jabatan = {self.jabatan}")
        print(f"jenisKelamin = {self.jenisKelamin}")
        print(f"No. HP = {self.noHp}")
        ("-------------------\n")
        
if __name__ == "__main__":
    cetakMhs = Mahasiswa("211112080", "M. Natasya Ramadana", "TI", "Pria", "082162205010")
    for proses in absHasil.__subclasses__():
        proses.hasil(cetakMhs)
    
    cetakMhs = Mahasiswa("211111999", "Kaori Miyazono", "Manajemen", "Wanita", "Udh Meninggal")
    for proses in absHasil.__subclasses__():
        proses.hasil(cetakMhs)
        
    cetakDsn = Dosen("1234567", "Saya Sendiri", "Dosen Tetap", "Pria", "0812345678")
    for cetak in AbsHasil.__subclasses__():
        cetak.hasil(cetakDsn)
