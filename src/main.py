import mylib


#database karyawan
employees = [
    [0, 'Agus', '111', 50, 60000000, 'Baik'],
    [1, 'Bambang', '112', 30, 50000000, 'Cukup'],
    [2, 'Seli', '113', 49, 20000000, 'Kurang'],
    [3, 'Zefir', '114', 56, 90000000, 'Panutan']
]


#main function dari program
def main():
    print(
        'Selamat datang di arsip perusahaan x, silahkan tekan tombol menu yang mau diakses.'
    )
    menu = '''
            List Menu:

1. Menampilkan data karyawan yang ada di perusahaan.
2. Menambahkan data karyawan di perusahaan
3. Memperbaharui data karyawan di perusahaan
4. menghapus data karyawan di perusahaan
5. exit
'''

    while True:
        #menampilkan data karyawan
        print(menu)

        #meminta input user
        choice = input('Silahkan masukan angka sesuai menu: ')

        #menampilkan menu choice
        if choice == '1':
            mylib.Menu1(employees)
        elif choice == '2':
            mylib.Menu2(employees)
        elif choice == '3':
            mylib.Menu3(employees)
        elif choice == '4':
            mylib.Menu4(employees)
        elif choice == '5':
            print('Terima kasih atas penggunaan program ini, have a nice day')
            break    
        else:
            print('Input anda salah, silahkan masukan angka lagi yang sesuai dengan menuf2f323')
main()

