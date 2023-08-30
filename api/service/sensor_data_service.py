from flask import Request, Response
import pandas as pd

class SensorDataService():

    request:Request

    def __init__(self, request:Request) -> None:
        self.request = request

    def __read_data_from_csv__(self) -> pd.DataFrame:
        raw_data:pd.DataFrame = pd.read_csv('./resources/sensor.csv')
        return raw_data

    def get_filtered_sensor_data(self) -> Response:
        print(self.__read_data_from_csv__())
        return {"message": "ok"}, 200