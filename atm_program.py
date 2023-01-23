import random 
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukan pin anda : '))
    trial = 0

    while (not id == int(atm.showPin())) and trial < 3:
        id = int(input('Pin salah Masukan pin Anda lagi :'))
        trial += 1

        if trial == 3:
            print('Anda telah melakukan habis untuk loginya silahkan masukan kembali datanya')
            exit()

    while True:
        print('Selamat datang di ATM, silahkan masukkan pilih menu utama dibawah ini')
        print('1. Cek Saldo')
        print('2. Debet')
        print('3. Simpan')
        print('4. Ganti Pin')
        print('5. Keluar')
        pilihMenu = int(input('Pilih menu diatas 1-5 :'))

        if pilihMenu == 1:
           print('Jumlah Saldo Anda Saat Ini : ' + str(atm.showBalance()))
        elif pilihMenu == 2: 
           input_nominal = float(input('Masukkan nominal yang ingin di debet : '))
           checking_confirm = str(input('Yakinkah ada ingin mendebet : (y/n)'));

           if checking_confirm == 'y':
              print("Saldo anda saat ini adalah : "+ str(atm.showBalance()))
           else :
              break

           if input_nominal < atm.showBalance():
              atm.debetCust(input_nominal)
              print('Transaki anda telah berhasil')
              print('sisa saldo anda : '+ str(atm.showBalance()))
           else :
              print('Maaf saldo anda melebihi batas')

        elif pilihMenu == 3:
           input_nominal = float(input('Masukkan nominal yang ingin di debet : '))
           checking_confirm = str(input('Yakinkah ada ingin menyimpan : (y/n)'));
           
           if checking_confirm == 'y':
              atm.simpanCust(input_nominal)
              print('Saldo anda berhasil disimpan')
              print('Saldo anda saat ini yaitu : '+ str(atm.showBalance()))
           else :
              break

        elif pilihMenu == 4: 
            input_new_pin = int(input('Masukkan pin yang baru :'))
            checking_status = str(input('Apakah anda ingin mengganti password anda (y/n) ? '))

            if checking_status == 'y':
               if not input_new_pin == atm.showPin():
                  print('Password anda berhasil berubah')
               else: 
                  print('Password sama seperti sebelumnya, Mohon masukkan yang lain!') 
            else :
                print('Anda mengagalkan pnergantian password')
                break

        elif pilihMenu == 5:
            print('=====Inilah resi anda saat ini============')
            print('No Record : ' + str(random.randint(100000, 1000000)))
            print('Tanggal   : ' + str(datetime.datetime.now()))
            print('Saldo Akhir : '+ str(atm.showBalance()))
            print('Terima Kasih')
            exit();
        else:
            print('Maaf, menu yang anda pilih tidak ada!')