import abc
import math

# ================= Product Interface =================
class bangun_ruang(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def menghitung_luas(self):
        pass

    @abc.abstractmethod
    def menghitung_keliling(self):
        pass
# ===============================================

# ================= Concreate Product =================
class segitiga(bangun_ruang):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def menghitung_luas(self):
        return 0.5*self.alas * self.tinggi
    def menghitung_keliling(self):
        return self.alas + self.tinggi + math.sqrt(self.alas**2 + self.tinggi**2)

class persegi(bangun_ruang):
    def __init__(self, sisi):
        self.sisi = sisi
    def menghitung_luas(self):
        return self.sisi ** 2
    def menghitung_keliling(self):
        return 4 * self.sisi
    
class lingkaran(bangun_ruang):
    def __init__(self, radius):
        self.radius = radius
    def menghitung_luas(self):
        return 3.14 * self.radius * self.radius
    def menghitung_keliling(self):
        return 2 * 3.14 * self.radius
# ================================================

# =====================  Creator ====================
class factory_bangun_ruang:
    def create_bangun(self, nama_bangun):
        if nama_bangun == "segitiga":
            alas = float(input("Masukan alas segitiga: "))
            tinggi = float(input("Masukan tinggi segitiga: "))
            return segitiga(alas,tinggi)
        
        elif nama_bangun == "persegi":
            sisi = float(input("Masukan sisi persegi: "))
            return persegi(sisi)
        
        elif nama_bangun == "lingkaran":
            radius = float(input("Masukan radius lingkaran: "))
            return lingkaran(radius)
# ================================================

# ================= Concreate Creator =================
class client:
    def client_start(self):
        # Intansiasi Factory
        factory = factory_bangun_ruang()

        # Client Request
        nama_bangun = str(input("Masukan nama bangun yang ingin dibuat: "))
        bangun = factory.create_bangun(nama_bangun)
        print("Object yang dibuat : ",type(bangun))
        print("Luas Object : ",bangun.menghitung_luas())
        print("Keliling Objek : ",bangun.menghitung_keliling())
# ================================================

if __name__ == "__main__":  
    client1 = client()
    client1.client_start()



    
