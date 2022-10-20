from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 주문 도서 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select b.no, b.title, a.count from orders_book a, book b where a.book_no = b.no;'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--주문 도서 리스트--')
    for index, result in enumerate(results):
        print(f'{result["no"]}, {result["title"]}, {result["count"]}')

# 주문 도서 추가
def insert(count, book_no):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into cart values(null, %d, %d)'
        count = cursor.execute(sql, (count, book_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    book_no = input('book_no : ')
    count = input('count : ')
    price = input('price : ')

    insert(count, book_no)

    print('---------------------------------------------')
    run_list()

# ----------------------------------------------------------------
def conn():
    db = connect(
        user='bookmall',
        password='bookmall',
        host='127.0.0.1',
        port=3306,
        db='bookmall',
        charset='utf8')

    return db