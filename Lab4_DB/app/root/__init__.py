from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .movie_route import movie_bp
    from .boxoffice_route import boxoffice_bp
    from .review_route import review_bp

    app.register_blueprint(movie_bp)
    app.register_blueprint(boxoffice_bp)
    app.register_blueprint(review_bp)
