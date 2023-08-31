from flask import Blueprint, request

from api.service.sensor_data_service import SensorDataService

sensor_data_route = Blueprint('/sensor_data_route', __name__)

@sensor_data_route.route('/', methods = ['GET'])
def get_filtered_sensor_data():
    """
    Sensor Data GET endpoint
    In this endpoint the dataset is loaded, filtered and filtered data is send

    Filter criteria
    - Only data of april 2018
    - Only 07 and 47 sensors data
    - Only sensor measurements > 20 and < 30
    ---
    """
    service:SensorDataService = SensorDataService(request)
    return service.get_filtered_sensor_data()

@sensor_data_route.route('/', methods = ['POST'])
def print_sensor_data_as_dataframe(): 
    """
    Sensor Data POST endpoint
    In this endpoint a json with sensor data is recieved in the same format
    of the GET endpoint, the json sensor data is converted to a pandas 
    Dataframe and printed in console
    ---
    """
    service:SensorDataService = SensorDataService(request)
    return service.print_sensor_data_as_dataframe()