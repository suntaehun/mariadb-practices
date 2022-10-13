-- 함수 : 날짜 함수
-- curdate(), current_date : 날짜
select curdate(), current_date;

-- curtime(), current_time : 시간
select curtime(), current_time;

-- now() : 날짜+시간  vs  sysdate()
select now(), sysdate();
select now(), sleep(2), now();
select now(), sleep(2), sysdate();

-- date_format()
-- 2022년 10월 13일 10:12:55
select date_format(now(), '%Y년 %m월 %d일 %h:%i:%s');
select date_format(now(), '%d %b, \ %y %h:%i:%s');

-- period_diff
-- 포멧팅: YYMM
-- 예) 근무 개월 수
select first_name, period_diff(date_format(curdate(), '%y%m'), date_format(hire_date, '%y%m')) as month
	from employees order by month desc;
    
-- date_add(=adddate), date_sub(=subdate)
-- 날짜를 date에 type(year, month, day)의 표현식을 더하거나 뺀다.
-- 예제) 각 사원들의 근속년 수가 5년이 되는 날은 언제인가요?
select first_name, hire_date, date_add(hire_date, interval 5 year)
	from employees;

-- cast
select '12345' + 10, cast('12345' as int) + 10;
select date_format(cast('2022-10-10' as date), '%Y년 %m월 %d일');
select cast(cast(1-2 as unsigned) as signed);
select cast(cast(1-2 as unsigned) as int);
select cast(cast(1-2 as unsigned) as integer);

-- type
-- 문자 : varchar, char, text, CLOB(Character Large OBject)
-- 정수 : signed(unsigned), int(integer), medium int, big int
-- 실수 : float, double
-- 시간 : date, datetime
-- LOB : CLOB, BLOB(Binary Large OBject)
