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


def open_menu() -> None:
    print('\n1. Добавить книгу')
    print('0. Завершить работу')


def process_command(command: str) -> None:
    if command == '0':
        print('\nРабота завершена')
    elif command == '1':
        print('\nКоманда не реализована')


if __name__ == '__main__':
    main()
