-- 대소문자 구분없음, 버전, 날짜 
SELECT VERSION(), Version(), CURRENT_DATE, cUrrent_DaTe;

 -- 함수 및 수식
select
sin(PI()/4),
(4+1)*5;
select version(); select now();
-- 테이블 삭제
drop table pet;

-- 테이블 만들기
create table pet(
	name varchar(20),
	owner varchar(20),
    species varchar(20),
    gender char(1),
    birth date,
    death date
);

-- 스키마 확인
desc pet;

-- 조회
select name, owner, species, gender, birth, death from pet;

-- 데이터 넣기(생성, Create)
insert into pet value('개개', '선태헌', 'dog', 'm', '2022-10-12', null);

-- 데이터 삭제(삭제, Delete)
delete from pet where name ='개개';

-- load data local file
load data local infile 'C:\\pet.txt' into table pet;

-- udate(수정, Update) death
update pet set death = null where name != 'Bowser';

-- 조회1 : where
-- 1990년 이후에 태어난 아이들은?(출력 : 이름, 종, 생일)
select name, species, birth from pet where birth > '1990-12-31';

-- Gwen과 함께 사는 아이들은?(출력 : 이름, 종, 주인)
select name, species, owner from pet where owner = 'Gwen';

-- null 다루기1 : 현재 살아있는 아이들은?(출력 : 이름, 생일, 사망일)
select name, birth, death from pet where death is null;

-- null 다루기2 : 죽은 아이들은?(출력 : 이름, 생일, 사망일)
select name, birth, death from pet where death is not null;

-- like 검색1(패턴매칭) : 이름이 b로 시작하는 아이들은?(출력 : 이름)
select name from pet where name like 'b%';

-- like 검색2(패턴매칭) : 이름이 b로 시작하는 아이들 중에 이름이 6자인 아이는?(출력 : 이름)
select name from pet where name like 'b_____'; 

-- 정렬(order by)
-- 아이들을 어린 순으로 출력 (이름, 생일)
select name, birth from pet order by birth desc;
-- 아이들을 나이가 많은 순으로 출력 (이름, 생일)
select name, birth from pet order by birth asc;

-- 집계(통계) 함수
select count(*) from pet;



show databases;
show tables;