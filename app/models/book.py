class Book:

    def __init__(self, index: int, name: str, author: str):
        self.index = index
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f'''Номер книги: {self.index}
Имя книги: {self.name}
Автор: {self.author}'''