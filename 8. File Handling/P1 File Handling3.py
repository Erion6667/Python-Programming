print("Daftar nama Kelas 1 D4 SD A")
f = open("daftarnama.txt", 'w')
f.close()
while True:
  insert = input("Masukkan nama: ")
  f = open("daftarnama.txt", "r")
  nama = f.readlines()
  names=[i[0:-1] for i in nama]
  f.close()
  if insert in names:
    print("Nama sudah ada pada daftar.")
  else:
    with open("daftarnama.txt", "a") as f:
      f.write(insert+"\n")
    
  repeat = input("Ulangi masukkan nama?(y/t): ")
  if repeat.lower() == "y":
    continue
  elif repeat.lower() == "t":
        f = open("daftarnama.txt", "r")
        nama = f.readlines()
        names=[i[0:-1] for i in nama]
        print(names)
        break
  else:
    print("masukkan pilihan yang benar!") 

