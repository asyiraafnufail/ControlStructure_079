#MInta pengguna masukkan presentase nilai
percentage = float(input("Masukkan presentasenya: "))

#Periksa jika presentase diatas 90 maka akan print tulisan "Excellent"
if percentage >= 90:
    print("Excellent")

#Periksa jika presentase diatas 80 maka akan print tulisan "Very good"
elif percentage >= 80:
    print("Very Good")

#Periksa jika presentase diatas 70 maka akan print tulisan "Good"
elif percentage >= 70:
    print ("Good")

#Periksa jika presentase diatas 60 maka akan print tulisan "Average"
elif percentage >= 60:
    print ("Average")

#Periksa jika presentase dibawah 60 maka akan print tulisan "Needs improvement"
else:
    print ("Needs improvement")