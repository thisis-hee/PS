with cte1 as (
    select animal_id from animal_ins
    where sex_upon_intake like '%Intact%'
),
cte2 as (
    select animal_id from animal_outs
    where (sex_upon_outcome like '%Spayed%' or sex_upon_outcome like '%Neutered%')
)

select A.animal_id, A.animal_type, A.name from animal_ins as A
join cte1 on A.animal_id=cte1.animal_id
join cte2 on cte1.animal_id=cte2.animal_id