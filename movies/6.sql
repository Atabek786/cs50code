 SELECT AVG(rating) FROM ratings
   ...> (SELECT year FROM movies WHERE year = '2012');