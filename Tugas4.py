# Meminta input angka n dari pengguna
n = int(input("Masukkan angka n:"))

# Loop untuk memeriksa setiap angka dari 1 hingga n
for i in range(1, n + 1):
    # Memeriksa apakah angka i adalah ganjil
    if i % 2 != 0:
        # Mencetak angka ganjil
        print(i)