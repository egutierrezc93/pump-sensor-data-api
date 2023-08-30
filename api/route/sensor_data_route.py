from flask import Blueprint, request

from api.service.sensor_data_service import SensorDataService

sensor_data_route = Blueprint('/sensor_data_route', __name__)

@sensor_data_route.route('/', methods = ['GET'])
def get_filtered_sensor_data():
    """
    Home route for health inspection
    this route return a Hello World! message
    ---
    """
    service:SensorDataService = SensorDataService(request)
    return service.get_filtered_sensor_data()