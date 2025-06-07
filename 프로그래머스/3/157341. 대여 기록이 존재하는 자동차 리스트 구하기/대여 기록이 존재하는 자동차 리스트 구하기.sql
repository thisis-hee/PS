select 
  C.car_id
from car_rental_company_car as C
join car_rental_company_rental_history as H on C.car_id=H.car_id
where H.start_date between '2022-10-01' and '2022-10-31' and C.car_type='세단'
group by C.car_id
order by C.car_id desc

