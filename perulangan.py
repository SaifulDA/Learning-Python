# example for 
var_list = [1, 2, 3, 4, 5]
for i in var_list:
    print(i)

# range
for i in range(10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# while
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
# nested loop
for i in range(1,3):
    for j in range(1,3):
        print(i,j)

# break
for i in range(2):
    print("perulangan luar: ", i)
    for j in range(10):
        print("perulangan dalam: ", j)
        if j == 1:
            break
# example string
for huruf in 'dico ding':
    if huruf == ' ':
        break
    print('huruf saat ini: {}'.format(huruf))

# else setelah for
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print('angka di temukan')
        break
else:
    print('angka tidak di temukan')

# else setelah while
count = 0
while count < 3:
    print('dicoding')
    count += 1
else:
    print('while selesai')

# pass
if x > 5:
    pass
else:
    print('x kurang dari 5')

# list comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
    pangkat.append(n ** 2)
print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n ** 2 for n in angka]
print(pangkat)