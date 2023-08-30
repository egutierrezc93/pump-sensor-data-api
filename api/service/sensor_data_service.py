from flask import Request, Response, jsonify
import pandas as pd

class SensorDataService():

    request:Request

    def __init__(self, request:Request) -> None:
        self.request = request

    def __read_data_from_csv__(self) -> pd.DataFrame:
        raw_data:pd.DataFrame = pd.read_csv('./resources/sensor.csv')
        return raw_data
    
    def __filter_by_date__(self, df:pd.DataFrame, year:str='2018', month:str='04') -> pd.DataFrame:
        sensor_df:pd.DataFrame = df.copy()
        sensor_df.timestamp = pd.to_datetime(sensor_df.timestamp)
        sensor_df['date'] = sensor_df.timestamp.dt.strftime('%Y-%m-%d')
        sensor_df['time'] = sensor_df.timestamp.dt.strftime('%H:%M:%S')
        filtered_df = sensor_df.loc[sensor_df.date.str.startswith('2018-04')]
        return filtered_df
    
    def __filter_sensor_data__(self, df:pd.DataFrame, sensor:str, min:int=20, max:int=30) -> pd.DataFrame:
        filtered_df:pd.DataFrame = df[['date', 'time', sensor, 'machine_status']]
        filtered_df = filtered_df.loc[filtered_df[sensor] < max]
        filtered_df = filtered_df.loc[filtered_df[sensor] > min]
        filtered_df = filtered_df.rename({sensor: 'measure'}, axis='columns')
        filtered_df['sensor'] = sensor
        return filtered_df
    
    def __get_filtered_sensors_data__(self, df:pd.DataFrame) -> dict:
        sensor_07_filtered_df:pd.DataFrame = self.__filter_sensor_data__(df, sensor='sensor_07')
        sensor_47_filtered_df:pd.DataFrame = self.__filter_sensor_data__(df, sensor='sensor_47')
        filtered_sensor_data_df:pd.DataFrame = pd.concat([sensor_07_filtered_df, sensor_47_filtered_df])
        return filtered_sensor_data_df.to_dict('records')

    def get_filtered_sensor_data(self) -> Response:
        try:
            sensor_df:pd.DataFrame = self.__read_data_from_csv__()
            date_filtered_df:pd.DataFrame = self.__filter_by_date__(sensor_df)
            filtered_sensor_data_dict:dict = self.__get_filtered_sensors_data__(date_filtered_df)
            response:Response = jsonify(filtered_sensor_data_dict), 200
            return response
        except Exception as error:
            print('An exception ocurred in SensorDataService.get_filtered_sensor_data', error)
            return {"message": "Internal Server Error"}, 500