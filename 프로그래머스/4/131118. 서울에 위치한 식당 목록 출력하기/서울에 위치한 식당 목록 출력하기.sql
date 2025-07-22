with cte1 as (
  select
    rest_id, rest_name, food_type,
    favorites, address
  from rest_info
),
cte2 as (
  select 
    rest_id, round(avg(review_score),2) as score
  from rest_review
  group by rest_id
)

select cte1.*, cte2.score from cte1
join cte2 on cte1.rest_id=cte2.rest_id
where address like '서울%'
order by score desc, favorites desc