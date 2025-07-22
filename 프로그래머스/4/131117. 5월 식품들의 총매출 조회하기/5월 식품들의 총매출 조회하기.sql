with cte1 as (
    select
      P.product_id, P.product_name, P.price, O.amount, P.price*O.amount as total, O.produce_date
    from food_product as P
    join food_order as O on P.product_id=O.product_id
    where year(produce_date)=2022 and month(produce_date)=5
)

select product_id, product_name, sum(total) as total_sales from cte1
group by product_id
order by total_sales desc, product_id