show tables;

-- insert into categorys values(null,'novel');
-- insert into categorys values(null, 'essay');
-- insert into categorys values(null, 'IT');
-- select * from categorys;
select no, category from categorys order by no desc;


-- insert into member values(null, '선태헌', '010-2994-7862', 'sth7862@naver.com', password(123123));
-- insert into member values(null, '둘리', '010-1234-5678', 'dooly@naver.com', password(0000));
-- select * from member;
select name, phone_number, email, password from member order by no desc;


--  insert into book values(null, '데미안', 7200, 1);
-- insert into book values(null, '난중일기', 13500, 2);
-- insert into book values(null, '이것이 MySQL이다', 32000, 3);
-- select * from book;
select title, price from book order by no desc;

-- insert into cart values(null, 5, 1, 2);
-- insert into cart values(null, 20, 3, 1);
-- select * from cart;
select b.title, a.count, b.price * a.count as prices
	from cart a, book b
   where a.book_no = b.no;


-- insert into orders values(null, 32000, '인천광역시', 1);
-- select * from orders;
select a.no, b.name, b.email, a.price, a.address
	from orders a, member b
   where a.member_no = b.no;

-- insert into orders_book values(null, 20, 1);
-- insert into orders_book values(null, 50, 2);
-- select * from orders_book;
select b.no, b.title, a.count from orders_book a, book b where a.book_no = b.no;