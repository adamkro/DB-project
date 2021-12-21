    SELECT      PE.name AS name, COUNT(G.genre) AS genres
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        genre G ON G.movie_id = PR.movie_id
    WHERE       PR.category = 'writer'
    GROUP BY    PR.person_id
    ORDER BY    COUNT(G.genre) DESC
    LIMIT       10
