from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 카테고리 추가
def insert(category):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into categorys values(null, %s)'
        count = cursor.execute(sql, (category, ))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    category = input('category : ')

    insert(category)

    print('---------------------------------------------')
    run_list()

# 카테고리 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select category from categorys order by no desc'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--카테고리 리스트--')
    for index, result in enumerate(results):
        print(f'{index + 1} - {result["category"]}')

# 카테고리 삭제
def deletebycategory(category):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'delete from categorys where category = %s'
        count = cursor.execute(sql, (category, ))

        db.commit()

        cursor.close()
        db.close()

        return  count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_delete():
    category = input('category : ')
    deletebycategory(category)
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