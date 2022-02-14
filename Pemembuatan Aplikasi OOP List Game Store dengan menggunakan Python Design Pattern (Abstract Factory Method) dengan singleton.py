import abc
import math
#----------SubfactoryA--------
#----------Abstract factoryA----
class game_pc(metaclass=abc.ABCMeta):
    def __init__(self):
        self.list_game = []
        
    @abc.abstractmethod
    def create_game(self):
        pass

    def ganti_info(self, nomor_urut_game, informasi_baru):
        self.list_game[nomor_urut_game-1] = informasi_baru

    def start_pilihan(self):
        nomor_urut_game = 1
        for game in self.list_game:
            print("%i. %s"%(nomor_urut_game,game))
            nomor_urut_game += 1
#-------Concreate Product---------
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class FarCry2(game_pc):
    def create_game(self):
        self.list_game.append(" Developer : Ubisoft ")
        self.list_game.append(" Size : 2.42GB ")
        self.list_game.append(" Genre : FPS ")
            
@singleton
class ResidentEvilIV(game_pc):
    def create_game(self):
        self.list_game.append(" Developer : Konami ")
        self.list_game.append(" Size : 16GB ")
        self.list_game.append(" Genre : Action, Horor, FPS ")

@singleton
class GTAV(game_pc):
    def create_game(self):
        self.list_game.append(" Developer : RockStar ")
        self.list_game.append(" Size : 99GB ")
        self.list_game.append(" Genre :Adventure ")
#-------------Concreate Factory-------------
class factory_Game_PC:
    def get_game(self, Game):
        if Game == "FarCry2":
            return FarCry2()
        
        elif Game == "Resident Evil 6":
            return ResidentEvilIV()
        
        elif Game == "GTAV":
            return GTAV()
#-----------Sub FactoryB----------
#-----------Abstract Product-------
class Game_PS4(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deskripsi_game_PS4(self):
        pass
#----------Concreat Product---------------
class GodOfWar(Game_PS4):
    def deskripsi_game_PS4(self):
        print("God of War adalah franchise game aksi-petualangan yang dibuat oleh David Jaffe di Sony's Santa Monica Studio")
        
class PES2020(Game_PS4):
    def deskripsi_game_PS4(self):
        print("PES 2020 adalah video game simulasi sepak bola yang dikembangkan oleh PES Productions dan diterbitkan oleh Konami")
        
class DevilMayCry(Game_PS4):
    def deskripsi_game_PS4(self):
        print("Devil May Cry adalah seri video game aksi-petualangan yang dikembangkan dan diterbitkan oleh Capcom dan dibuat oleh Hideki Kamiya")
#--------Concreate Factory-----------
class factory_Game_PS4:
    def get_game(self, Game):
        if Game == "God Of War":
            return GodOfWar()
    
        elif Game == "PES 2020":
            return PES2020()
        
        elif Game == "Devil May Cry":
            return DevilMayCry()
#---------Abstract Factory-----------
class IAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_game(self, Game):
        pass

class AbstractFactory(IAbstractFactory):
    def __init__(self):
        self.Game_PC= factory_Game_PC()
        self.Game_PS4 = factory_Game_PS4()
        
    def get_game(self, Game):
        try:
            if Game in ["FarCry2","Resident Evil 6","GTAV"]:
                return self.Game_PC.get_game(Game)
            elif Game in ["God Of War","PES 2020","Devil May Cry"]:
                return self.Game_PS4.get_game(Game)
            else:
                raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
#--------------Client-----------------
class client:
    def client_start(self):
        # Intansiasi Abstract Factory
        AbsFactory = AbstractFactory()

        # Staff
        staff1 = AbsFactory.get_game("FarCry2")
        staff2 = AbsFactory.get_game("Resident Evil 6")
        staff3 = AbsFactory.get_game("GTAV")
        staff1.create_game()
        staff2.create_game()
        staff3.create_game()
        
        # Customer mendapat info game PS4
        print("======= DESKRIPSI GAME PS 4 =======")
        customer1 = AbsFactory.get_game("God Of War")
        customer2 = AbsFactory.get_game("PES 2020")
        customer3 = AbsFactory.get_game("Devil May Cry")
        
        customer1.deskripsi_game_PS4()
        customer2.deskripsi_game_PS4()
        customer3.deskripsi_game_PS4()

        # Check singleton
        print("======= Customer4 Memilih Game Resident Evil 6 =======")
        customer4 = AbsFactory.get_game("Resident Evil 6")
        customer4.start_pilihan() # Terdapat kesalahan informasi
        
        print("============== Ganti Informasi ============")
        staff2.ganti_info(1," Developer : Capcom") # informasi diperbaiki 
        customer4.start_pilihan() # Refresh

#-------------------------------------------------------------------------------------
if __name__ == "__main__":  
    client1 = client()
    client1.client_start()
        
