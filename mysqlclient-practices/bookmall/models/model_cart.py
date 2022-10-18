from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 카트 리스트
def findall():
    try:
        db = conn()
        cursor = db.cursor(DictCursor)

        sql = 'select name, phone_number, email, password from member order by no desc'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러 : {e}')

def run_list():
    results = findall()
    print('--회원 리스트--')
    for index, result in enumerate(results):
        print(f'{index + 1}:{result["name"]}, {result["phone_number"]}, {result["email"]}, {result["password"]}')


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