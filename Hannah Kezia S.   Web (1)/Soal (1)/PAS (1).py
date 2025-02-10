#Dictionary minat dan karir
minat_karir = {
    "teknologi":"Programmer,Data Scientist,Cybersecurity Spesialist",
    "seni":"Desainer Grafis,Pelukis,Animator",
    "musik":"Musisi,Komposer,Produser Musik",
    "olahraga":"Atlet,Pelatih,Fisioterapis Olahraga",
    "menulis":"Penulis,Editor,Jurnalis",
    "bisnis":"Pengusaha,Manager,Kunsultan Bisnis",
    "kesehatan":"Dokter,Perawat,Terapis",
    "memasak":"Koki,Ahli Gizi,Pemilik Restoran",
}
#input minat pengguna
print("Minat yang tersedia:",",".join(minat_karir.keys()))
nama= input("Hai... Masukan namamu ya:")
minat = input("Masukan minat Anda:").lower()

#Pencarian karir yang cocok
if minat in minat_karir:
    print(f"\nMinat Anda:{minat.capitalize()}")
    print(f"Karir masa depan yang cocok:{minat_karir[minat]}")
    print(f"Selamat {nama}! Semoga kamu dapat menjadi seorang {minat_karir[minat].split(',')[0]}.")
else:
    print(f"\nMaaf,minat tersebut belum tersedia di daftar kami.")
    print(f"Tetap semangat,{nama}! Temukan karir impianmu yang sesuai dengan minatmu.")

print('☺️')
print('Termakasih sudah mencoba program ini ya.')