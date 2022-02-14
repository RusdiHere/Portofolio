import abc


# ----------------Sub Factory A--------------------
# ----------------Abstract Product-----------------
class mobil(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info_mobil(self):
        pass


class motor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info_motor(self):
        pass


# ---------------Concreate product mobil-----------------
class Avanza(mobil):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_mobil(self):
        return ("Mobil : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


class Ayla(mobil):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_mobil(self):
        return ("Mobil : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


class Civic(mobil):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_mobil(self):
        return ("Mobil : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


# ---------------Concreate product motor-----------------
class Vespa(motor):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_motor(self):
        return ("Motor : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


class Beat(motor):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_motor(self):
        return ("Motor : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


class Nmax(motor):
    def __init__(self, warna, tahun_keluaran, jenis):
        self.warna = warna
        self.tahun_keluaran = tahun_keluaran
        self.jenis = jenis

    def info_motor(self):
        return ("Motor : %s, %s, %i") % (self.jenis, self.warna, int(self.tahun_keluaran))


# --------------Concreate factory mobil------------------
class factory_mobil:
    def pilihan_kendaraan(self, pilih):
        if pilih == "Avanza":
            warna = input("Masukan Warna mobil: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Avanza(warna, tahun_keluaran, jenis)

        elif pilih == "Ayla":
            warna = input("Masukan Warna motor: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Ayla(warna, tahun_keluaran, jenis)

        elif pilih == "Civic":
            warna = input("Masukan Warna motor: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Civic(warna, tahun_keluaran, jenis)


# --------------Concreate factory motor------------------
class factory_motor:
    def pilihan_kendaraan(self, pilih):
        if pilih == "Vespa":
            warna = input("Masukan Warna motor: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Vespa(warna, tahun_keluaran, jenis)

        elif pilih == "Beat":
            warna = input("Masukan Warna motor: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Beat(warna, tahun_keluaran, jenis)

        elif pilih == "Nmax":
            warna = input("Masukan Warna motor: ")
            tahun_keluaran = int(input("Masukan Tahun Keluaran: "))
            jenis = pilih
            return Nmax(warna, tahun_keluaran, jenis)


# -------------Abstract Factory-----------
class IAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pilihan_kendaraan(self, pilih):
        pass


class AbstractFactory(IAbstractFactory):
    def __init__(self):
        self.f_mobil = factory_mobil()
        self.f_motor = factory_motor()

    def pilihan_kendaraan(self, pilih):
        try:
            if pilih in ["Avanza", "Ayla", "Civic"]:
                return self.f_mobil.pilihan_kendaraan(pilih)
            elif pilih in ["Vespa", "Beat", "Nmax"]:
                return self.f_motor.pilihan_kendaraan(pilih)
            else:
                raise Exception("Invalid")
        except Exception as _e:
            print(_e)
        return None


# -----------Client------------------
class client:
    def client_mulai(self):
        AbsFactory = AbstractFactory()

        # ------request-------
        pilih = str(input("Masukan nama mobil: "))
        kendaraan = AbsFactory.pilihan_kendaraan(pilih)
        print("Object yang dideskripsikan : ",type(kendaraan))
        print("Spesifikasi : ",kendaraan.info_mobil())

        # ------request---------
        pilih = str(input("Masukan nama motor: "))
        kendaraan = AbsFactory.pilihan_kendaraan(pilih)
        print("Object yang dideskripsikan : ",type(kendaraan))
        print("Spesifikasi : ",kendaraan.info_motor())


# -----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    client1 = client()
    client1.client_mulai()


