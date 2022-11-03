'''
SIMULASI PROGRAM PEMBUAT KARIKATUR BEREKSTENSI HTML by python
created by Muhammad Yusuf 2021

'''


import ascii_magic
import time
import os
os.system('cls')


print('''
SELAMAT DATANG DI PROGRAM PEMBUAT KARIKATUR
▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
''')


hs = os.listdir('projek/karikatur ascii/img')

gambar = input('Masukkan nama gambar: ')+'.'
ekstensi = input('Masukkan ekstensi gambar (jpg/jpeg/png/dll) :')
file = ['projek/karikatur ascii/img/',gambar,ekstensi]
file = ''.join(file)
print('\nTunggu sebentar')
time.sleep(1)

if gambar+ekstensi not in hs:
    print('Gambar tidak tersedia..')

else:
    print('Berhasil membuat karikatur...\n')
    fileName =  'projek/karikatur ascii/output/' + input('Masukkan nama hasil file: ')+'.html'
    print('Menyimpan file...')
    time.sleep(1)
    print('File berhasil di simpan di folder output..')
    try :
        my_art = ascii_magic.from_image_file(    
        file,
        columns=100,
        width_ratio=2,
        mode=ascii_magic.Modes.HTML)
        ascii_magic.to_html_file(fileName, my_art)

        my_art2 = ascii_magic.from_image_file('projek/karikatur ascii/img/thank.png')
        ascii_magic.to_terminal(my_art2)

    except Exception as e:
        print('Error', e)
