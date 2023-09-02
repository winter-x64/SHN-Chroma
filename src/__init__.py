from flask import Flask


def mainApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'This is a secret key'

    # import for the blueprints
    from .views.home import home

    # blueprint mapping for the web application
    app.register_blueprint(home, url_prefix='/')

    return app