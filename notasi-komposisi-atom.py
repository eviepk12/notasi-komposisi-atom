# Sekumpulan program untuk membantu tugas tugas kimia kls 10
# made by zainal

def notasiKomposisiAtom():
    soal = int(input("Tulis nomor atom di bawah kiri lambang :"))
    protonElektron = soal 

    soalNeutron = int(input("Tulis nomor massa di atas kiri lambang atom :"))
    neutron = soalNeutron - protonElektron

    print("Proton : ", protonElektron)
    print("Elektron : ", protonElektron)
    print("Neutron :", neutron)

def notasiKomposisiAtomBermuatan():
    soal = int(input("Tulis nomor atom di bawah kiri lambang :"))
    mass = int(input("Tulis nomor massa di atas kiri lambang :"))
    muatan = int(input("Tulis muatan di kanan atas lambang :"))

    proton = soal

    if muatan == "+":
        elektron = proton - 1
    if muatan == "-":
        elektron = proton + 1
    else:
        print("Tulis muatan dengan benar!")

    neutron = mass - proton

    print("Proton :", proton)
    print("Elektron :", elektron)
    print("Neutron :", neutron)

def konfigurasiBohr():
    print ("Tulis nomor massa di bawah lambang :")

print ("1. Notasi Komposisi Atom")
print ("2. Notasi Komposisi Atom Dengan Muatan")
print ("3. Konfigurasi Elektron Bohr \n")
option = int(input("Ketik nomor yang diinginkan :"))

match option:
    case 1:
        notasiKomposisiAtom()
        exit()
    case 2:
        notasiKomposisiAtomBermuatan()
        exit
    case _: 
        print("Pilih yang bener!!")

