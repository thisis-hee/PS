select P.product_code, sum(P.price*O.sales_amount) as sales from product as p
join offline_sale as O on P.product_id = O.product_id
group by product_code
order by sales desc, P.product_code