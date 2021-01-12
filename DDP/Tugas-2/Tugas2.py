import random
import string


def buka_rekening():  # Mutia
    print("*** BUKA REKENING ***")
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    nama = input("Masukkan nama: ")
    setoran = eval(input("Masukkan setoran awal: "))
    f = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt', 'a+')
    f.write(norek + ', ' + nama + ', ' + str(setoran) + '\n')
    f.close()
    print("Pembukaan rekening dengan nomor ",
          norek, "atas nama ", nama, "berhasil.\n")
    return menu()


def setoran_tunai():  # Wahyu
    print("\n*** SETORAN TUNAI ***")
    rek_setor = input("Masukkan nomor rekening: ").upper()
    nominal_setor = eval(input("Masukkan nominal yang akan disetor: "))

    a_file = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt')
    f_nasabah = []
    for data in a_file:
        d_nasabah = data.strip().split(', ')
        if rek_setor in d_nasabah:
            hasil = int(d_nasabah[2]) + nominal_setor
            d_nasabah[2] = str(hasil)
            print("Setoran tunai sebesar", nominal_setor,
                  "ke rekening", rek_setor, "berhasil. \n")
        f_nasabah.append(d_nasabah)
    a_file.close()

    cek = 0
    for i in range(len(f_nasabah)):
        if rek_setor in f_nasabah[i][0]:
            cek = 1
    if cek == 0:
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal. \n")
        menu()
    return f_nasabah


def upload(l):
    if l != None:
        a_file = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt', 'w+')
        for i in range(len(l)):
            a_file.write(l[i][0] + ', ' + l[i][1] + ', ' + l[i][2] + '\n')
        a_file.close()
    menu()


def tarik_tunai():  # Mufti
    print("\n*** TARIK TUNAI ***")
    rek_tarik = input("Masukkan nomor rekening: ").upper()
    nominal_tarik = eval(input("Masukkan nominal yang akan ditarik: "))

    a_file = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt')
    f_nasabah = []
    for data in a_file:
        d_nasabah = data.strip().split(', ')
        if rek_tarik in d_nasabah:
            if int(d_nasabah[2]) > nominal_tarik:
                hasil = int(d_nasabah[2]) - nominal_tarik
                d_nasabah[2] = str(hasil)
                print("Tarik tunai sebesar", nominal_tarik,
                      "dari rekening", rek_tarik, "berhasil. \n")
            else:
                print("Saldo tidak mencukupi. Tarik tunai gagal.")
        f_nasabah.append(d_nasabah)
    a_file.close()

    cek = 0
    for i in range(len(f_nasabah)):
        if rek_tarik in f_nasabah[i][0]:
            cek = 1
    if cek == 0:
        print("Nomor rekening tidak terdaftar. Tarik tunai gagal. \n")
    return f_nasabah


def transfer():  # Aldi
    print("\n*** TRANSFER ***")
    rek_sumber = input("Masukkan nomor rekening sumber: ").upper()
    rek_tujuan = input("Masukkan nomor rekening tujuan: ").upper()
    nominal_tf = eval(input("Masukkan nominal yang akan ditransfer: "))

    a_file = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt')
    f_nasabah = []
    for data in a_file:
        d_nasabah = data.strip().split(', ')

        # mengurangi saldo rekening sumber
        if rek_sumber in d_nasabah:
            if int(d_nasabah[2]) > nominal_tf:
                hasil = int(d_nasabah[2]) - nominal_tf
                d_nasabah[2] = str(hasil)
            else:
                print("Saldo tidak mencukupi. Transfer tunai gagal.")

        # menambahkan saldo rekening tujuan
        if rek_tujuan in d_nasabah:
            result = int(d_nasabah[2]) + nominal_tf
            d_nasabah[2] = str(result)
        f_nasabah.append(d_nasabah)
    a_file.close()

    # memeriksa keberadaan nomor rekening sumber dan tujuan
    cek_sumber = 0
    cek_tujuan = 0
    gagal_transfer = False
    for i in range(len(f_nasabah)):
        if rek_sumber in f_nasabah[i][0]:
            cek_sumber = 1
        if rek_tujuan in f_nasabah[i][0]:
            cek_tujuan = 1

    if (cek_sumber == 0) and (cek_tujuan == 0):
        print("Nomor rekening sumber dan tujuan tidak terdaftar. Transfer tunai gagal. \n")
        gagal_transfer = True
    elif cek_sumber == 0:
        print("Nomor rekening sumber tidak terdaftar. Transfer tunai gagal. \n")
        gagal_transfer = True
    elif cek_tujuan == 0:
        print("Nomor rekening tujuan tidak terdaftar. Transfer tunai gagal. \n")
        gagal_transfer = True

    if gagal_transfer == False:
        print("Transfer tunai sebesar", nominal_tf,
              "dari rekening", rek_sumber, "ke rekening ", rek_tujuan, "berhasil. \n")

        no_tf = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))

        f_transfer = open(
            'D:/_STTNF/Tugas/Code/DDP/Tugas-2/transfer.txt', 'a+')
        f_transfer.write(no_tf + ', ' + rek_sumber + ', ' +
                         rek_tujuan + ', ' + str(nominal_tf) + '\n')
        f_transfer.close()

        return f_nasabah


def daftar_transfer():  # Fikri
    print("\n*** LIHAT DAFTAR TRANSFER ***")
    norek = input("Masukkan nomor rekening sumber transfer: ").upper()

    f_nasabah = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt')
    kode = 0
    for nasabah in f_nasabah:
        if norek in nasabah:
            kode = 1
    f_nasabah.close()

    if kode == 0:
        print("Nomor rekening sumber tidak terdaftar. \n")
        menu()
    elif kode == 1:
        f_transfer = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/transfer.txt')
        cetak_teks = True
        kosong = True
        for transfer in f_transfer:
            list_tf = transfer.strip().split(', ')
            if norek in list_tf[1]:
                if cetak_teks == True:
                    print('Daftar transfer dari rekening', norek, ': ')
                    cetak_teks = False
                    kosong = False
                print(list_tf[0], list_tf[1], list_tf[2], list_tf[3])
        if kosong == True:
            if cetak_teks == True:
                print('Tidak ada data yang ditampilkan.')
                cetak_teks = False
        print('\n')
        f_transfer.close()
        menu()


def keluar():
    print("Terimasih atas kunjungan Anda...")


def input_menu():
    menu = input("Masukkan menu pilihan Anda: ")
    pilihan(menu)


def pilihan(menu):
    if menu == '1':  # Mutia
        return buka_rekening()
    elif menu == '2':  # Wahyu
        return upload(setoran_tunai())
    elif menu == '3':  # Mufti
        return upload(tarik_tunai())
    elif menu == '4':  # Aldi
        return upload(transfer())
    elif menu == '5':  # Fikri
        return daftar_transfer()
    elif menu == '6':
        return keluar()
    else:
        print("Pilihan Anda salah. Ulangi.")
        input_menu()


def menu():
    print("MENU :")
    print("[1] Buka rekening")
    print("[2] Setoran tunai")
    print("[3] Tarik tunai")
    print("[4] Transfer")
    print("[5] Lihat daftar transfer")
    print("[6] Keluar")
    input_menu()


print("***** SELAMAT DATANG DI NF BANK *****")
menu()
