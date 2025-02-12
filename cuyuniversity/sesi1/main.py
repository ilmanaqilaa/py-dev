from libs import welcome_message, exit_program
from games import cuypy
from tools import warung_mini

def menu():
    user_option = int(input(f"Menu program: \n1. Games Cuypy\n2. Warung Mini\n\nsilahkan pilih: "))
    
    if user_option == 1:
        cuypy.start_cuypy()
    elif user_option == 2:
        warung_mini.start_warung()
    else:
        print("Pilih lah program yang tersedia")

def main():
    welcome_message()
    menu()
    exit_program()

if __name__ == '__main__':
    main()