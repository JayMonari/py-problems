import re


ISBN_LENGTH = 10


def is_valid(isbn: str) -> bool:
    isbn = re.sub("[^0-9X]", "", isbn)
    has_check_char = isbn.find('X') != -1
    if len(isbn) != ISBN_LENGTH or (
            has_check_char and isbn.find('X') != len(isbn) - 1):
        return False

    isbn = isbn[:-1] if has_check_char else isbn
    isbn_sum = sum([int(d) * (ISBN_LENGTH - i) for i, d in enumerate(isbn)])
    isbn_sum += 10 if has_check_char else 0
    return isbn_sum % 11 == 0
