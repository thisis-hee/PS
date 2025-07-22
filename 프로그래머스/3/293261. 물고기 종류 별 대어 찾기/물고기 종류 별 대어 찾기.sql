with cte1 as (
    select * from
    (select
      I.id, N.fish_name, I.length,
      row_number() over (partition by fish_name order by length desc) as rnk
    from fish_info as I
    join fish_name_info as N on I.fish_type=N.fish_type) as sub
    where rnk=1
)

select id, fish_name, length from cte1
order by id