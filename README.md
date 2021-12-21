# DB-project

google docs:
https://docs.google.com/document/d/1hVN3kQrPuDw3GEbbd6vyaQantxwL1IQj-PLC-f6ZBpg/edit

Login to PuTTY and run:
ssh -L 3305:mysqlsrv1.cs.tau.ac.il:3306 adamkroskin@nova.cs.tau.ac.il

docs mysql python:
https://www.w3schools.com/python/python_mysql_getstarted.asp


Relations:  
best_picture_winners(id)  
movie(id, title, year, usa_gross_income)  
person(id, name, birthplace, children)  
principal(id, movie_id, person_id, category)  
rating(id, total_votes, mean_vote)  
genre(id, movie_id, genre)  


optimizations:  
keys, foreign keys  
index (movie.year, movie.usa_gross_income, person.children, rating.total_votes, rating.mean_vote, genre.genre, principal.category)  
double index??  
decomposition : BCNF/3NF?  
views  
