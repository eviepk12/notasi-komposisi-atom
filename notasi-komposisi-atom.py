def notasiKomposisiAtom():
    soal = int(input("Tulis nomor proton di bawah kiri lambang atom :"))
    protonElektron = soal 

    soalNeutron = int(input("Tulis nomor massa di atas kiri lambang atom :"))
    neutron = soalNeutron - protonElektron

    print("Proton : ", protonElektron)
    print("Elektron : ", protonElektron)
    print("Neutron :", neutron)

print ("1. Notasi Komposisi Atom")
option = int(input("Ketik nomor yang diinginkan :"))

match option:
    case 1:
        notasiKomposisiAtom()
        exit()
    case _: 
        print("Pilih yang bener!!")

