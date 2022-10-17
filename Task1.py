#Kelas Induk(Parent Class)
class MNatasyaR:
    def __init__(self, nik, nama, jenisKelamin, noHP):
        self.nik = nik
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.noHP = noHP

class Mahasiswa(MNatasyaR):
    def __init__(self, nik, nama, jenisKelamin, noHP, programStudi,kelas):
        super().__init__(nik, nama, jenisKelamin, noHP)
        self.programStudi = programStudi
        self.kelas = kelas

    def cetakAbsensi(self):
        print("-----Absensi Mahasiswa-----")
        print(f"Nama\t: {self.nama}")
        print(f"NIK\t: {self.nik}")
        print("Absensi\t: Hadir ya Bosque\n")

class Dosen(MNatasyaR):
    def __init__(self, nik, nama, jenisKelamin,noHP):
        super().__init__(nik, nama, jenisKelamin, noHP)
    
    def cetakPerkenalan(self):
        print("-----Perkenalan Dosen-----")
        print(f"Nama\t: {self.nama}")
        print(f"No. Hp\t: {self.noHP}\n")


mhs = Mahasiswa(211112080, "M. Natasya Ramadana", "Laki-Laki", "082162205010", "Teknik Informatika", "C")
dsn = Dosen(12345678, "Gojo Satoru", "Laki-Laki", "0812345678")
dsn2 = Dosen(696969, "Koro-Sensei", "Laki-Laki", "0811223344")

mhs.cetakAbsensi()
dsn.cetakPerkenalan()
dsn2.cetakPerkenalan()