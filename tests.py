import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверяем, что не создаются книги с количеством символов в названии = 41 и 50
    @pytest.mark.parametrize(
        'book_name',
        [
            'a' * 41,
            'a' * 50
        ]
    )
    def test_add_new_book_dont_add_book_with_41_and_50_symbols(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name not in collector.books_genre


    # Проверяем, что set_book_genre устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_book_and_genre_in(self):

        collector = BooksCollector()

        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Ужасы')

        assert collector.books_genre['Идиот'] == 'Ужасы'


    # Проверяем, что выводится жанр книги по названию
    def test_get_book_genre_by_book_name(self):
        collector = BooksCollector()
        
        collector.add_new_book('Гроза')
        collector.set_book_genre('Гроза', 'Фантастика')

        assert collector.get_book_genre('Гроза') == 'Фантастика'


    # Проверяем, что get_books_with_specific_genre выводит список книг определённого жанра
    def test_get_books_with_specific_genre_get_2_books_by_genre(self):

        collector = BooksCollector()

        for book_name in ['Война и мир', 'Вишнёвый сад']:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, 'Детективы')

        assert collector.get_books_with_specific_genre('Детективы') == ['Война и мир', 'Вишнёвый сад']


    # Проверяем, что get_books_genre выводит текущий словарь books_genre
    def test_get_books_genre_returns_get_books_genre_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Ужасы')

        assert collector.get_books_genre() == {'Идиот': 'Ужасы'}


    # Проверяем, что get_books_for_children возвращает список книг, который подходит детям
    def test_get_books_for_children_return_list_of_books(self):

        collector = BooksCollector()

        for book_name, genre in zip(
              ['Зверополис', 'Двенадцать стульев', '1984', 'Зов Ктулху'],
              ['Мультфильмы', 'Комедии', 'Фантастика', 'Ужасы']
              ):
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        assert collector.get_books_for_children() == ['Зверополис', 'Двенадцать стульев', '1984']


    # Проверяем, что add_book_in_favorites добавляет книгу в избранное
    def test_add_book_in_favorites_adds_1_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Идиот')
        collector.add_book_in_favorites('Идиот')

        assert collector.favorites == ['Идиот']

    # Проверяем, что delete_book_from_favorites удаляет 1 книгу из списка favorites
    def test_delete_book_from_favorites_deletes_1_book_from_favorites(self):
        collector = BooksCollector()

        for book_name in ['Зверополис', '1984']:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites('Зверополис')

        assert collector.favorites == ['1984']

    # Проверяем, что get_list_of_favorites_books возвращает список избранных книг
    def test_get_list_of_favorites_books_returns_list_of_book_name(self):
        collector = BooksCollector()
        
        for book_name in ['Зверополис', '1984']:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == ['Зверополис', '1984']