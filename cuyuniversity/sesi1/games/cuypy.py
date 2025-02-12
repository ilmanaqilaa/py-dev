import random

while True:

    goa_form = "|_|"
    empty_goa = [goa_form] * 4

    marmut_position = random.randint(1, 4)
    
    goa = empty_goa.copy()
    goa[marmut_position - 1] = "[0_0]"

    empty_goa = " ".join(empty_goa)
    goa = " ".join(goa)
    print(f"Coba perhatikan goa di bawah ini \n\n{empty_goa}\n")

    pilihan_user = int(input("Menurutmu di goa nomor berapa marmut berada? [1 / 2 / 3 / 4]: "))

    while pilihan_user not in [1, 2, 3, 4]:
        pilihan_user = int(input("Angkamu tidak sesuai! Ayo pilih angka yang benar!!! [1 / 2 / 3 / 4]: "))
        
    print()

    if pilihan_user == marmut_position:
        print(goa)
        print(f"Selamat kamu benar! Posisi marmut berada di goa nomor {marmut_position} dan pilihanmu adalah goa nomor {pilihan_user}")
    else:
        print(goa)
        print(f"Kamu salah!!! Posisi marmut bukan berada di goa {pilihan_user}, tapi berada di goa {marmut_position}")
        
    play_again = input("\n\n Apakah kamu ingin melanjutkan gamenya? [y / n]")
    if play_again == "n":
        break

print("\n\n Program Selesai")