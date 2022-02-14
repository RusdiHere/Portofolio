class Biografi:
  def __init__ (self, nama, alamat):
    self.nama = nama
    self.alamat = alamat

  def perkenalan (self):
    print(f'Perkenalkan nama saya {self.nama} dari {self.alamat}')
    
class Pekerjaan_Bekerja (Biografi):
  def __init__ (self, nama, alamat, pekerjaan):
    Biografi.__init__(self, nama, alamat)
    self.pekerjaan = pekerjaan

class Pekerjaan_Sekolah(Biografi):
  def __init__ (self, nama, alamat, pekerjaan):
    super().__init__(nama, alamat)
    self.pekerjaan = pekerjaan


Andi = Biografi('Andi', 'Surabaya')
Andi.perkenalan()
Deni = Pekerjaan_Sekolah('Deni', 'Makassar', 'SMA Negeri 1 Makassar')
Deni.perkenalan()
print(f'Saya sekolah di {Deni.pekerjaan}')

Budi = Pekerjaan_Bekerja('Budi', 'Pontianak', 'Google')
Budi.perkenalan()
print(f'Saya bekerja di {Budi.pekerjaan}')

