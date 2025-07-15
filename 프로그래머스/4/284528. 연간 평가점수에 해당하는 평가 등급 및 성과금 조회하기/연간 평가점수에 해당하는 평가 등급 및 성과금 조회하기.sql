with cte1 as (
    select emp_no, avg(score) as score from hr_grade
    group by emp_no
),
cte2 as (
    select 
        E.emp_no, E.emp_name, E.sal,
        case when cte1.score>=96 then 'S'
        when cte1.score>=90 then 'A'
        when cte1.score>=80 then 'B'
        else 'C' end as 'rating'
    from hr_employees as E
    join cte1 on E.emp_no=cte1.emp_no
)

select 
    emp_no, emp_name, rating as grade,
    case when rating='S' then sal*0.2
    when rating='A' then sal*0.15
    when rating='B' then sal*0.1
    else 0
    end as 'bonus'
from cte2
order by emp_no asc
