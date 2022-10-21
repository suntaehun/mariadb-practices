from bookmall.models import model_member, model_categorys, model_book, model_cart, model_orders, model_orders_book

model_member.insert('선태헌', '010-2994-7862', 'sth7862@naver.com', 'password(123123)')
model_member.insert('둘리', '010-1234-5678', 'dooly@naver.com', 'password(0000)')
model_categorys.insert('novel')
model_categorys.insert('essay')
model_categorys.insert('IT')
model_book.insert('데미안', 7200, 1)
model_book.insert('난중일기', 13500, 2)
model_book.insert('이것이 MySQL이다', 32000, 3)
model_cart.insert(5, 1, 2)
model_cart.insert(20, 3, 1)
model_orders.insert(32000, '인천광역시', 1)
model_orders_book.insert(20, 1)
model_orders_book.insert(50, 2)


model_member.run_list()
model_categorys.run_list()
model_book.run_list()
model_cart.run_list()
model_orders.run_list()
model_orders_book.run_list()