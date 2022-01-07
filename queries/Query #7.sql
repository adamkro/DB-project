select birthplace, count(id)
from person
where birthplace like '%usa' and birthplace<>'usa'
group by birthplace
having count(id)>0
order by count(id) desc;