CREATE TABLE IF NOT EXISTS movie (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    year INTEGER,
    director TEXT,
    cover TEXT
);

CREATE TABLE IF NOT EXISTS actor (
    id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    name TEXT,
    FOREIGN KEY (movie_id) REFERENCES movie (id)
);