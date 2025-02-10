print('####################')
print('Registrasi Jurusan Universitas \n Harapan Cerdas Bangsa ')
print('By Hannah 9B')
print('####################')

print('Jurusan tersedia: \n Keperawatan \n Multimedia \n Apoteker \n Bisnis Daring dan Pemasaran \n Akuntansi dan Keuangan Lembaga \n Teknik Komputer dan Informatika \n Manajemen Perkantoran')
daftar_jurusan = {
    'Keperawatan': 10000000,
    'Multimedia': 8000000,
    'Bisnis Daring dan Pemasaran': 8000000 ,
    'Akuntansi dan Keuangan Lembaga': 7950000,
    'Teknik Komputer dan Informatika': 8500000,
    'Manajemen Perkantoran': 7000000,
}
print('Data Wajib Diisi!!!')
nama= input('Masukkan nama Calon Siswa SMK: ')
pilihan_jurusan = input('Masukkan Jurusan yang diminati: ')
if pilihan_jurusan in daftar_jurusan:
    print(f'Hei {nama}.....\n Jurusan yang anda minati adalah {pilihan_jurusan}')
    print(f'Biaya: Rp {daftar_jurusan[pilihan_jurusan]} Per Semester')
    print('Terima kasih sudah mengisi!')
    print('Silahkan tunggu sebentar ya...')
else:
    print('Maaf jurusan yang anda minati tidak tersedia!')