names = ['bayu\n''alde\n']
file = 'text.txt'
while True:
    print('a. lihat nama yang sudah tersimpan \nb. tambahkan nama\nc. tutup')
    c = input('pilih a/b/c: ')
    if c == 'a':
        d = open(file,'r')
        print(d.read())
        d.close()
    elif c =='c':
        e = input('masukkan nama: ')
        f = open(file, 'a')
        f.writelines(names)
        f.close()
        g = open(file,'r')
        print(g.read())
        g.close()
    else:
        break