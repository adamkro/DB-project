SELECT ranks.title, ranks.genre, ranks.rate
FROM 	(
	    SELECT      M.title AS title, G.genre AS genre, R.mean_vote AS rate,
	    				 ROW_NUMBER() OVER (PARTITION BY G.genre ORDER BY R.mean_vote DESC) AS movieRank
	    FROM        (SELECT *
	                 FROM movie
	                 WHERE YEAR = 1973) M
	    JOIN        genre G ON M.id = G.movie_id
	    JOIN        rating R ON M.id = R.id
	    WHERE       R.total_votes >= 1250
		) AS ranks
WHERE ranks.movieRank = 1