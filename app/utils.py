from app.interface.open_menu import open_menu


def main() -> None:
    open_menu()
    command = input('\nВведите команду: ')
    process_command(command)
    while command != '0':
        if command != '1':
            print('\nВы ввели отсутствующую команду')
        print('\nПопробуйте снова')
        open_menu()
        command = input('\nВведите команду: ')
        process_command(command)


def process_command(command: str) -> None:
    if command == '0':
        print('\nРабота завершена')
    elif command == '1':
        print('\nКоманда не реализована')