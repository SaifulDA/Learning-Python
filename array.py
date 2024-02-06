# array
import array

x = array.array('i', [1, 2, 3, 4, 5])
print(x)
print(type(x))

# nilai default
var_arr = [0 for i in range(10)]
print(var_arr)

# array nilai
var_arr= [0 for i in range(10)]
for i in range(10):
    var_arr[i] = i
print(var_arr)

# pemprosessan sekuneisal pada array
var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
        print(f'index {i}, nilai {current_element}, index {next_index}, nilai {next_element}')
    else:
        next_element = None
        print(f'current_element : {current_element}, next_element : {next_element}')

# mencari nilai terbesar
var_arr = [1, 7, 2, 89, 8, 88]
left_pointer = var_arr[0]

for i in range (len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer
print(left_pointer)