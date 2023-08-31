from flask import Blueprint

home_route = Blueprint('home_route', __name__)

@home_route.route('/')
def hello_world():
    """
    Home route for health check
    this route return a Hello World! message
    ---
    """
    return {"message": "Hello World!"}, 200