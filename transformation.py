# upper
kata = "belajar python"
kata = kata.upper()
print(kata)

#lower
kata = "BELAJAR PYTHON"
kata = kata.lower()
print(kata)

#rstrip
print("python     ".rstrip())
#lstrip
print("     python".lstrip())
#strip
print("     python     ".strip())

kata = 'CodeCodePythonCodeCode'
print(kata.strip('Code'))

#startswith
print("python".startswith("py"))
#endswith
print("python".endswith("py"))

#join
print(" ".join(["Halo", "Dunia"]))
print ('adalah'.join(['halo', 'dunia', 'kita']))

#split
print("Halo Dunia".split())
print('''Halo
      Dunia
      Kita'''.split('\n'))

#replace
string = "Halo Dunia Kita Semua"
print(string.replace("Semua", "Semuanya"))

#checking
#isUpper
kata = "BELAJAR PYTHON"
print(kata.isupper())
#isLower
kata = "belajar python"
print(kata.islower())
#isAlpha
kata = "belajarpython"
print(kata.isalpha())
#isalnum
kata = "belajarpython123"
print(kata.isalnum())
#isdecimal
kata = "123"
print(kata.isdecimal())
#isspace
print("      ".isspace())
#istitle
print("Halo Dunia".istitle())

#zfill
teks = 'code'
tambah_teks = teks.zfill(10)
print(tambah_teks)

#rjust
teks = 'code'
tambah_teks = teks.rjust(10)
print(tambah_teks)

#ljust
teks = 'code'
tambah_teks = teks.ljust(10)
print(tambah_teks)

#center
teks = 'code'
tambah_teks = teks.center(10)
print(tambah_teks)

#string literal
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
#raw string
print(r'Dicoding\tIndonesia')