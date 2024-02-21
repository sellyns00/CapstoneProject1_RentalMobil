from colorama import Fore,Style
#membuat teks jadi berwarna (Fore.WARNA + 'teks' + Style.RESET_ALL)

listMobil = [
    {
        'Merk': 'Toyota Avanza',
        'Tahun': '2009',
        'Jenis': 'SPV',
        'Status': 'Ada',
        'harga': 200000
    },
    {
        'Merk': 'Honda Brio',
        'Tahun': '2009',
        'Jenis': 'SPV',
        'Status': 'Kosong',
        'harga': 180000
    },
    {
        'Merk': 'Toyota Rush',
        'Tahun': '2007',
        'Jenis': 'SPV',
        'Status': 'Ada',
        'harga': 250000    }
]

cart = []

def menu():
    print(f'''
        Selamat Datang di Rental Mobil ESSA

        List Menu :
        1. Menampilkan Daftar Mobil
        2. Menambah Mobil
        3. Update Mobil
        4. Menghapus Mobil
        5. Sewa Mobil
        6. Exit Program
        ''')
    
def daftarMobil():
    print('Daftar Mobil\n')
    print('Index\t| Merk  \t\t| Tahun\t| Jenis\t| Status\t| Harga \t')
    for i in range(len(listMobil)) :
        print('{}\t| {}\t\t| {}\t| {}\t| {}    \t| {}\t'.format(i,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['Status'],listMobil[i]['harga']))

def tambahMobil():
    merkMobil = input('Masukkan Merk Mobil : ')
    tahunMobil = int(input('Masukkan Tahun Mobil : '))       
    jenisMobil = input('Masukkan Jenis Mobil : ')
    statusMobil = input('Masukkan Status Mobil : ')
    hargaMobil = int(input('Masukkan Harga Mobil : '))
    listMobil.append({
        'Merk': merkMobil,
        'Tahun': tahunMobil,
        'Jenis': jenisMobil,
        'Status': statusMobil,
        'harga' : hargaMobil
    })
    daftarMobil()
    
def hapusMobil():
    daftarMobil()
    indexMobil = int(input('Masukkan index Mobil yang ingin dihapus : '))
    del listMobil[indexMobil]
    daftarMobil()
    
def update(): 
    daftarMobil()
    while True:
        cari_index = int(input('Silahkan masukkan index data mobil rental yang ingin diupdate: '))
        if cari_index in range(len(listMobil)):
            harga_baru = int(input('Masukkan harga baru sewa: '))
            cek = str(input('Apakah Anda yakin ingin update data ini? (Y/N) ')).capitalize()
            if cek == 'Y':
                listMobil[cari_index]['harga'] = harga_baru
            daftarMobil()
        else:
            print(Fore.RED+ 'Data Tidak Ada'+ Style.RESET_ALL)
            daftarMobil()
            break    
    
def sewaMobil():
    daftarMobil()
    print('SEWA MOBIL\n')
    nama = str(input('Masukkan Nama Anda: '))
    while True :
        i = int(input('Masukkan index Mobil yang ingin disewa : '))
        if i in range(len(listMobil)) and listMobil[i]['Status'] == 'Ada':
            sewa = int(input('Berapa lama Anda ingin menyewa mobil? ... Hari :  '))
            total = sewa * listMobil[i]['harga']
            status = 'Berhasil disewa oleh' +' '+ nama
            listMobil[i]['Status'] = status
            cart.append([nama,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['harga'],sewa,total,status])
        else :
            print(Fore.RED+ 'Maaf Mobil Tidak Tersedia'+ Style.RESET_ALL)   
            menu()
            break        
        print('Isi Cart Sewa\n')
        print('Nama Customer\t| Merk\t\t| Tahun\t | Jenis | Harga\t| Lama Sewa (hari)\t | Total\t | Status')
        for item in cart :
            print(f'{item[0]}\t\t| {item[1]}\t| {item[2]}\t | {item[3]}\t | {item[4]}\t| {item[5]}\t\t\t | {item[6]}\t | {item[7]}\t')
        checker = input('Mau sewa yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Total Yang Harus Dibayar = {}'.format(total))
    jmlUang = int(input('Masukkan jumlah uang = '))
    if(jmlUang > total) :
        kembali = jmlUang - total
        print('Terima kasih \n\nUang kembali anda = {}'.format(kembali))
        cart.clear()

    elif(jmlUang == total) :
        print('Terima kasih')
        cart.clear()
        exit()
    else :
        kekurangan = total - jmlUang
        print(Fore.RED+ 'Uang Anda Kurang Sebesar {}'.format(kekurangan)+ Style.RESET_ALL)
        
while True :
    pilihanMenu = input('''
        Selamat Datang di Rental Mobil ESSA

        List Menu :
        1. Menampilkan Daftar Mobil
        2. Menambah Mobil
        3. Update Mobil
        4. Menghapus Mobil
        5. Sewa Mobil
        6. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        daftarMobil()
    elif(pilihanMenu == '2') :
        tambahMobil()
    elif(pilihanMenu == '3') :
        update()
    elif(pilihanMenu == '4') :
        hapusMobil()
    elif(pilihanMenu == '5') :
        sewaMobil() 
    elif(pilihanMenu == '6') :
        exit()       
    #     print('Daftar Mobil\n')
    #     print('Index\t| Merk  \t\t| Tahun\t| Jenis\t| Status\t| Harga \t')
    #     for i in range(len(listMobil)) :
    #         print('{}\t| {}\t\t| {}\t| {}\t| {}    \t| {}\t'.format(i,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['Status'],listMobil[i]['harga']))
    #     indexMobil = int(input('Masukkan index Mobil yang ingin dihapus : '))
    #     del listMobil[indexMobil]
    #     print('Daftar Mobil\n')
    #     print('Index\t| Merk  \t\t| Tahun\t| Jenis\t| Status\t| Harga \t')
    #     for i in range(len(listMobil)) :
    #         print('{}\t| {}\t\t| {}\t| {}\t| {}    \t| {}\t'.format(i,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['Status'],listMobil[i]['harga']))

    # elif(pilihanMenu == '5') :

    #     print('Daftar Mobil\n')
    #     print('Index\t| Merk  \t\t| Tahun\t| Jenis\t| Status\t| Harga \t')
    #     for i in range(len(listMobil)) :
    #         print('{}\t| {}\t\t| {}\t| {}\t| {}    \t| {}\t'.format(i,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['Status'],listMobil[i]['harga']))
    #     nama=str(input('Masukkan Nama Anda: '))
    #     while True :
    #         i = int(input('Masukkan index Mobil yang ingin disewa : '))
    #         if i in range(len(listMobil)) and listMobil[i]['Status'] == 'Ada':
    #             sewa = int(input('Berapa lama Anda ingin menyewa mobil? ... Hari :  '))
    #             total = sewa * listMobil[i]['harga']
    #             status = 'Berhasil disewa oleh' +' '+ nama
    #             listMobil[i]['Status'] = status
    #             cart.append([nama,listMobil[i]['Merk'],listMobil[i]['Tahun'],listMobil[i]['Jenis'],listMobil[i]['harga'],sewa,total,status])
            
    #         else :
    #             print ('Maaf Mobil yang Anda pilih tidak tersedia\n')    
                
    #         print('Isi Cart Sewa\n')
    #         print('Nama Customer\t| Merk\t\t| Tahun\t | Jenis | Harga\t| Lama Sewa (hari)\t | Total\t | Status')
    #         for item in cart :
    #             print(f'{item[0]}\t\t| {item[1]}\t| {item[2]}\t | {item[3]}\t | {item[4]}\t| {item[5]}\t\t\t | {item[6]}\t | {item[7]}\t')
    #         checker = input('Mau sewa yang lain? (ya/tidak) = ')
    #         if(checker == 'tidak') :
    #             break

    #     while True :
    #         print('Total Yang Harus Dibayar = {}'.format(total))
    #         jmlUang = int(input('Masukkan jumlah uang = '))
    #         if(jmlUang > total) :
    #             kembali = jmlUang - total
    #             print('Terima kasih \n\nUang kembali anda = {}'.format(kembali))
    #             cart.clear()
    #             break
    #         elif(jmlUang == total) :
    #             print('Terima kasih')
    #             cart.clear()
    #             exit()
    #         else :
    #             kekurangan = total - jmlUang
    #             print('Uang anda kurang sebesar {}'.format(kekurangan))
    #             exit()
                
    # elif(pilihanMenu == '6') :
    #     break
    #     exit()
    
