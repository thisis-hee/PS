select distinct H.car_id from car_rental_company_rental_history as H
join car_rental_company_car as C on H.car_id=C.car_id
where C.car_type='세단' and month(H.start_date)=10
order by H.car_id desc