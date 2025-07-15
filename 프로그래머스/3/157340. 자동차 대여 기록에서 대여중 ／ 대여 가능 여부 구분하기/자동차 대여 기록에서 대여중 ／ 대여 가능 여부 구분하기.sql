# 대여중인 car_id
with cte1 as (
    select distinct car_id, 0 as availability from car_rental_company_rental_history
    where start_date<='2022-10-16' and end_date>='2022-10-16'
),
# 전체 car_id
cte2 as (
    select distinct car_id from car_rental_company_rental_history
)

select 
    cte2.car_id,
    case when availability='0' then '대여중' else '대여 가능' end as availability
from cte2
left outer join cte1 on cte2.car_id=cte1.car_id
order by car_id desc
