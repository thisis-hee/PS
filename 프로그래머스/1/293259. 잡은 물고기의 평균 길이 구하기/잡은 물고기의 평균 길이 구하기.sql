with cte1 as (
    select
      id, fish_type, ifnull(length, 10) as length
    from fish_info
)

select round(avg(length),2) as average_length from cte1
