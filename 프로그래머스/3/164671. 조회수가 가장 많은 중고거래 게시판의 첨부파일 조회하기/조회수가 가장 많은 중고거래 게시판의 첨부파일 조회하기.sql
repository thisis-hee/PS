select concat('/home/grep/src/', B.board_id, '/', F.file_id, F.file_name, F.file_ext) as file_path from used_goods_board as B
join used_goods_file as F on B.board_id=F.board_id
where views = (select max(views) from used_goods_board)
order by F.file_id desc