-- 문제1. 현재 평균 연봉보다 많은 월급을 받는 직원은 몇 명이나 있습니까?
select count(*)
	from salaries
   where to_date = '9999-01-01'
	and salary > (select avg(salary)
						from salaries
					  where to_date = '9999-01-01');

-- 문제2. 현재, 각 부서별로 최고의 급여를 받는 사원의 사번, 이름, 부서, 연봉을 조회하세요.
-- 단 조회결과는 연봉의 내림차순으로 정렬되어 나타나야 합니다.
select a.emp_no, a.first_name, d.dept_name, c.salary
	from employees a, dept_emp b, salaries c, departments d
   where a.emp_no = b.emp_no
	and a.emp_no = c.emp_no
    and b.dept_no = d.dept_no
    and b.to_date = '9999-01-01'
    and c.to_date = '9999-01-01'
    and (b.dept_no, c.salary) in (select dept_no, max(salary)
									from dept_emp a, salaries b
								   where a.emp_no = b.emp_no
									and a.to_date = '9999-01-01'
									and b.to_date = '9999-01-01'
								   group by dept_no)
order by c.salary desc;

-- 문제3. 현재, 자신의 부서 평균 급여보다 연봉(salary)이 많은 사원의 사번, 이름과 연봉을 조회하세요
select a.emp_no, a.first_name, c.salary
	from employees a, dept_emp b, salaries c,
		(select a.dept_no, avg(b.salary) as avg_salary
			from dept_emp a, salaries b
		   where a.emp_no = b.emp_no
			and a.to_date = '9999-01-01'
			and b.to_date = '9999-01-01'
		   group by a.dept_no) d
   where a.emp_no = b.emp_no
	and a.emp_no = c.emp_no
    and d.dept_no = b.dept_no
    and b.to_date = '9999-01-01'
    and c.to_date = '9999-01-01'
    and c.salary > d.avg_salary;

-- 문제4. 현재, 사원들의 사번, 이름, 매니저 이름, 부서 이름으로 출력해 보세요.    
select a.emp_no, a.first_name, d.manager_name, c.dept_name
	from employees a,
		 dept_emp b,
         departments c,
         (select a.dept_no, b.emp_no, b.first_name as manager_name
			from dept_manager a, employees b
			where a.emp_no = b.emp_no
			  and a.to_date = '9999-01-01') d
	where a.emp_no = b.emp_no
	 and b.dept_no = c.dept_no
     and d.dept_no = c.dept_no
     and b.to_date = '9999-01-01'
order by a.emp_no;
     
-- 문제5. 현재, 평균연봉이 가장 높은 부서의 사원들의 사번, 이름, 직책, 연봉을 조회하고 연봉 순으로 출력하세요.
 select a.emp_no, a.first_name, c.title, d.salary
	from employees a,
		 dept_emp b,
         titles c,
         salaries d,
         (select a.dept_no as max_dept_no, avg(b.salary) as avg_max_salary
			from dept_emp a, salaries b
			where a.emp_no = b.emp_no
			 and a.to_date = '9999-01-01'
			 and b.to_date = '9999-01-01'
			group by a.dept_no
            having avg_max_salary = (select max(a.avg_salary) 
									from (select a.dept_no, avg(b.salary) as avg_salary
											from dept_emp a, salaries b
											where a.emp_no = b.emp_no
											and a.to_date = '9999-01-01'
											and b.to_date = '9999-01-01'
											group by a.dept_no) a)) e
	  where a.emp_no = b.emp_no
		and a.emp_no = c.emp_no
        and a.emp_no = d.emp_no
        and e.max_dept_no = b.dept_no
        and b.to_date = '9999-01-01'
        and c.to_date = '9999-01-01'
        and d.to_date = '9999-01-01'
        and b. dept_no = e.max_dept_no;
    
-- 문제6. 평균 연봉이 가장 높은 부서는?
select a.dept_no as dept_no, avg(b.salary) as avg_salary
	from dept_emp a, salaries b
   where a.emp_no = b.emp_no
 group by a.dept_no;
 
 select max(a.avg_salary)
	from (select a.dept_no, avg(b.salary) as avg_salary
			from dept_emp a, salaries b
			where a.emp_no = b.emp_no
			group by a.dept_no) a;
 
 
 
 select *
	from departments a,
		(select a.dept_no, avg(b.salary) as avg_salary
			from dept_emp a, salaries b
			where a.emp_no = b.emp_no
			group by a.dept_no) b
	where a.dept_no = b.dept_no


-- 문제7. 평균 연봉이 가장 높은 직책?

-- 문제8. 현재 자신의 매니저보다 높은 연봉을 받고 있는 직원은?
-- 부서이름, 사원이름, 연봉, 매니저 이름, 메니저 연봉 순으로 출력합니다.