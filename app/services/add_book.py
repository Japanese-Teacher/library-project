from app.models.book import Book


def add_book() -> None:
    index = len(book_list) + 1
    name = input('\nИмя: ')
    author = input('\nАвтор: ')
    book_list.append(Book(
        index=index,
        name=name,
        author=author,
    ))


book_list: list[Book] = []
index = 0
