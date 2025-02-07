from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    # We are not trying to run the app in a test environment
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        #     "SQLALCHEMY_DATABASE_URI")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('RENDER_DATABASE_URI')
    # We are trying to test the app
    else:
        # Turns testing mode on
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models.book import Book
    from app.models.author import Author
    from app.models.genre import Genre
    from app.models.book_genre import BookGenre

    # Register Blueprints
    from .book_routes import books_bp
    app.register_blueprint(books_bp)

    from .author_routes import authors_bp
    app.register_blueprint(authors_bp)

    from .genre_routes import genres_bp
    app.register_blueprint(genres_bp)

    return app