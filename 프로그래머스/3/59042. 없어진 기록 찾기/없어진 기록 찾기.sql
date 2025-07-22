select O.animal_id, O.name from animal_outs as O
left outer join animal_ins as I on O.animal_id=I.animal_id
where I.name is null and O.name is not null
order by I.animal_id, I.name