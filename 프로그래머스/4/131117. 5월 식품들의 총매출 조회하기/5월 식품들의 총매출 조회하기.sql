select 
    product.product_id, product.product_name, 
    sum(product.price*ord.amount) as total_sales
from food_product as product
join food_order as ord on product.product_id=ord.product_id
where year(ord.produce_date)=2022 and month(ord.produce_date)=5
group by product.product_id
order by total_sales desc, product.product_id asc