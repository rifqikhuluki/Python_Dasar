# countinue, pass, break

# pass -> berfungsi sebagai dummy, tidak akan di eksekui

angka = 0

while angka < 5 :
    angka += 1

    if angka == 3 :
        pass# tidak di eksekusi
    
    print(angka)

while angka < 5 :
    angka += 1

    if angka == 3 :
        continue
    
    print(angka)