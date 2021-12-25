select person.name,count(movie_id) as numberOfBestPictureWinningMoviesDirectedByHim
from principal,person
where category="director" and principal.person_id=person.id and exists (select * from best_picture_winners where best_picture_winners.id=principal.movie_id)
group by principal.person_id
order by count(movie_id) desc
limit 1;
