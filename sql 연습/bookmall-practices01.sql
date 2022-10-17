show tables;

-- insert into category values(null,'novel');
-- insert into category values(null, 'essay');
-- insert into category values(null, 'IT');
select * from category;

-- insert into member values(null, '선태헌', '010-1234-5678', 'qwer@adsf.com', password(123123));
-- insert into member values(null, '조성훈', '010-9876-5432', 'zxcv@qwer.com', password(0000));
select * from member;

-- insert into book values(null, 'AAA', 15000, 1);
-- insert into book values(null, 'BBB', 24000, 2);
-- insert into book values(null, 'CCC', 18000, 3);
select * from book;

-- insert into cart values(null, 1, 2, 1);
-- insert into cart values(null, 1, 3, 2);
select * from cart;

-- insert into orders values(null, 24000, '인천광역시 검암동', 1);
select * from orders;

insert into orders_book values(null, 1, 1, 1);
insert into orders_book values(null, 1, 2, 1);
select * from orders_book;
