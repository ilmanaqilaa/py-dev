from libs import welcome_message, exit_program
from games import cuypy
from tools import warung_mini

def options():
    user_option = int(input(f"Menu program: \n1. Games Cuypy\n2. Warung Mini\n\nsilahkan pilih: "))
    return user_option

def main():
    welcome_message()

    user_option = options()
    
    if user_option == 1:
        cuypy.start_cuypy()
    elif user_option == 2:
        warung_mini.start_warung()
    
    exit_program()

if __name__ == '__main__':
    main()