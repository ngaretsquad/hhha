print("Menghitung Waktu Jarak dan Kecepatan :")
def option():
	print("1.waktu tempuh")
	print("2.jarak")
	print("3.kecepatan rata rata")
	print("4.keluar")
	pilihan = int (input("masukan pilihan anda : "))
	return pilihan
	
pilihan = True 
while (pilihan<4) :
	pilihan = option()
	if (pilihan==1):
		kotaasal=str(input("Masukan nama kota asal : "))
		kotatujuan=str(input("Masukan nama kota tujuan : "))
		jarak=int(input("masukan jarak antar kota : " ))
		kecepatan=int(input("kecepatan rata-rata kendaraan : "))
		waktutempuh=jarak/kecepatan
		print("Waktu Yang Anda Tempuh : %.2f"%(waktutempuh),"Jam")
		print("=====================================================\n")