from flask import Blueprint

home_route = Blueprint('api', __name__)

@home_route.route('/')
def hello_world():
    """
    Home route for health inspection
    this route return a Hello World! message
    ---
    """
    return {"message": "Hello World!"}, 200