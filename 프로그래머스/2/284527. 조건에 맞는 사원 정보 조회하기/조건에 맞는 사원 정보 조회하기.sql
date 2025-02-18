select sum(gr.score) as score, gr.emp_no, em.emp_name, em.position, em.email from hr_department as dt
join hr_employees as em on dt.dept_id=em.dept_id
join hr_grade as gr on em.emp_no=gr.emp_no
group by em.emp_no
order by score desc
limit 1