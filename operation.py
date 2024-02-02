# list len
contoh_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
print(contoh_list)
print(len(contoh_list))
list_string = "Halo Dunia"
print(list_string)
print(len(list_string))

# min and max
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(angka))
print(max(angka))

# count 
angka = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
print(angka.count(5))
count_string = "Halo Dunia Kita Semua"
print(count_string.count("a"))

# in and not in
kalimat = "Halo Dunia Kita Semua adalah manusia baik"
print("adalah" in kalimat)
print("adalah" not in kalimat)
print("hidup" in kalimat) 
print("hidup" not in kalimat)

# memberikan nilai pada beberapa variabel sekaligus
data = ['shirt', 'white', 'L']
apparel, color, size = data
print(data)
print(apparel)
print(color)
print(size)

# sort
kendaraan = ['motor', 'mobil', 'sepeda', 'becak', 'delman']
kendaraan.sort()
print(kendaraan)
kendaraan.sort(reverse=True)
print(kendaraan)
