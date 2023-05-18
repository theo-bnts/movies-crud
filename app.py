from flask import Flask, request, make_response, render_template, redirect
import os
import sqlite3
import cv2
import base64
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_get():
    connection = sqlite3.connect('./databases/database.db')
    cursor = connection.cursor()

    def base64_cover_with_faces(original_image_path):
        image = cv2.imread(original_image_path)

        three_channels_image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

        image_height, image_width, _ = image.shape

        thickness = int(image_width / 200)

        if image_width > 2000 or image_height > 2000:
            scale = 2000 / max(image_width, image_height)

            image_width = int(image_width * scale)
            image_height = int(image_height * scale)

            three_channels_image = cv2.resize(three_channels_image, (image_width, image_height))
        else:
            scale = 1

        detector = cv2.FaceDetectorYN.create(
            model = './models/face_detection_yunet_2022mar.onnx',
            config = '',
            input_size = (image_width, image_height),
            score_threshold = 0.9,
            nms_threshold = 0.3,
            top_k = 5000,
            backend_id = 0,
            target_id = 0
        )

        faces = detector.detect(three_channels_image)
        faces = faces[1]

        if not faces is not None:
            return None

        for (index, face) in enumerate(faces):
            x, y, w, h = int(face[0] / scale), int(face[1] / scale), int(face[2] / scale), int(face[3] / scale)
            color = (255, 205, 25)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

        _, image_buffer = cv2.imencode('.jpg', image)
        base64_image_buffer = base64.b64encode(image_buffer).decode('utf-8')

        return base64_image_buffer
    
    def get_actors(movie_id):
            sql = '''
                SELECT name
                FROM actor
                WHERE movie_id = ?
            '''

            actors = cursor.execute(sql, (movie_id, )).fetchall()

            actors = [actor[0] for actor in actors]

            return actors
    
    def get_movies():
        sql = '''
            SELECT id, title, description, year, director, cover
            FROM movie
        '''

        movies = cursor.execute(sql).fetchall()

        for index in range(len(movies)):
            movie = {
                'id': movies[index][0],
                'title': movies[index][1],
                'description': movies[index][2],
                'year': movies[index][3],
                'director': movies[index][4],
                'actors': get_actors(movies[index][0]),
                'cover': base64_cover_with_faces('./static/images/' + movies[index][5])
            }

            movies[index] = movie

        return movies
    
    movies = get_movies()
    
    connection.close()
      
    return render_template('list.jinja', movies=movies)

@app.route('/movie/new', methods=['GET'])
def new_get():
    return render_template('new-edit.jinja')

@app.route('/movie/new', methods=['POST'])
def new_post():
    connection = sqlite3.connect('./databases/database.db')
    cursor = connection.cursor()

    def insert_cover():
        cover = request.files['cover']

        cover.filename = str(uuid.uuid4()) + '.' + cover.filename.split('.')[-1]

        cover.save('./static/images/' + cover.filename)

        return cover.filename

    def insert_movie():
        sql = '''
            INSERT INTO movie (title, description, year, director, cover)
            VALUES (?, ?, ?, ?, ?)
        '''

        cursor.execute(sql, (request.form['title'], request.form['description'], request.form['year'], request.form['director'], insert_cover()))

        return cursor.lastrowid

    def insert_actors(movie_id):
        index = 1
        while (actor := request.form['actor_' + str(index)]) != '':
            sql = '''
                INSERT INTO actor (name, movie_id)
                VALUES (?, ?)
            '''

            cursor.execute(sql, (actor, movie_id))

            index += 1

    movie_id = insert_movie()
    insert_actors(movie_id)

    connection.commit()
    connection.close()

    return redirect('/')

@app.route('/movie/<int:movie_id>/edit', methods=['GET'])
def edit_get(movie_id):
    connection = sqlite3.connect('./databases/database.db')
    cursor = connection.cursor()

    def get_movie(movie_id):
        sql = '''
            SELECT title, description, year, director, cover
            FROM movie
            WHERE id = ?
        '''

        movie = cursor.execute(sql, (movie_id, )).fetchone()

        return movie[0], movie[1], movie[2], movie[3], movie[4]

    def get_actors(movie_id):
        sql = '''
            SELECT name
            FROM actor
            WHERE movie_id = ?
        '''

        actors = cursor.execute(sql, (movie_id, )).fetchall()

        actors = [actor[0] for actor in actors]

        return actors

    def base64_cover(filename):
        image = cv2.imread('./static/images/' + filename)

        _, image_buffer = cv2.imencode('.jpg', image)

        base64_image_buffer = base64.b64encode(image_buffer).decode('utf-8')

        return base64_image_buffer

    title, description, year, director, cover_filename = get_movie(movie_id)
    actors = get_actors(movie_id)
    cover = base64_cover(cover_filename)

    return render_template('new-edit.jinja', id=movie_id, title=title, description=description, year=year, director=director, actors=actors, cover=cover)

@app.route('/movie/<int:movie_id>/edit', methods=['POST'])
def edit_post(movie_id):
    connection = sqlite3.connect('./databases/database.db')
    cursor = connection.cursor()

    def update_cover(movie_id):
        cover = request.files['cover']

        if cover.filename == '':
            return

        cover.filename = str(uuid.uuid4()) + '.' + cover.filename.split('.')[-1]

        cover.save('./static/images/' + cover.filename)

        sql = '''
            UPDATE movie
            SET cover = ?
            WHERE id = ?
        '''

        cursor.execute(sql, (cover.filename, movie_id))

    def update_actors(movie_id):
        sql = '''
            DELETE FROM actor
            WHERE movie_id = ?
        '''

        cursor.execute(sql, (movie_id, ))

        index = 1
        while (actor := request.form['actor_' + str(index)]) != '':
            sql = '''
                INSERT INTO actor (name, movie_id)
                VALUES (?, ?)
            '''

            cursor.execute(sql, (actor, movie_id))

            index += 1
    
    def update_movie(movie_id):
        sql = '''
            UPDATE movie
            SET title = ?, description = ?, year = ?, director = ?
            WHERE id = ?
        '''

        cursor.execute(sql, (request.form['title'], request.form['description'], request.form['year'], request.form['director'], movie_id))

    update_movie(movie_id)
    update_cover(movie_id)
    update_actors(movie_id)

    connection.commit()
    connection.close()

    return redirect('/')

@app.route('/movie/<int:id>/delete', methods=['GET'])
def delete(id):
    connection = sqlite3.connect('./databases/database.db')
    cursor = connection.cursor()

    sql = '''
        DELETE FROM movie
        WHERE id = ?
    '''

    cursor.execute(sql, (id, ))

    connection.commit()
    connection.close()

    return redirect('/')