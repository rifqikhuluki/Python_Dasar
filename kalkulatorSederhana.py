# kalkulator sederhana menggunakan logika percabangan

angka1 = float(input("Masukkan angka 1 = "))
operator = input("Masukkan operasi (+,-,*,/) = ")
angka2 = float(input("Masukkan angka 2 = "))

if operator == "+" :
    hasil = angka1 + angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-" :
    hasil = angka1 - angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*" :
    hasil = angka1 * angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/" :
    hasil = angka1/angka2
    print(f"Hasilnya adalah {hasil}")
else :
    print(f"operasi {operator} tidak valid")
