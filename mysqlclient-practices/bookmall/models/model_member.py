from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

# 고객 추가
def insert(name, phone_number, email, password):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'insert into member values(null, %s, %s, %s, password(%s))'
        count = cursor.execute(sql, (name, phone_number, email, password))

        db.commit()

        cursor.close()
        db.close()

        return count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_add():
    name = input('name : ')
    phone_number = input('phone_number : ')
    email = input('email : ')
    password = input('password : ')

    insert(name, phone_number, email, password)

    print('---------------------------------------------')
    run_list()

# 고객 리스트
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
    print('--고객 리스트--')
    for index, result in enumerate(results):
        print(f'{index + 1}:{result["name"]}, {result["phone_number"]}, {result["email"]}, {result["password"]}')

# 고객 삭제 (이름, 비밀번호)
def deletebyname_password(name, password):
    try:
        db = conn()
        cursor = db.cursor()

        sql = 'delete from member where name = %s and password = password(%s)'
        count = cursor.execute(sql, (name, password, ))

        db.commit()

        cursor.close()
        db.close()

        return  count == 1
    except OperationalError as e:
        print(f'에러 : {e}')

def run_delete():
    name = input('name : ')
    password = input('password : ')
    deletebyname_password(name, password)
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