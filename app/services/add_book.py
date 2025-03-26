from app.models.book import Book


def add_book() -> None:
    name = input('\nИмя: ')
    author = input('\nАвтор: ')
    book_list.append(Book(
        name=name,
        author=author,
    ))


book_list: list[Book] = []
