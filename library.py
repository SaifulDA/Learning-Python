# regex
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import math
import re     # Import modul regex

pola = '^a...s$'
string_tes = 'abyss'
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")

# math

print(math.sqrt(25))
print(math.pi)

# numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

# matplotlib

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Membuat plot garis
plt.plot(x, y)

# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

# Menampilkan plot
plt.show()

# seaborn

# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn

# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

# json

# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'

# parse  x:
y = json.loads(x)

print(y["umur"])

# beautifulsoup4

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)

# urllib

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)
