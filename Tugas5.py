# Meminta input nilai n dari pengguna
n = int(input("Masukkan nilai n: "))

# Loop untuk mengatur baris (1 hingga n)
for i in range(1, n + 1):
    # Loop untuk mencetak angka sebanyak nilai baris saat ini
    for j in range(i):
        print(i, end=" ")  # Mencetak angka di baris yang sama
# Menambahkan baris baru setelah selesai mencetak semua baris
print()
