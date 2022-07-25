from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):  # Добавление двух книг.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_one_book_twice(self):  # Нельзя добавить одну и ту же книгу дважды.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_which_is_not_in_the_list(self):  # Нельзя выставить рейтинг книге, которой нет в списке.
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)
        assert len(collector.books_rating) == 0

    def test_set_book_rating_less_than_1(self):  # Нельзя выставить рейтинг меньше 1.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert collector.books_rating['Гордость и предубеждение и зомби'] != 0

    def test_set_book_rating_more_than_10(self):  # Нельзя выставить рейтинг больше 10.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert collector.books_rating['Гордость и предубеждение и зомби'] < 10

    def test_get_book_rating_at_not_added_book_not_rating(self):  # У не добавленной книги нет рейтинга.
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    def test_get_book_rating_added_book_has_a_default_rating_of_1(self):  # У добавленной книги рейтинг по умиолчанию 1.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating(self):  # Вывод списка книг с определенным рейтингом.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_with_specific_rating(1) == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_rating_incorrect_rating(self):  # Вывод списка книг с неккоретным рейтингом.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 6)
        assert collector.get_books_with_specific_rating(8) == []

    def test_get_books_rating_efficiency(self):  # Проверка метода get_books_rating.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1}

    def test_get_books_rating_efficiency_no_add_book(self):  # Проверка метода get_books_rating не добавляя книг.
        collector = BooksCollector()
        assert collector.get_books_rating() == {}

    def test_add_book_in_favorites(self):  # Добавление книг в избранное.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби']

    def test_delete_book_from_favorites(self):  # Удаление книги из избранного.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.delete_book_from_favorites('Гордость и предубеждение и зомби') == None

    def test_get_list_of_favorites_books(self):  # Получение список Избранных книг.
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
