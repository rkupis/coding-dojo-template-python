import unittest

class Discount:
    NoDiscount = 1
    TwoVariousBooks = 0.95
    ThreeVariousBooks = 0.90
    FourVariousBooks = 0.80
    FiveVariousBooks = 0.75

class Book:
    PRICE = 8
    def __init__(self, type):
        print('Book')

    class Type:
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        FIFTH = 5
        def __init__(self):
            print('Type')

class Corb:
    def __init__(self):
        self.books = []
    def clear(self):
        self.books = []
    def add(self, book):
        if book not in self.books:
            self.books.append(book)
    def itemCounter(self):
        return len(self.books)

    def sumPrice(self):
        return 100

class ExampleTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1, 1)

    def test_corb_isempty(self):
        corb = Corb()
        corb.clear()
        self.assertEqual(corb.itemCounter, 0)

    def test_corb_add_this_same_books(self):
        corb = Corb()
        book1 = Book(Book.Type.SECOND)
        corb.add(book1)
        self.test_corb_sum( corb, 1, Discount.NoDiscount)
        book2 = Book(Book.Type.SECOND)
        corb.add(book2)
        self.test_corb_sum( corb, 2, Discount.NoDiscount)
        book3 = Book(Book.Type.SECOND)
        corb.add(book3)
        self.test_corb_sum( corb, 3, Discount.NoDiscount)
        book4 = Book(Book.Type.SECOND)
        corb.add(book4)
        self.test_corb_sum( corb, 4, Discount.NoDiscount)
        book5 = Book(Book.Type.SECOND)
        corb.add(book5)
        self.test_corb_sum( corb, 5, Discount.NoDiscount)

    def test_corb_add_various_books(self):
        corb = Corb()
        book1 = Book(Book.Type.FIRST)
        corb.add(book1)
        self.test_corb_sum( corb, 1, Discount.NoDiscount)
        book2 = Book(Book.Type.SECOND)
        corb.add(book2)
        self.test_corb_sum( corb, 2, Discount.TwoVariousBooks)
        book3 = Book(Book.Type.THIRD)
        corb.add(book3)
        self.test_corb_sum( corb, 3, Discount.ThreeVariousBooks)
        book4 = Book(Book.Type.FOURTH)
        corb.add(book4)
        self.test_corb_sum( corb, 4, Discount.FourVariousBooks)
        book5 = Book(Book.Type.Five)
        corb.add(book5)
        self.test_corb_sum( corb, 5, Discount.FiveVariousBooks)

    def test_corb_add_this_same_instance_of_books(self):
        corb = Corb()
        book1 = Book(Book.Type.FIRST)
        corb.add(book1)
        self.test_corb_sum( corb, 1, Discount.NoDiscount)
        corb.add(book1)
        self.test_corb_sum( corb, 1, Discount.NoDiscount)

    def test_corb_sum(self, corb, o, discount):
        self.assertEqual(corb.itemCounter(), expectedCounterStarte)
        self.assertEqual(corb.sumPrice(), corb.itemCounter() * Book.PRICE * discount)


    def test_corb_isempty(self):
        corb = Corb()
        corb.clear()
        self.assertEqual(corb.itemCounter, 0)

if __name__ == '__main__':
    unittest.main()
