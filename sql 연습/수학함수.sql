-- 함수 : 수학
-- abs : 절대값
select abs(1), abs(-1);

-- ceil : 바로 위 정수
select ceil(3.14), ceiling(3.14);

-- floor : 바로 아래 정수
select floor(3.14);

-- mod : 나머지
select mod(10, 3);

-- round(x) : x에 가장 근접한 정수
-- round(x, d) : x값 중에 소수점 d자리에 가장 근접한 실수
select round(1.498), round(1.498, 1), round(1.498, 0);

-- power(x, y), pow(x, y) : x의 y승
select power(2, 10), pow(2, 10);

-- sign(x) : 양수:1, 음수:-1, 0:0
select sign(20), sign(-20), sign(0);

-- greatest(x, y, ---) : 가장 큰 값
-- least(x, y, ---,) : 가장 작은 값
select greatest(10, 40, 20, 50), least(10, 40, 20, 50);
select greatest('b', 'A', 'C', 'B'), greatest('hello', 'hela', 'hell');










