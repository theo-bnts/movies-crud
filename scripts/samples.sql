INSERT INTO movie (title, description, year, director, cover) VALUES ('The Godfather', 'Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.', 1972, 'Francis Ford Coppola', '87bc05dc-16e6-4830-aff8-89e369653567.jpg');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Godfather'), 'Marlon Brando');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Godfather'), 'Al Pacino');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Godfather'), 'James Caan');

INSERT INTO movie (title, description, year, director, cover) VALUES ('The Lord of the Rings: The Return of the King', 'Gandalf and Aragorn lead the World of Men against Sauron''s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.', 2003, 'Peter Jackson', 'd5a7cb49-c37d-4a65-8655-9d80017e399a.jpg');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Return of the King'), 'Elijah Wood');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Return of the King'), 'Viggo Mortensen');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Return of the King'), 'Ian McKellen');

INSERT INTO movie (title, description, year, director, cover) VALUES ('Pulp Fiction', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 1994, 'Quentin Tarantino', '086f62dd-c6ed-475e-b2d3-9da72658a28b.jpg');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Pulp Fiction'), 'John Travolta');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Pulp Fiction'), 'Uma Thurman');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Pulp Fiction'), 'Samuel L. Jackson');

INSERT INTO movie (title, description, year, director, cover) VALUES ('The Lord of the Rings: The Fellowship of the Ring', 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', 2001, 'Peter Jackson', 'b466ccda-bc41-444e-bfa2-0b051c7c0bf1.jpg');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Fellowship of the Ring'), 'Elijah Wood');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Fellowship of the Ring'), 'Ian McKellen');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'The Lord of the Rings: The Fellowship of the Ring'), 'Orlando Bloom');

INSERT INTO movie (title, description, year, director, cover) VALUES ('Fight Club', 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.', 1999, 'David Fincher', '27c30688-41a1-4c8c-9d86-e795f2b381ea.jpg');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Fight Club'), 'Brad Pitt');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Fight Club'), 'Edward Norton');
INSERT INTO actor (movie_id, name) VALUES ((SELECT id FROM movie WHERE title = 'Fight Club'), 'Meat Loaf');