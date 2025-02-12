import main

def start_warung():
    while True:
        print("Ini adalah aplikasi warung mini")
        back_to_menu = input("Kembali ke menu utama? [y/n]: ")

        if back_to_menu == "y":
            main.main()

if __name__ == "__main__":
    start_warung()