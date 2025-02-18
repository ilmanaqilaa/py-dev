import main
from services import db

def add_barang():
    kode_barang = input('Kode barang: ')
    nama_barang = input('Nama barang: ')
    harga_barang = int(input('Harga barang: '))
    stok_barang = int(input('Stok barang: '))

    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def check_barang():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
Kode Barang: {kode_barang}
Nama Barang: {nama_barang} | Rp. {harga_barang}
Stok Barang: {stok_barang}
              ''')

def start_warung():
    while True:
        menu = int(input('Menu:\n1. Tambah Barang\n2. Cek barang\n3. Kembali\n\nSilahkan pilih menu: '))

        if menu == 1:
            add_barang()
        elif menu == 2:
            check_barang()
        elif menu == 3:
            main.menu()
        else:
            break

if __name__ == "__main__":
    start_warung()