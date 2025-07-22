select 
  H.flavor
from first_half as H
join icecream_info as I on H.flavor=I.flavor
where I.ingredient_type='fruit_based' and H.total_order>3000