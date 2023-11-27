import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Золотой ключик')
    collector.add_new_book('Оно')
    collector.add_new_book('Кто нашёл, берёт себе')
    collector.add_new_book('Сияние')
    collector.add_new_book('Профессия')
    collector.add_new_book('Винни-пух')
    collector.add_new_book('Настенькины комиксы')
    collector.add_new_book('Преступление и наказание')
    collector.add_new_book('Простоквашино')
    collector.set_book_genre('Золотой ключик', 'Мультфильмы')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Кто нашёл, берёт себе', 'Детективы')
    collector.set_book_genre('Сияние', 'Ужасы')
    collector.set_book_genre('Профессия', 'Фантастика')
    collector.set_book_genre('Винни-пух', 'Мультфильмы')
    collector.set_book_genre('Настенькины комиксы', 'Комедии')
    return collector
