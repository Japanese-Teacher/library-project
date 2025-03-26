from app.services.add_book import book_list


def choose_book_to_edit() -> int:
    for book in book_list:
        print(book.index, book.name, book.author, sep=" ")
    index = int(input('Введите номер книги: ')) - 1
    return index

def edit_book(index: int) -> None:
    command = input('Введите номер параметра книги: ')
    if command == '1':
        print('\nВведите новое название: ')
        new_name = input()
        book_list[index].name = new_name
    elif command == '2':
        print('\nВведите нового автора: ')
        new_author = input()
        book_list[index].author = new_author
    else:
        print('\nТакого параметра не существует')