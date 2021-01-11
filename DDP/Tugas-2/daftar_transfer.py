def daftar_transfer():
    print("\n*** LIHAT DAFTAR TRANSFER ***")
    norek = input("Masukkan nomor rekening sumber transfer: ")

    f_nasabah = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/nasabah.txt')
    kode = 0
    for nasabah in f_nasabah:
        if norek in nasabah:
            kode = 1
    f_nasabah.close()

    if kode == 0:
        print("Nomor rekening sumber tidak terdaftar. \n")
    elif kode == 1:
        f_transfer = open('D:/_STTNF/Tugas/Code/DDP/Tugas-2/transfer.txt')
        list_final = []
        for transfer in f_transfer:
            list_tf = transfer.strip().split(', ')
            list_final.append(list_tf)

        if norek in list_final[1]:

        f_transfer.close()


daftar_transfer()
