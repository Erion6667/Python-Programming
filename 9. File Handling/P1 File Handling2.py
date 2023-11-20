import os

print("Menu Menulis dan Membaca")

while True:
    print()
    print("""Berikut daftar dari menu menulis dan membaca
          1. Menulis teks baru
          2. Melanjutkan menulis
          3. Membaca teks
          4. Keluar
          Note: Jika file belum ada tidak bisa mencoba menu 2 dan 3""")
    choose = int(input("Apa yang ingin anda lakukan? (1/2/3/4) "))
    print()
    if choose == 1:
        while True:
            listfile = os.listdir()
            filename = input('Masukan nama file baru: ').lower()
            if filename +'.txt' in listfile:
                print("File tersebut sudah ada, silahkan ganti dengan nama baru!")
                continue
            else:
                with open(filename + '.txt', 'x') as tl:
                    tl.writelines(input('Apa yang ingin anda tulis? '))
                    print('Menu menulis sudah berakhir')
                    break
        break
    elif choose == 2:
        listfile = os.listdir()
        filename = input("Masukan nama file yang ingin ditambahkan: ").lower
        if filename + '.txt' in listfile:
            with open(filename + '.txt', 'a') as lj:
                isi = input('Apa yang ingin anda tambahkan? ')
                lj.writelines(isi)
                print("Penambahan", isi, "berhasil dilakukan")
        else:
            print("Nama file yang ingin ada edit tidak tersedia, pastikan nama file sudah benar!")
    elif choose == 3:
        listfile = os.listdir()
        filename = input("Masukkan nama file yang ingin dibaca: ").lower()
        if filename + '.txt' in listfile:
            with open(filename + '.txt', 'r') as bc:
                print(bc.read())
        else:
            print("File yang ingin anda baca tidak tersedia, pastikan nama file sudah benar!")
    elif choose == 4:
        print('Menu menulis dan membaca sudah berakhir')
        break
    else:
        print("Pilihlah pilihan yang benar!")
        continue
    