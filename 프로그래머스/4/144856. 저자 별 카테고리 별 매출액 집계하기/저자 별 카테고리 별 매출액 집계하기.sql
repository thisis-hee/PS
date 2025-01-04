select 
    book.author_id, author.author_name, book.category,
    sum(book.price*sales.sales) as total_sales
from book as book
join author as author on book.author_id=author.author_id
join book_sales as sales on book.book_id=sales.book_id
where 
    year(sales.sales_date)='2022' and month(sales.sales_date)='01'
group by author.author_name, book.category
order by book.author_id asc, book.category desc