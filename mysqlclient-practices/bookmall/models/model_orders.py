from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 주문 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select a.no, b.name, b.email, a.price, a.address from orders a, member b where a.member_no = b.no'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--주문 리스트--')
    for index, result in enumerate(results):
        print(f'{result["no"]}, ({result["name"]}, {result["email"]}), {result["price"]}, {result["address"]}')

# 주문 추가
def insert(price, address, member_no):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into cart values(null, %d, %s, %d)'
        count = cursor.execute(sql, (price, address, member_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    member_no = input('member_no : ')
    address = input('address : ')
    price = input('price : ')

    insert(price, address, member_no)

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