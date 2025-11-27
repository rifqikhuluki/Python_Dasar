#operasi aritmatika

a = 10
b = 5

#operasi penambahan
hasilPenambahan = a + b
print(a, '+', b,'=', hasilPenambahan )

#operasi pengurangan
hasilPengurangan = a - b
print(a, '-', b, '=', hasilPengurangan)

#operasi perkalian
hasilPerkalian = a*b
print(a, '*', b, '=', hasilPerkalian)

#operasi pembagian
hasilPembagian = a/b
print(a, '/', b, '=', hasilPembagian)

#operasi ekspoen (pangkat) **
hasilEksponen = a ** b
print(a, '**', b, '=', hasilEksponen)

#operasi modulus
hasilModulus = a % b
print(a, '%', b, '=', hasilModulus)

#operasi floor division //
hasilFloor = a // b
print(a, '//', b, '=', hasilFloor)

#prioritas operasi
x = 5
y = 2
z = 8

hasilPrioritas = x ** y * z + x / y - x % z // y
print(x, '**', y, '*', z, '+', x, '/', y, '-', x, '%', z, '//', y, '=', hasilPrioritas)