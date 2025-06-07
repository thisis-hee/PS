with writer_cnt as 
(
  select writer_id, count(*) as board_cnt from used_goods_board
    group by writer_id
    having count(*)>=3
)

# select * from writer_cnt

select 
  user_id, nickname, concat(city, ' ', street_address1, ' ',street_address2) as '전체주소', 
  concat(substring(TLNO,1,3),'-',substring(TLNO,4,4),'-',substring(TLNO,8,4))
  as '전화번호'
from used_goods_user as U
join writer_cnt as W on W.writer_id=U.user_id
order by U.user_id desc
