from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 상품 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select title, price from book order by no desc'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--상품 리스트--')
    for index, result in enumerate(results):
        print(f'{index + 1} - 제목 : {result["title"]} / 가격 : {result["price"]}원')

# 상품 추가
def insert(title, price, categorys_no):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into book values(null, %s, %s, %s)'
        count = cursor.execute(sql, (title, price, categorys_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    title = input('title : ')
    price = input('price : ')
    categorys_no = input('categorys_no : ')

    insert(title, price, categorys_no)

    print('---------------------------------------------')
    run_list()

# 상품 삭제
def deletebytitle(title):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'delete from book where title = %s'
        count = cursor.execute(sql, (title, ))

        db.commit()

        cursor.close()
        db.close()

        return  count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_delete():
    title = input('title : ')
    deletebytitle(title)
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