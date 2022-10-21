from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 카트 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select b.title, a.count, b.price * a.count as prices from cart a, book b where a.book_no = b.no'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--카트 리스트--')
    for index, result in enumerate(results):
        print(f'{index + 1} - 제목 : {result["title"]} / 수량 : {result["count"]} / 금액 : {result["prices"]}')

# 카트 추가
def insert(count, book_no, member_no):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into cart values(null, %s, %s, %s)'
        count = cursor.execute(sql, (count, book_no, member_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    member_no = input('member_no : ')
    book_no = input('book_no : ')
    count = input('count : ')

    insert(count, book_no, member_no)

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