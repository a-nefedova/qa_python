import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Подозрительные пассажиры твоих ночных поездов', ''])
    def test_add_new_book_not_add(self, name, collector):
        books_before_add = len(collector.get_books_genre())
        collector.add_new_book(name)
        books_after_add = len(collector.get_books_genre())
        assert books_after_add == books_before_add

    def test_set_book_genre_set(self, collector):
        collector.set_book_genre('Простоквашино', 'Мультфильмы')
        assert collector.get_book_genre('Простоквашино') == 'Мультфильмы'

    def test_set_book_genre_not_set(self, collector):
        collector.set_book_genre('Преступление и наказание', 'Романы')
        assert collector.get_book_genre('Преступление и наказание') == ''

    def test_get_book_genre_got_genre(self, collector):
        assert collector.get_book_genre('Профессия') == 'Фантастика'

    def test_get_books_with_specific_genre_got_two_books(self, collector):
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_genre_got_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Керри')
        collector.set_book_genre('Керри', 'Ужасы')
        collector.add_new_book('Роза Марена')
        collector.set_book_genre('Роза Марена', 'Ужасы')
        assert collector.get_books_genre() == {'Керри': 'Ужасы', 'Роза Марена': 'Ужасы'}

    def test_get_books_for_children_got_books_wo_age_rating(self, collector):
        books_for_children = ['Золотой ключик', 'Профессия', 'Винни-пух', 'Настенькины комиксы']
        assert collector.get_books_for_children() == books_for_children

    def test_add_book_in_favorites_add_two_books(self, collector):
        collector.add_book_in_favorites('Кто нашёл, берёт себе')
        collector.add_book_in_favorites('Оно')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_got_one_book(self, collector):
        collector.add_book_in_favorites('Кто нашёл, берёт себе')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Кто нашёл, берёт себе')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_got_list(self, collector):
        collector.add_book_in_favorites('Кто нашёл, берёт себе')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Кто нашёл, берёт себе', 'Оно']
