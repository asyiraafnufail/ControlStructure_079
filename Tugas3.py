# Meminta input dari pengguna untuk jumlah bilangan Fibonacci yang ingin ditampilkan
n = int(input("Masukkan bilangan n: "))

# Inisialisasi dua bilangan pertama Fibonacci
a, b = 0, 1

# Menampilkan pesan awal
print("Bilangan fibonaccinya adalah:")

# Loop untuk menghasilkan deret Fibonacci sebanyak 'n' kali
for i in range(n):
    # Memeriksa apakah bilangan Fibonacci saat ini <= 10 dan mencetaknya
    if a <= 10:
        print(a, end=" ")
    # Mengupdate nilai a dan b ke bilangan berikutnya dalam deret Fibonacci
    a, b = b, a + b

# Menambahkan baris baru setelah output selesai
print()