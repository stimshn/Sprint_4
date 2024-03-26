import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_book_and_this_book_is_on_list(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1 and list(collector.books_genre.keys())[0] == name

    def test_add_new_book_long_name_book_is_not_added(self):
        collector = BooksCollector()
        name = 'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_add_genre_for_book(self):
        collector = BooksCollector()
        name = '12 стульев'
        collector.add_new_book(name)
        collector.set_book_genre(name,'Комедии')
        assert list(collector.books_genre.values())[0] == 'Комедии'

    def test_set_book_genre_adding_undefined_genre_is_not_added(self):
        collector = BooksCollector()
        name = 'Как относиться к себе и людям'
        collector.add_new_book(name)
        collector.set_book_genre(name,'Психология')
        assert list(collector.books_genre.values())[0] == ''

    def test_get_book_genre_book_genre_found(self):
        collector = BooksCollector()
        name = 'Мастер и Маргарита'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'

    def test_get_books_with_specific_genre_get_fantastic_genre(self):
        collector = BooksCollector()
        name_1 = 'Портрет Дориана Грея'
        name_2 = 'Грозовой перевал'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Фантастика')
        collector.set_book_genre(name_2, 'Детективы')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 1

    def test_get_books_genre_books_displayed_in_dictionary(self):
        collector = BooksCollector()
        name_1 = 'Приключения Алисы в стране чудес'
        name_2 = 'Робинзон Крузо'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Мультфильмы')
        collector.set_book_genre(name_2, 'Детективы')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_books_with_age_genre_not_included_in_list(self):
        collector = BooksCollector()
        name_1 = 'Маленький принц'
        name_2 = 'Заводной апельсин'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Мультфильмы')
        collector.set_book_genre(name_2, 'Ужасы')
        assert collector.get_books_for_children()[0] == name_1

    def test_add_book_in_favorites_book_added_in_favorites(self):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Мультфильмы')
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        collector = BooksCollector()
        name = 'Евгений Онегин'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Детективы')
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_favorites_book_in_list(self):
        collector = BooksCollector()
        name_1 = 'Облачный атлас'
        name_2 = 'Марсианин'
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)
        collector.set_book_genre(name_1, 'Фантастика')
        collector.set_book_genre(name_2, 'Фантастика')
        collector.add_book_in_favorites(name_1)
        collector.add_book_in_favorites(name_2)
        assert collector.get_list_of_favorites_books() == [name_1, name_2]