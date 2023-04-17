from flask import Blueprint, request, render_template
from movieswebsite.db import get_movies

bp = Blueprint('movies', __name__, url_prefix='/movies')

# https://werkzeug.palletsprojects.com/en/2.0.x/routing/
# Rules that end with a slash are “branches”, others are “leaves”. 
# If strict_slashes is enabled (the default), 
# visiting a branch URL without a trailing slash will redirect to the URL with a slash appended.
@bp.route('/', methods=['GET'], strict_slashes=False)
def movie_list():
    movies = get_movies()
    return render_template('movies.html', movies=movies)