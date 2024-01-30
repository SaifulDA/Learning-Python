# type data
age = 17
salary = 50000.0

print(type(age))
print(type(salary))

x = 6
print(type(x)) 
x = "6"
print(type(x))
x = 6.0
print(type(x))
x = 1+2j
print(type(x))

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# boolean
x = True
print(type(x))
x = False
print(type(x))

x = 'Halo Dunia'
print(type(x))

# multi line
multi_line = """Halo Dunia.
Ini adalah
multi line string"""
print(multi_line)

# indexing
x = 'Halo Dunia'
print(x[0])
x = 'Halo Dunia'
print(x[4:])

# formatting
name = "John Doe"
print(f"Halo nama saya, {name}!")
name = "John Doe"
print("nama saya %s!" % (name))
name = "John Doe"
print("nama saya adalah".format(name))

#list
x = [1, 2.2, 'python']
print(type(x))

x = [1, 2.2, 'python', True]
print(x[2])

# mutable
x = [1, 2.2, 'python', True]
x[1] = 'apa'
print(x)

#indexing
x = ['laptop', 'mouse', 'keyboard', 'monitor', 'printer', 'speaker', 'flashdisk']
print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

# interval
x = ['laptop', 'mouse', 'keyboard', 'monitor', 'printer', 'speaker', 'flashdisk']
print(x[0:])
print(x[:5])
print(x[0:5:2])

# tuple
x = (1, 2.2, 'python')
print(type(x))
x = (1, 2.2, 'python', True)
print(x[2])
print(x[0:2])

# set
x = {1, 2, 3, 4, 4, 4, 5}
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
union = set1.union(set2)
print("union =", union)

intersection = set1.intersection(set2)
print("intersection =", intersection)

# dictionary
x = {'nama': 'Andi', 'usia': 22, 'status': 'mahasiswa'}
print(type(x))
print(x['nama'])

# add data in dictionary
x = {'nama': 'Andi', 'usia': 22, 'status': 'mahasiswa'}
x['is_married'] = False
print(x)

# delete data in dictionary
x = {'nama': 'Andi', 'usia': 22, 'status': 'mahasiswa'}
del x['usia']
print(x)

# update data in dictionary
x = {'nama': 'Andi', 'usia': 22, 'status': 'mahasiswa'}
x['usia'] = 25
print(x)

# convertion type data
print(int(2.8))
print(float(5))
print(str(6.0))
print(bool(1))

# konversi kumpulan data
print(tuple([1, 2, 3, 4]))
print(list('Halo Dunia'))
print(set([1, 2, 3, 4, 4, 4, 5]))
print(dict([['nama', 'Andi'], ['usia', 22]]))