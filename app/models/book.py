class Book:

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f'''Имя книги: {self.name}
Автор: {self.author}'''