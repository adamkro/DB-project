    SELECT      PE.children, COUNT(person_id)
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        rating R ON PR.movie_id = R.id
    WHERE       R.mean_vote >= 9.8 AND
                (PR.category = 'actor' OR PR.category = 'actress')
    GROUP BY    PE.children

