from flask import Flask


def create_app():
    app = Flask(__name__)

    from src import classifier

    app.register_blueprint(classifier.bp)
    app.add_url_rule('/', endpoint='index')

    return app


if __name__ == "__main__":
    create_app()