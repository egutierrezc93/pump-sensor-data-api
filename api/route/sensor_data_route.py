from flask import Blueprint, request

from api.service.sensor_data_service import SensorDataService

sensor_data_route = Blueprint('/sensor_data_route', __name__)

@sensor_data_route.route('/', methods = ['GET'])
def get_filtered_sensor_data():
    """
    Sensor Data GET endpoint
    In this endpoint the dataset is uploaded, filtered and filtered data is send

    Filter criteria
    - Only data of april 2018
    - Only 07 and 47 sensors data
    - Only sensor measurements > 20 and < 30
    ---
    """
    service:SensorDataService = SensorDataService(request)
    return service.get_filtered_sensor_data()