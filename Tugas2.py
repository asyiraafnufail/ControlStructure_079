# Meminta input bilangan
num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))
num3 = float(input("Masukkan bilangan ketiga: "))

# Memeriksa apakah num1 adalah yang terbesar
if num1 >= num2 >= num3:
    largest = num1

# Memeriksa apakah num2 adalah yang terbesar
elif num2 >= num1 >= num3:
    largest = num2

# Jika semua salah, maka num3 adalah yang terbesar
else:
    largest = num3

# Mencetak bilangan terbesar
print(f"Angka terbesarnya adalah: {largest}")

#tes commit