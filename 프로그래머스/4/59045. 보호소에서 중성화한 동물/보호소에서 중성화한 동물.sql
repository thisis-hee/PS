with cte1 as (
    select I.animal_id, I.animal_type, I.name, I.sex_upon_intake as ins, O.sex_upon_outcome as outs from animal_ins as I
    join animal_outs as O on I.animal_id=O.animal_id
)

select animal_id, animal_type, name from cte1
where ins != outs