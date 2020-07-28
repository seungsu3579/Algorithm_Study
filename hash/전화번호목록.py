# 전화번호 목록


def solution(phone_book):
    phone_book.sort()
    phone_book_map = dict()
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_book_map.get(phone_number[:i], None) != None:
                return False
        phone_book_map[phone_number] = 1
    return True
