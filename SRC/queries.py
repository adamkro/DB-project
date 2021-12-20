v

def query_1(min_votes, year):
    return f"""
    SELECT      M.title AS title, G.genre AS genre, R.mean_vote RATE rate
    FROM        (SELECT *
                 FROM movie
                 WHERE year = {year}) M
    JOIN        genre G ON M.id = G.movie_id
    JOIN        rating R ON M.id = R.id
    WHERE       R.total_votes >= {min_votes}
    GROUP BY    G.genre
    HAVING      R.mean_vote = MAX(R.mean_vote)
    """


def query_2(min_rating):
    return f"""
    SELECT      COUNT(PR.person_id) AS amount_of_actors
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        rating R ON PR.movie_id = R.id
    WHERE       R.mean_vote >= {min_rating} AND
                (PR.category = actor OR PR.category = actress)
    GROUP BY    PR.person_id
    HAVING      P.children = 0
    """

def query_3():
    return """
    SELECT      PE.name AS name, COUNT(G.genre) as genres
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        genre G ON G.movie_id = PR.movie_id
    WHERE       PR.category = writer
    GROUP BY    PR.person_id
    ORDER BY    COUNT(G.genre) as genres
    LIMIT       10
    """
