from flask import Flask


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)
    from home.views import home_app
    from demo.views import demo_app
    from recalc.views import recalc_app
    app.register_blueprint(home_app)
    app.register_blueprint(demo_app)
    app.register_blueprint(recalc_app)
    return app

