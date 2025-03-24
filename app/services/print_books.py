from app.services.add_book import book_list


def print_books() -> None:
    if not book_list:
        print('Книг нет')
    print(*book_list)
