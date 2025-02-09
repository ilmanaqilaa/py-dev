import random

welcome_massage = "Welcome to minigame"
marmut_position = random.randint(1, 4)

print("***************************")
print(f"*** {welcome_massage} ***")
print("***************************")

nama_user = input("Siapa namamu: ")

print(f"""Selamat datang {nama_user}! di minigame
      
Coba perhatikan goa di bawah ini!!!
|_| |_| |_| |_|
""")

while True:
    try:
        pilihan_user = int(input("Menurutmu di goa berapa posisi marmut berada? [1 / 2 / 3 / 4]: "))
        if pilihan_user not in [1, 2, 3, 4]:
            print("Masukkan nomor goa yang valid [1 / 2 / 3 / 4]!")
            continue
    except ValueError:
        print("Harap masukkan angka yang valid!")
        continue

    while True:
        konfirmasi = input("Apakah kamu yakin dengan nomor pilihanmu? [Y / N]: ").strip().upper()
        if konfirmasi in ["Y", "N"]:
            break
        print("Input kamu tidak valid, masukkan jawaban yang benar! [Y / N]")

    if konfirmasi == "N":
        continue

    print(f"Pilihan kamu adalah goa bernomor {pilihan_user}")

    if pilihan_user == marmut_position:
        input(f"KAMU BENAR!!! MARMUT BERADA DI GOA {marmut_position} dan pilihanmu adalah {pilihan_user}")
        break
    else:
        input(f"KAMU SALAH!!! POSISI MARMUT BERADA DI {marmut_position}. Ayo coba lagi!")
    