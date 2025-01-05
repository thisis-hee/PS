select count(*) as fish_count, fish_name from fish_info as info
join fish_name_info as name on name.fish_type=info.fish_type
group by fish_name
order by fish_count desc