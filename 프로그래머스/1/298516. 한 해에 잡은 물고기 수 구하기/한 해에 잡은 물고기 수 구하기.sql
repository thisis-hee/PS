select count(*) as fish_count from fish_info
where date_format(time, '%Y')='2021'