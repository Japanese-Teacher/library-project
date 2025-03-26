class Book:
    _index = 0
    def __init__(self, name: str, author: str):
        Book._index += 1
        self.index = Book._index
        self._index += 1
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f'''
Номер книги: {self.index}
Имя книги: {self.name}
Автор: {self.author}'''