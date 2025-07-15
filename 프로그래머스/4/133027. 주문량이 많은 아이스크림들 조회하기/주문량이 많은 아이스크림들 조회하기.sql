with cte1 as (
    select * from first_half
    union
    select * from july
)

select flavor from cte1
group by flavor
order by sum(total_order) desc
limit 3