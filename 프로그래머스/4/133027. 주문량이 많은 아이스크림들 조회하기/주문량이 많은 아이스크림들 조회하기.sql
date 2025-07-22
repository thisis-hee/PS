with cte1 as (
    select shipment_id, flavor, sum(total_order) as total_order from july
    group by flavor
), 
cte2 as (
    select 
      F.*, F.total_order+cte1.total_order as total_sum 
    from first_half as F
    join cte1 on F.flavor=cte1.flavor
    order by total_sum desc
)

select flavor from cte2
order by total_sum desc
limit 3