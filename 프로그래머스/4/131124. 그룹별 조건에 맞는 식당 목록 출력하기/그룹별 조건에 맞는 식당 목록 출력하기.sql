with cte1 as (
    select 
        M.member_name, count(R.review_text) as review_cnt
    from rest_review as R
    join member_profile as M on R.member_id=M.member_id
    group by M.member_name
    order by review_cnt desc
),
cte2 as (
    select member_name from cte1
    where review_cnt=(select max(review_cnt) from cte1)
)

select
    M.member_name, R.review_text,
    date_format(R.review_date, '%Y-%m-%d') as review_date
from rest_review as R
join member_profile as M on R.member_id=M.member_id
where M.member_name in (select * from cte2)
order by review_date, review_text