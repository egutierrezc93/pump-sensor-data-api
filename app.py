from flask import Flask
from api.route.home_route import home_route

def config_app() -> Flask:
    app:Flask = Flask(__name__)
    app.register_blueprint(home_route, url_prefix='/api')
    return app
    
app:Flask = config_app()