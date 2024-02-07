# example 1
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriks)

# menggunakan numpy
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

# cek memory
import sys
import numpy as np

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("ukuran list dalam bytes: ", sys.getsizeof(var_list)*len(var_list))
print("ukuran array dalam bytes: ", var_array.size * var_array.itemsize)

# operasi matriks
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)


# indexing 
var_mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12],
           [13, 14, 15],
           [16, 17, 18],
           [19, 20, 21],
           [22, 23, 24],
           [25, 26, 27],
           [28, 29, 30]]
print(var_mat[2][1])

# membuat matriks 2x2
var_mat = [[1, 2],
            [3, 4]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2
print(def_mat)

# menggunakan numpy
import numpy as np

var_mat = np.array([[1, 2],
                    [3, 4]])
result = var_mat * 2
print(result)