show tables;
desc book;
desc author;

-- author insert
insert into author values(null, '원수연');

-- author select
select * from author;

-- author delete all
delete from author;

-- book insert
insert into book values(null, 'test', '재고있음', 3);

-- book select
select * from book;

-- book delete all
delete from book;

-- findAll
select a.no, a.title, b.name, a.status
 from book a, author b where a.author_no = b.no order by a.no asc;
 
 -- status update
 update book set status = ? where no = ?;