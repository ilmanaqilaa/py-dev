import random

welcome_massage  = "SELAMAT DATANG DI MINIGAME"
marmut_position = random.randint(1, 4)

print("********************************")
print(f"** {welcome_massage} **")
print("********************************")

nama_user = input("Siapa namamu: ")

print(f"""
Halo {nama_user}! Coba perhatikan goa di bawah ini

|_| |_| |_| |_|     
""")

pilihan_user = int(input("Menurutmu di goa nomor berapa marmut berada? [1 / 2 / 3 / 4]: "))

konfirmasi = input("Apakah kamu sudah yakin memilih nomor goa tersebut? [Y / N]")

if konfirmasi in ["Y", "y"]:
    print(f"Pilihanmu adalah goa bernomor {pilihan_user}")
elif konfirmasi in ["N", "n"]:
    pilihan_user = int(input("Menurutmu di goa nomor berapa marmut berada? [1 / 2 / 3 / 4]: "))
    print(f"Pilihanmu adalah goa bernomor {pilihan_user}")
else:
    input("Kamu memasukan konfirmasi yang tidak valid. Ulangi program!!!")
    exit()

if pilihan_user == marmut_position:
    print(f"Selamat {nama_user} kamu benar! Posisi marmut berada di goa nomor {marmut_position} dan pilihanmu adalah goa nomor {pilihan_user}")
else:
    print(f"Kamu salah!!! Posisi marmut bukan berada di goa {pilihan_user}, tapi berada di goa {marmut_position}")