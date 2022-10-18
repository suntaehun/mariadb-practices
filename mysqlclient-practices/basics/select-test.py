from MySQLdb import connect
from MySQLdb import OperationalError
from MySQLdb.cursors import DictCursor

try:
    # 1. 연결
    db = connect(
        user='webdb',
        password='webdb',
        host='127.0.0.1',
        port=3306,
        db='webdb',
        charset='utf8')

    # 2. cursor 생성
    cursor = db.cursor(DictCursor)

    # 3. sql(select문) 실행
    sql = 'select name, owner, species, gender, date_format(birth, "%Y-%m-%d") as birth from pet'
    count = cursor.execute(sql)

    # 4. 결과 받아오기
    results = cursor.fetchall()

    # 5. 자원 정리
    cursor.close()
    db.close()

    # 결과 확인
    for result in results :
        print(result)

except OperationalError as e:
    # 에러 처리
    print(f'에러 : {e}')