diction = {
    'key1' : 'value1',
    'num1' : 19,
    'nama' : 'fikri',
}

def tampildictionary1(diction1):
    out = '' 
    i = 1 
    for key,value in diction1.items():
        out += ('{}.    {}\t{}\n'.format(i,key,value))
        i += 1
    print (out)

def tampildictionary():
    tampildictionary1(diction)

def inputData():
    count = input('Masukan banyak yang ingin anda inputkan? ') 
    for i in range(int(count)):
        typedata = input('Masukkan tipe data =\n 1. str \n 2. int\n')
        if typedata == '1' :
            key = input('Masukkan key dictionary baru anda=  ')
            value = input('Masukkan value baru anda=  ')
            diction.update({key : value})
        elif typedata == '2' :
            key = input('Masukkan key baru anda= ')
            value = int(input('Masukkan value baru anda=  '))
            diction.update({key : value})
    tampildictionary()

def search():
    search = input('Masukkan key yang ingin anda cari? ')
    out = {}
    for key,value in diction.items():
        if search in key:
            out.update({key : value})
    tampildictionary1(out)


def exitdictionary():
    exit()

backToMenu = 'y'
while(backToMenu == 'y'):
    pilihMenu = input('\n----MENU UTAMA---\n1. Lihat dictionary \n2. Isi dictionary \n3. Search dictionary\n4. Keluar\nPilih salah satu : ') #1
    index = int(pilihMenu)-1 
    menu = [tampildictionary , inputData, search, exitdictionary]
    menu[index]()
    backToMenu = input('Kembali Ke Menu Utama? (y/n)')

        


        
