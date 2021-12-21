
def query_1(min_votes, year):
    return f"""
    SELECT ranks.title, ranks.genre, ranks.rate
    FROM 	(
            SELECT      M.title AS title, G.genre AS genre, R.mean_vote AS rate,
                            ROW_NUMBER() OVER (PARTITION BY G.genre ORDER BY R.mean_vote DESC) AS movieRank
            FROM        (SELECT *
                        FROM movie
                        WHERE YEAR = {year}) M
            JOIN        genre G ON M.id = G.movie_id
            JOIN        rating R ON M.id = R.id
            WHERE       R.total_votes >= {min_votes}
            ) AS ranks
    WHERE ranks.movieRank = 1
    """


def query_2(min_rating):
    return f"""
    SELECT      PE.children, COUNT(person_id)
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        rating R ON PR.movie_id = R.id
    WHERE       R.mean_vote >= {min_rating} AND
                (PR.category = 'actor' OR PR.category = 'actress')
    GROUP BY    PE.children
    """

def query_3():
    return """
    SELECT      PE.name AS name, COUNT(G.genre) AS genres
    FROM        principal PR
    JOIN        person PE ON PR.person_id = PE.id
    JOIN        genre G ON G.movie_id = PR.movie_id
    WHERE       PR.category = 'writer'
    GROUP BY    PR.person_id
    ORDER BY    COUNT(G.genre) DESC
    LIMIT       10
    """
