# Desc: Contoh penggunaan if else
ketersediaan = "daging ayam"

if ketersediaan == "daging ayam":
    print("Saya akan memasak ayam bakar")
else:
    print("Saya akan memasak telur dadar")

score = 90
if score == 90:
    print("Selamat! Anda mendapatkan nilai A")

tinggi_badan = 120

if tinggi_badan >= 160:
    print("Tinggi badan anda sudah ideal")
else:
    print("Tinggi badan anda belum ideal")

# elif
nilai = 65
if nilai > 80:
    print("Selamat! Anda mendapatkan nilai A")
    print("Pertahankan!")
elif nilai > 70:
    print("Selamat! Anda mendapatkan nilai B")
    print("Belajar lebih giat lagi!")
elif nilai > 60:
    print("Selamat! Anda mendapatkan nilai C")
    print("Tingkatkan lagi!")
else:
    print("Maaf, anda tidak lulus mata kuliah ini")
    print("Belajar lebih giat lagi!")

# add and or
nilai = 81
perilaku = "baik"
if nilai >= 80 and perilaku == "baik":
    print("selamat nilai anda A dan berperilaku baik!")
elif nilai >= 80 or perilaku != "A":
    print("selamat nilai anda A atau berperilaku tidak baik!")
else:
    print("belajar lebih giat lagi!")

# tenary operator
lulus = True
print ("selamat") if lulus else print("coba lagi")

# tenary tuple
lulus = True
kelulusan = ("perbaiki", "selamat")[lulus]
print(kelulusan)