# example 1
class Mobil:
    warna = "merah"
mobil_1 = Mobil()
print(mobil_1.warna)

# example 2
class Mobil:
    warna = "merah"
mobil_1 = Mobil()
mobil_1.warna = "biru"
print(mobil_1.warna)

# example 3
class Mobil:
    warna = "merah"

mobil1= Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# mengubah atribut kelas
Mobil.warna = "biru"
print(mobil1.warna)
print(mobil2.warna)

# example 4
class Mobil:
    # atribut instance
    def __init__(self):
        self.warna = "merah"

mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# mengubah atribut instance
mobil_1.warna = "biru"

print(mobil_1.warna)
print(mobil_2.warna)

# example 5
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
mobil1 = Mobil("merah", "toyota", 100)

print(mobil1.warna)
print(mobil1.merek)
print(mobil1.kecepatan)

# example 6
def my_decorator(func):
    def wrapper():
        print("Sebelum eksekusi fungsi")
        func()
        print("Setelah eksekusi fungsi")
    return wrapper
# dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Halo, World!")
# memanggil fungsi yang sudah didekorasi
say_hello()

# example 7
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil1 = Mobil("merah", "toyota", 100)
print("sebelum tambah kecepatan")
print(mobil1.kecepatan)

mobil1.tambah_kecepatan()
print("setelah tambah kecepatan")
print(mobil1.kecepatan)

# example 8 staticmethod
class Mobil:
    def __init__(self, warna):
        self.warna = warna

    @staticmethod
    def intro_mobil():
        print("ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil1 = Mobil("merah")
mobil1.intro_mobil()

# example 9 metode class
class Mobil:
    jumlah_mobil = 0
    def __init__(self, merek):
        self.merek = merek
        
    @classmethod
    def intro_mobil(cls):
        print("ini adalah metode dari kelas Mobil")

Mobil.intro_mobil()
mobil1 = Mobil("toyota")
mobil1.intro_mobil()

# inheritance
class Mobil:
    def __init__(self, merek, warna, kecepatan):
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
# kelas mobil dasar
mobil1 = Mobil("toyota", "merah", 100)
print(mobil1.kecepatan)

# kelas mobil sport
mobil_sport_1 = MobilSport("ferrari", "biru", 100)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)

# example 10
class Mobil:
    def __init__(self, merek, warna, kecepatan):
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan
    def tambah_kecepatan(self):
        self.kecepatan += 10

class mobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        self.kecepatan += 20

# kelas mobil sport
mobil_sport_1 = mobilSport("Ferari", "hitam", 160 )
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)

# example 11 super
class Mobil:
    def __init__(self, merek, warna, kecepatan):
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan
    def tambah_kecepatan(self):
        self.kecepatan += 10

class mobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("kecepatan anda meningkat 10 km/jam")
# kelas mobil sport
mobil_sport_1 = mobilSport("Ferari", "hitam", 160 )
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)