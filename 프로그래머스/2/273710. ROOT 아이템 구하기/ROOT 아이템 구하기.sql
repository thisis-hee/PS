with cte_1 as (select * from item_tree
where parent_item_id is null)

select I.item_id, I.item_name from item_info as I
join cte_1 as C on I.item_id=C.item_id
order by I.item_id