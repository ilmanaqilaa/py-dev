from libs import welcome_message, exit_program
from games import cuypy

def main():
    welcome_message()
    cuypy.start_cuypy()
    exit_program()

if __name__ == '__main__':
    main()