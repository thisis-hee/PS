select 
  B.book_id, A.author_name, date_format(B.published_date, '%Y-%m-%d') as published_date 
from book as B
join Author as A on B.author_id=A.author_id
where category='경제'
order by published_date