from app.interface.add_book_menu import add_book_menu
from app.interface.edit_book_menu import edit_book_menu, choose_book_to_edit_menu
from app.interface.open_menu import open_menu
from app.services.add_book import add_book
from app.services.edit_book import choose_book_to_edit
from app.services.print_books import print_books


def main() -> None:
    open_menu()
    command = input('\nВведите команду: ')
    process_command(command)
    while command != '0':
        if command != '1' and command != '2' and command != '3':
            print('\nВы ввели отсутствующую команду')
            print('\nПопробуйте снова')
        open_menu()
        command = input('\nВведите команду: ')
        process_command(command)


def process_command(command: str) -> None:
    if command == '0':
        print('\nРабота завершена')
    elif command == '1':
        add_book_menu()
        add_book()
    elif command == '2':
        print_books()
    elif command == '3':
        choose_book_to_edit_menu()
        choose_book_to_edit()
        edit_book_menu()

