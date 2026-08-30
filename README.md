# qa_python
# Проект 4 спринта: Юнит-тестирование

## Описание

Проект содержит юнит-тесты для класса `BooksCollector`

Класс `BooksCollector` позволяет добавлять книги, устанавливать им жанры, получать книги по жанру, выбирать книги для детей и работать со списком избранных книг

## Реализованные тесты

1. Проверка невозможности добавления книги с названием длиной 41 и 50 символов - test_add_new_book_dont_add_book_with_41_and_50_symbols
2. Проверка установки жанра для добавленной книги - test_set_book_genre_book_and_genre_in
3. Проверка получения жанра книги по её названию - test_get_book_genre_by_book_name
4. Проверка получения списка книг определённого жанра - test_get_books_with_specific_genre_get_2_books_by_genre
5. Проверка получения текущего словаря книг и их жанров - test_get_books_genre_returns_get_books_genre_dict
6. Проверка получения списка книг, подходящих детям - test_get_books_for_children_return_list_of_books
7. Проверка добавления книги в избранное - test_add_book_in_favorites_adds_1_book_in_favorites
8. Проверка удаления книги из избранного - test_delete_book_from_favorites_deletes_1_book_from_favorites
9. Проверка получения списка избранных книг - test_get_list_of_favorites_books_returns_list_of_book_name

Для проверки граничных значений длины названия книги используется параметризация

## Запуск тестов

Для запуска тестов выполнить команду:

```bash
pytest -v tests.py