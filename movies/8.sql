SELECT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies WHERE title = "Toy Story";