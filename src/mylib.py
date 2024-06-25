from tabulate import tabulate

def stringValidation(title):

    while True:
        text= input(title)
        if text.isalpha() == True:
            break
        else:
            print('Silahkan inputkan hanya teks')
    return text.capitalize()

def integerValidation(title, minval = 0, maxval = 100):
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print(f'Silahkan masukan angka diantara {minval} dan {maxval}')
        except:
            print('Silahkan masukan angka')
    return num

       
#####BAGIAN MENU 1

def Menu1(database):
    while True:    
        print(f'''
                1. Data karyawan
                2. Mencari data berdasarkan nomor induk
                3. kembali ke menu utama
                ''')
        subChoice = input('Silahkan masukan pilihan angka sesuai menu: ')
            
        #menampilkan sub menu opsi 1
        #menampilkan data karyawan
        if subChoice == '1':
            showFunc(database)
        #menyortir karyawan berdasarkan Nomor induk
        elif subChoice == '2':
            showPerson(database)
        elif subChoice == '3':
            break
        else:
            print('input anda tidak valid, silahkan coba lagi')



#fungsi menampilkan data karyawan secara keseluruhan 
def showFunc(database, Header =['No.','Nama','No. Induk','Umur','Gaji','Performa']):
    if  database:
        print(tabulate(database, headers= Header, tablefmt= 'grid'))
    else:
        print('Data kosong, silahkan tambahkan data.')


#fungsi gaji karyawan menu1
def showPerson(database):
    while True:
            employee_id = input('Silahkan masukan nomor induk karyawan: ')
            found = False

            # Memeriksa nomor induk karyawan
            for employee in database:
                if employee_id == employee[2]:
                    output = tabulate([employee], headers= ['No.','Nama','No. Induk','Umur','Gaji','Performa'], tablefmt= 'grid')                    
                    print(f'Data karyawan:\n{output}')
                    found = True
                    break

            if not found:
                print('Data yang dicari tidak ada')

            search_again = input('Apakah Anda ingin mencari lagi?: ').lower()
            if search_again in ['tidak', 't', 'n']:
                break

#####BAGIAN MENU 2

def Menu2(database):
    while True:    
        print(f'''
                1. Menambahkan data karyawan
                2. kembali ke menu utama
                ''')
        subChoice = input('Silahkan masukan pilihan angka sesuai menu: ')
            
        if subChoice == '1':
            addEmplo(database)
        elif subChoice == '2':
            break           
        else:
            print('input anda tidak valid, silahkan coba lagi')

def addEmplo(database):
    while True:
        while True:
            name = stringValidation(title='Masukan nama pegawai:').lower()
            # Memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[1].lower() == name:
                    dupeFound = True
                    break
            if dupeFound:
                print('Nama yang anda pakai sudah ada di pegawai lain: ')
            else:
                break

        while True:            
            nomorInduk = integerValidation(
                title = 'Masukan no. induk pegawai :',
                minval= 0,
                maxval= 1000
                )
            #memeriksa duplikat
            dupeFound = False
            lenNum = False
            for employee in database:
                if employee[2] == str(nomorInduk):
                    dupeFound = True
                    break
                if len(str(nomorInduk)) < 3:
                    lenNum = True
                    break

            if dupeFound:
                print('Nomor induk yang anda pakai sudah ada di pegawai lain: ')
            elif lenNum:
                print('Nomor induk harus 3 angka')
            else: 
                break
        while True:
            umur = integerValidation(
                title= 'Masukan umur karyawan: ',
                minval= 0
            )
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[3] == umur:
                    dupeFound = True
            
            if dupeFound:
                print('Umur yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 
        while True:
            gaji = integerValidation(
                title= 'Masukan gaji karyawan: ',
                minval = 0,
                maxval= 100000000
            )
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[4] == gaji:
                    dupeFound = True
            
            if dupeFound:
                print('Gaji yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 
        while True:
            performa= stringValidation(title= 'Masukan performa pegawai: ')
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[5] == performa:
                    dupeFound = True
            
            if dupeFound:
                print('Performa yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 

        while True:
            promptYakin = input('Apakah anda yakin untuk menyimpan data ini? (ya/tidak) ')
            if promptYakin.lower() in ['ya','yes','y']:
                database.append([len(database) + 1, name, nomorInduk, umur, gaji, performa])
                showFunc(database)
                print("Data pegawai berhasil disimpan.")
                return
            elif promptYakin.lower() == 'tidak':
                print("Data pegawai tidak disimpan.")
                return
            else:
                print("Input tidak valid. Silakan jawab dengan 'ya' atau 'tidak'.")


#####BAGIAN MENU 3

def Menu3(database):
    while True:    
        print(f'''
                1. Memperbaharui data karyawan per baris
                2. Memperbaharui data karyawan per Kolom
                3. kembali ke menu utama
                ''')
        subChoice = input('Silahkan masukan pilihan angka sesuai menu: ')
            
        if subChoice == '1':
            updateEmplo(database)
        if subChoice == '2':
            updateEmploColumns(database)
        elif subChoice == '3':
            break
        else:
            print('input anda tidak valid, silahkan coba lagi')


def updateEmplo(database):
   while True:
        #Meminta input dari user untuk nomor induk karyawan yang ingin diupdate
        nomorInduk = integerValidation(
                        title = 'Masukan no. induk pegawai :',
                        minval= 0,
                        maxval= 1000
                        )
        
        #Verifikasi apakah nomor induk karyawan ada di daftar karyawan
        employee = None
        for row, empl in enumerate(database):
            if empl[2] == str(nomorInduk):
                employee = empl
                showFunc([empl])
                break

        if not employee:
            print('Data yang anda cari tidak ada')
            break
    
        #validasi update
        valiUpdate = input('Apakah anda yakin ingin mengubah database?[yes/no]: ').lower()      
        if valiUpdate not in ['yes', 'y', 'ya']:
            print('Update dibatalkan')
            break
        
        
        while True:
            name = stringValidation(title='Masukan nama pegawai:').lower()
            # Memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[1].lower() == name:
                    dupeFound = True
                    break
            if dupeFound:
                print('Nama yang anda pakai sudah ada di pegawai lain: ')
            else:
                break

        while True:            
            nomorInduk = integerValidation(
                title = 'Masukan no. induk pegawai :',
                minval= 0,
                maxval= 1000
                )
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[2] == str(nomorInduk):
                    dupeFound = True
                    break
            if dupeFound:
                print('Nomor induk yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break
        while True:
            umur = integerValidation(
                title= 'Masukan umur karyawan: ',
                minval= 0
            )
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[2] == umur:
                    dupeFound = True
            
            if dupeFound:
                print('Umur yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 
        while True:
            gaji = integerValidation(
                title= 'Masukan gaji karyawan: ',
                minval = 0,
                maxval= 100000000
            )
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[2] == gaji:
                    dupeFound = True
            
            if dupeFound:
                print('Gaji yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 
        while True:
            performa= stringValidation(title= 'Masukan performa pegawai: ')
            #memeriksa duplikat
            dupeFound = False
            for employee in database:
                if employee[2] == performa:
                    dupeFound = True
            
            if dupeFound:
                print('Performa yang anda pakai sudah ada di pegawai lain: ')
            else: 
                break 


        #validasi update karyawan
            # Confirm the final update
        valiUpdate1 = input('Apakah Anda yakin ingin menyimpan perubahan?(yes/no): ').lower()
        if valiUpdate1 not in ['yes', 'y', 'ya']:
            print('Update dibatalkan.')
            break
        
        database[row] = [empl[0], name, str(nomorInduk), umur, gaji, performa]
        # Update the employee data
        # employee[1] = name
        # employee[2] = nomorInduk
        # employee[3] = umur
        # employee[4] = gaji
        # employee[5] = performa
        print('Data berhasil diubah!')
        
        # Show updated database
        showFunc(database)
        
        # Ask if user wants to continue updating
        if input('Apakah Anda ingin melanjutkan memperbarui data lainnya? (yes/y/ya): ').lower() not in ['yes', 'y', 'ya']:
            break

#update data per kolom
def updateEmploColumns(database):
    while True:
        #Meminta input dari user untuk nomor induk karyawan yang ingin diupdate
        #showFunc(database)
        nomorInduk = integerValidation(
                        title = 'Masukan no. induk pegawai :',
                        minval= 0,
                        maxval= 1000
                        )
        
        #Verifikasi apakah nomor induk karyawan ada di daftar karyawan
        employee = None
        for row, empl in enumerate(database):
            if empl[2] == str(nomorInduk):
                employee = empl
                showFunc([empl])
                break
        if not employee:
            print('Data yang anda cari tidak ada')
            continue
    
        #validasi update
        valiUpdate = input('Apakah anda yakin ingin mengubah database? ').lower()      
        if valiUpdate not in ['yes', 'y', 'ya']:
            print('Update dibatalkan')
            break

        #Verifikasi apakah nomor induk karyawan ada di daftar karyawan
        #update per kolom
        while True:
            print("""
                Kolom yang dapat diupdate:
                1. Nama
                2. Nomor induk
                3. Umur
                4. Gaji
                5. Performa    
            """)
            
            choice = input("Silahkan pilih dari kolom diatas ").lower()

            position = None
            if choice == '1':
                while True:
                    new_value = stringValidation(title='Masukan nama pegawai baru:')
                    dupeFound = False
                    for emp in database:
                        if emp != employee and emp[1].lower() == new_value.lower():
                            dupeFound = True
                            break
                    if dupeFound:
                        print('Nama yang Anda masukkan sudah ada untuk pegawai lain.')
                    else:
                        positon = 1
                        break

            elif choice == '2':
                while True:
                    new_value = integerValidation(
                    title = 'Masukan no. induk pegawai :',
                    minval= 0,
                    maxval= 1000
                    )
                    dupeFound = False
                    for emp in database:
                        if emp != employee and emp[1] == new_value:
                            dupeFound = True
                            break
                    if dupeFound:
                        print('Nama yang Anda masukkan sudah ada untuk pegawai lain.')
                    else:
                        positon = 2
                        break

            elif choice == '3':
                while True:
                    new_value = integerValidation(
                    title = 'Masukan umur :',
                    minval= 0,
                    maxval= 1000
                    )
                    dupeFound = False
                    for emp in database:
                        if emp != employee and emp[1] == new_value:
                            dupeFound = True
                            break
                    if dupeFound:
                        print('Nama yang Anda masukkan sudah ada untuk pegawai lain.')
                    else:
                        positon = 3
                        break

            elif choice == '4':
                while True:
                    new_value = integerValidation(
                    title = 'Masukan gaji:',
                    minval= 0,
                    maxval= 1000
                    )
                    dupeFound = False
                    for emp in database:
                        if emp != employee and emp[1] == new_value:
                            dupeFound = True
                            break
                    if dupeFound:
                        print('Nama yang Anda masukkan sudah ada untuk pegawai lain.')
                    else:
                        positon = 4
                        break

            elif choice == '5':
                while True:
                    new_value = stringValidation(title='Masukan nama pegawai baru:')
                    dupeFound = False
                    for emp in database:
                        if emp != employee and emp[1].lower() == new_value.lower():
                            dupeFound = True
                            break
                    if dupeFound:
                        print('Nama yang Anda masukkan sudah ada untuk pegawai lain.')
                    else:
                        positon = 5
                        break
                
            # elif choice == '6':
            #     konfir = input('Apakah anda yakin ingin keluar dari menu?').lower()
            #     print(konfir)
            #     if konfir == 'y' or konfir == 'ya' or konfir == 'yes':
            #         break
            #     else:
            #         print('Anda tetap di program')
            #         continue
            
            else:
                print('Pilihan tidak valid, silahkan coba lagi')

            break
        
        confirm = input('Apakah anda yakin ingin mengubah database?(yes/no) ').lower()                
        if confirm not in ['yes', 'y', 'ya']:
            print('Update dibatalkan')
        else:
            database[row][positon] = new_value
            print('Data berhasil diubah!')

        break
                

#bagian menu 4
def Menu4(database):
     while True:    
        print(f'''
                1. Menghapus data karyawan
                2. kembali ke menu utama
                ''')
        subChoice = input('Silahkan masukan pilihan angka sesuai menu: ')
            
        #menampilkan sub menu opsi 1
        #menampilkan data karyawan
        if subChoice == '1':
            delPlo(database)
        #menyortir karyawan berdasarkan Nomor induk
        elif subChoice == '2':
            break
        else:
            print('input anda tidak valid, silahkan coba lagi')


def delPlo(database):    
    while True:
        showFunc(database)
        nomorInduk = integerValidation(
            title='Masukan no. induk pegawai :',
            minval=0,
            maxval=1000000000
        )

        employee = None
        for empl in database:
            if empl[2] == str(nomorInduk):
                employee = empl
                break
        if not employee:
            print('Data yang anda cari tidak ada')
            continue


        nomorInduk1 = str(nomorInduk)
        if nomorInduk1  in [employee[2] for employee in database]:
            for employee in database[:]:
                if employee[2] == nomorInduk1 :
                    x = input('Apakah anda yakin ingin menghapus data karyawan?')
                    if x not in ['y','yes','ya']:
                        print('Penghapusan data dibatalkan')
                        
                    else:
                        print('Data berhasil dihapus!')   
                        database.remove(employee)
                    showFunc(database)
                    break
            break
        else:
            print('Input anda invalid. Silahkan coba lagi.')
