select MCDP_CD as '진료과코드', count(*) as '5월예약건수' from appointment
where date_format(APNT_YMD, '%Y-%m')='2022-05'
group by MCDP_CD
order by count(*) asc, MCDP_CD asc

