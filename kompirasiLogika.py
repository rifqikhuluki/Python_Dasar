#++++++++3-------10+++++++
inputUser = float(input("Masukkan angka kurang dari 3 atau lebih dari 10 = "))

#periksa < 3
isKurangDari3 = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari3)

#periksa > 10
isLebihdari10 = (inputUser > 10)
print("Lebih dari 10 = ", isLebihdari10)

#periksa logika or
isCorrect = (isKurangDari3 or isLebihdari10)
print("angka yang anda masukkan = ", isCorrect)

print("\n", 15*"=", "\n")
#--------3+++++++10------
inputUser = float(input("Masukkan angka kurang dari 3 dan lebih dari 10 = "))

# periksa > 3
isLebihDari3 = (inputUser > 3)
print("Kurang dari 3 = ", isLebihDari3)

#periksa < 10
isKurangDari10 = (inputUser < 10)
print("Lebih dari 10 = ", isKurangDari10)

#periksa logika and
isCorrect = (isLebihDari3 and isKurangDari10)
print("angka yang anda masukkan = ", isCorrect)