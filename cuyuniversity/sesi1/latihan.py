import random
from libs import welcome_message

welcome_message("Wellcome to Minigame")

print()

nama_user = input("Siapa namamu: ")

while nama_user == "":
    nama_user = input("Jangan kosong dongg, Ayo siapa namamu?")



while True:

    goa_form = "|_|"
    empty_goa = [goa_form] * 4


    marmut_position = random.randint(1, 4)
    
    goa = empty_goa.copy()
    goa[marmut_position - 1] = "[0_0]"

    empty_goa = " ".join(empty_goa)
    goa = " ".join(goa)
    print(f"""
    Halo {nama_user}! Coba perhatikan goa di bawah ini
    {empty_goa}
    """)

    pilihan_user = int(input("Menurutmu di goa nomor berapa marmut berada? [1 / 2 / 3 / 4]: "))

    while pilihan_user not in [1, 2, 3, 4]:
        pilihan_user = int(input("Angkamu tidak sesuai! Ayo pilih angka yang benar!!! [1 / 2 / 3 / 4]: "))
        
    print()

    konfirmasi = input("Apakah kamu sudah yakin memilih nomor goa tersebut? [Y / N] ")

    print()

    if konfirmasi in ["Y", "y"]:
        print(f"Pilihanmu adalah goa bernomor {pilihan_user}")
        print()
    elif konfirmasi in ["N", "n"]:
        pilihan_user = int(input("Menurutmu di goa nomor berapa marmut berada? [1 / 2 / 3 / 4]: "))
        print(f"Pilihanmu adalah goa bernomor {pilihan_user}")
    else:
        input("Kamu memasukan konfirmasi yang tidak valid. Ulangi program!!!")
        exit()

    if pilihan_user == marmut_position:
        print(goa)
        print(f"Selamat {nama_user} kamu benar! Posisi marmut berada di goa nomor {marmut_position} dan pilihanmu adalah goa nomor {pilihan_user}")
    else:
        print(goa)
        print(f"Kamu salah!!! Posisi marmut bukan berada di goa {pilihan_user}, tapi berada di goa {marmut_position}")
        
    play_again = input("\n\n Apakah kamu ingin melanjutkan gamenya? [y / n]")
    if play_again == "n":
        break

print("\n\n Program Selesai")
        