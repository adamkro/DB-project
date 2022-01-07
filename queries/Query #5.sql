/*555 - user gross income - at least 5 million dollars, average vote of at least 5, at least 5 actors */

select movie.title
from principal, movie,rating 
where movie.id=rating.id and rating.mean_vote>=5 and principal.movie_id=movie.id and movie.usa_gross_income>=5000000 and (principal.category="actor" or principal.category="actress")
group by principal.movie_id
having count(principal.id)>=5;