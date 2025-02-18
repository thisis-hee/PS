select pd.product_code, sum(pd.price*off.sales_amount) as sales from product as pd
join offline_sale as off on pd.product_id=off.product_id
group by product_code
order by sales desc, product_code asc
