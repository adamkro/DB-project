select movie.title,count(if(match(person.name) against ('James'),1, NULL)) as numOfSmiths
from person, movie,principal
where person.id=principal.person_id and movie.id=principal.movie_id and principal.category="actor"
group by movie.id
order by numOfSmiths desc;