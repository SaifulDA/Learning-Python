# example 1
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)

# positional-or-keyword
def greeting (nama, pesan):
    return "helo, " + nama + "!" + pesan
print(greeting("dico", "apa kabar?"))
print(greeting(nama="dico", pesan="apa kabar?"))

# positional-only
def penjumlahan (a,b,/):
    return a + b
print(penjumlahan(1,2))

# keyword-only
def greeting (*, nama, pesan):
    return "helo, " + nama + "!" + pesan
print(greeting(pesan="apa kabar?", nama="dico"))

# variadic positional
def hitung_total(*args):
    print(type(args))
    total = (sum(args))
    return total
print(hitung_total(1,2,3,4,5))

# variadic keyword
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ","
    return info
print(cetak_info(nama="dico", umur="24", pekerjaan="guru"))

# fungsi lambda
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
print(mencari_luas_persegi_panjang(10, 5))

# variabel global
a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

# variabel lokal
def add(a,b):
    lokal_var = 5
    result = a+b-lokal_var
    return result
bilanganPertama = add(20,10)
print(bilanganPertama)