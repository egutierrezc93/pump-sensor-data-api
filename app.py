from flask import Flask
from api.route.home_route import home_route
from api.route.sensor_data_route import sensor_data_route

def config_app() -> Flask:
    """
    Flask server configuration function
    Here blueprint is implemented for the two routes that the
    server has
     - home route: single endpoint for health check
     - sensor data route: the challenge endpoints are impelemented here
    ---
    """
    app:Flask = Flask(__name__)
    app.register_blueprint(home_route, url_prefix='/api')
    app.register_blueprint(sensor_data_route, url_prefix='/api/sensor-data')
    return app
    
app:Flask = config_app()