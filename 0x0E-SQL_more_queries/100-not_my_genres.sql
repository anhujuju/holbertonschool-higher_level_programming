-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name AS name
FROM tv_genres
WHERE name NOT IN
(SELECT name
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter")
ORDER BY name;