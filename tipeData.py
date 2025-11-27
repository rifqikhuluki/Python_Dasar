#integer -> angka satuan
data_integer = 1
print("data : ", data_integer, ", bertipe data : ", type(data_integer))

#float -> angka dengan koma/desimal
data_float = 3.14
print("data : ", data_float, ", bertipe data : ", type(data_float))

#string -> kumpulan karakter
data_string = "Rifqi"
print("data : ", data_string, ", bertipe data : ", type(data_string))

#boolean -> biner -> true/false
data_bool = True
print("data : ", data_bool, ", bertipe data : ", type(data_bool))

#tipe data khusus

#bilangan kompleks
data_complex = complex(7,2)
print("data : ", data_complex, ", bertipe data : ", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(15.60)
print("data : ", data_c_double, ", bertipe data : ", type(data_c_double))

