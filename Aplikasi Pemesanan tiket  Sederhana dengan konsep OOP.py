import abc
import math
import string
import random

class tipe_kamar(metaclass=abc.ABCMeta):        
    @abc.abstractmethod
    def get_info_kamar(self):
        pass
    
    @abc.abstractmethod
    def get_total_sewa(self):
        pass
    
    def set_reservasi(self):
        self.nama_tamu = str(input("Masukan nama : "))
        self.jumlah_tamu = int(input("Masukan jumlah tamu: "))
        self.sarapan = str(input("Dengan Sarapan (ya/tidak): "))
        self.bebas_asap = str(input("Kamar bebas asap rokok (ya/tidak): "))
        if self.sarapan == "ya":
            self.sarapan = True
        else:
            self.sarapan = False
        if self.bebas_asap == "ya":
            self.bebas_asap = True
        else:
            self.bebas_asap = False
            
class deluxe(tipe_kamar):
    def get_info_kamar(self):
        print("< ========= Deluxe Room ========= >")
        print("Surround yourself with simple elegance in this 40-square meter beautifully appointed Deluxe Room. Equipped with large LED screens and high speed broadband internet access, guests staying in our Deluxe Room will also receive a complimentary mini bar and access to Gaharu Spa and Fitness. Smoking or non-smoking rooms are available on request, however will only be confirmed at check-in. Including Breakfast for 2 adult and 2 children under 6 years old. (Full charge for additional breakfast children more than 6 years old).")
        print("< ============================= >")
        
    def get_total_sewa(self):
        if self.jumlah_tamu > 2:
            biaya_extra_tamu = (self.jumlah_tamu - 2) * 100000
        else:
            biaya_extra_tamu = 0
        if self.sarapan :
            biaya_sarapan = self.jumlah_tamu * 25000
        else:
            biaya_sarapan = 0
        if self.bebas_asap :
            biaya_bebas_asap = 50000
        else:
            biaya_bebas_asap = 0
        total_sewa = 100000 + biaya_extra_tamu + biaya_sarapan +biaya_bebas_asap
        print("Total : ",total_sewa)
        return total_sewa

class executive_suite(tipe_kamar):
    def get_info_kamar(self):
        print("< ========= Executive Suite Room ========= >")
        print("We offer elegant accommodations and exclusive benefits including continental breakfast, daily refreshments, VIP express check-in at executive lounge.")
        print("< =================================== >")
        
    def get_total_sewa(self):
        if self.jumlah_tamu > 2:
            biaya_extra_tamu = (self.jumlah_tamu - 2) * 200000
        else:
            biaya_extra_tamu = 0
        if self.sarapan :
            biaya_sarapan = self.jumlah_tamu * 25000
        else:
            biaya_sarapan = 0
        if self.bebas_asap :
            biaya_bebas_asap = 50000
        else:
            biaya_bebas_asap = 0
        total_sewa = 5000000 + biaya_extra_tamu + biaya_sarapan +biaya_bebas_asap
        print("Total : ",total_sewa)
        return total_sewa
    
class interconnecting_two_bedroom(tipe_kamar):
    def get_info_kamar(self):
        print("<=========Interconnecting Two Bedroom=======>")
        print("Interconnecting Deluxe Breakfast for 4 persons. 2 Bedroom Double bed and Twin bed. This room suitable for your fan")
        print("<===========================================>") 

    def get_total_sewa(self):
        if self.jumlah_tamu > 2:
            biaya_extra_tamu = (self.jumlah_tamu - 2)* 300000
        else:
            biaya_extra_tamu = 0
        if self.sarapan :
            biaya_sarapan =self.jumlah_tamu*50000
        else:
            biaya_sarapan = 0
        if self.bebas_asap :
            biaya_bebas_asap =50000
        else:
            biaya_bebas_asap = 0
        total_sewa = 5000000 + biaya_extra_tamu + biaya_sarapan + biaya_bebas_asap 
        print("Total: ", total_sewa)
        return total_sewa
         
class factory_tipe_kamar:
    def get_kamar(self, tipe_kamar):
        if tipe_kamar == "deluxe":
            return deluxe()
        elif tipe_kamar == "executive_suite":
            return executive_suite()
        elif tipe_kamar == "interconnecting_two_bedroom":
            return interconnecting_two_bedroom()

class tipe_transportasi(metaclass=abc.ABCMeta):
    def pesan_tiket(self):
        self.nama_penumpang = str(input("Masukan nama anda : "))
        self.jumlah_penumpang = int(input("Masukan jumlah penumpang : "))
        self.kota_asal = str(input("Masukan kota asal (jakarta/bandung/jogja) : "))
        self.kota_tujuan = str(input("Masukan kota tujuan (jakarta/bandung/jogja) : "))
        
    @abc.abstractmethod
    def get_total_bayar(self):
        pass
    
class kereta(tipe_transportasi):
    def get_total_bayar(self):
        if self.kota_tujuan == "jakarta":
            biaya_perjalanan = 100000
        elif self.kota_tujuan == "bandung":
            biaya_perjalanan = 75000
        elif self.kota_tujuan == "jogja":
            biaya_perjalanan = 25000

        total_biaya = biaya_perjalanan * self.jumlah_penumpang
        print("Total biaya : ",total_biaya)
        return total_biaya

class pesawat(tipe_transportasi):
    def get_total_bayar(self):
        if self.kota_tujuan == "jakarta":
            biaya_perjalanan = 250000
        elif self.kota_tujuan == "bandung":
            biaya_perjalanan = 120000
        elif self.kota_tujuan == "jogja":
            biaya_perjalanan = 75000

        total_biaya = biaya_perjalanan * self.jumlah_penumpang
        print("Total biaya : ",total_biaya)
        return total_biaya
    
class factory_tiket:
    def get_tiket(self, tipe_transportasi):
        if tipe_transportasi == "kereta":
            return kereta()
        elif tipe_transportasi == "pesawat":
            return pesawat()

class pembayaran(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bayar(self):
        pass

class bank_transfer(pembayaran):
    def bayar(self,nominal):
        print("Silahkan lakukan transfer sejumlah %i pada : 1223-1244-8777-9808 (Bank ACB a/n Budi)"%(nominal))

class indoagustus(pembayaran):
    def bayar(self,nominal):
        # Generate Transaction Code
        size = 10
        chars = string.ascii_uppercase + string.digits
        kode_transaksi = "".join(random.choice(chars) for _ in range(size))
        print("Silahkan lakukan pembayaran dengan menunjukan kode : %s pada kasir Indoagustus. "%(kode_transaksi))

class factory_pembayaran:
    def get_pembayaran(self, tipe_pembayaran):
        if tipe_pembayaran == "bank_transfer":
            return bank_transfer()
        elif tipe_pembayaran == "indoagustus":
            return indoagustus()

class IAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_fitur(self, nama_bangun):
        pass

class AbstractFactory(IAbstractFactory):
    def __init__(self):
        self.tiket= factory_tiket()
        self.tipe_kamar = factory_tipe_kamar()
        self.pembayaran = factory_pembayaran()
        
    def get_fitur(self, user_request):
        try:    
            if user_request in ["deluxe","executive_suite", "interconnecting_two_bedroom"]:
                return self.tipe_kamar.get_kamar(user_request)
            elif user_request in ["pesawat","kereta"]:
                return self.tiket.get_tiket(user_request)
            elif user_request in  ["bank_transfer","indoagustus"]:
                return self.pembayaran.get_pembayaran(user_request)
            else:
                raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None

class application:
    def __init__(self):
        self.abstractFact = AbstractFactory()
        
    def main_menu(self):
        print("Selamat datang di aplikasi GamaTravel, silahkan memilih layanan yang diinginkan: ")
        print("1) Reservasi Hotel")
        print("2) Pemesanan Tiket")
        user_command = int(input("Masukan pilihan anda (contoh : 1) = "))
        self.command_handler(user_command)
        
    def command_handler(self, user_command):
        if user_command == 1 :
            print("Silahkan pilih hotel yang diinginkan: ")
            print("1) Jogja Indah Hotel")
            print("2) Amabrukmo Hotel")
            print("3) Malioboro Hotel")
            user_command_hotel = int(input("Masukan pilihan anda (contoh : 1) = "))
            if user_command_hotel == 1:
                nama_hotel = "Jogja Indah Hotel"
            elif user_command_hotel == 2 :
                nama_hotel = "Amabrukmo Hotel"
            elif user_command_hotel == 3 :
                nama_hotel = "Malioboro Hotel"
    
            print("Silahkan pilih tipe kamar yang diinginkan: ")
            print("1) deluxe")
            print("2) executive_suite")
            print("3) interconnecting_two_bedroom ")
            tipe_kamar = int(input("Masukan pilihan anda (contoh : 1) = "))
            if tipe_kamar == 1:
                kamar = self.abstractFact.get_fitur("deluxe")
            elif tipe_kamar == 2 :
                kamar = self.abstractFact.get_fitur("executive_suite")
            elif tipe_kamar == 3 :
                kamar = self.abstractFact.get_fitur("interconnecting_two_bedroom")
            
            print(type(kamar))
            kamar.get_info_kamar()
            kamar.set_reservasi()
            total_bayar = kamar.get_total_sewa()
            
        elif user_command == 2 :
            print("Silahkan pilih transportasi yang diinginkan: ")
            print("1) kereta")
            print("2) pesawat")
            tipe_transportasi = int(input("Masukan pilihan anda (contoh : 1) = "))
            if tipe_transportasi == 1:
                transportasi = self.abstractFact.get_fitur("kereta")
            elif tipe_transportasi == 2 :
                transportasi = self.abstractFact.get_fitur("pesawat")
            transportasi.pesan_tiket()
            total_bayar = transportasi.get_total_bayar()

        print("Silahkan pilih metode pembayaran : ")
        print("1) bank_transfer")
        print("2) indoagustus")  
        tipe_pembayaran = int(input("Masukan pilihan anda (contoh : 1) = "))
        if tipe_pembayaran == 1:
            pembayaran = self.abstractFact.get_fitur("bank_transfer")
        elif tipe_pembayaran == 2 :
            pembayaran = self.abstractFact.get_fitur("indoagustus")
        pembayaran.bayar(total_bayar)
        
if __name__ == "__main__":  
    client1 = application()
    client1.main_menu()

