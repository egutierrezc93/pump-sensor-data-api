from flask import Request, Response
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
        sensor_df['yearmonth'] = sensor_df.timestamp.dt.strftime('%Y-%m')
        filtered_df:pd.DataFrame = sensor_df.loc[sensor_df.yearmonth == '2018-04']
        return filtered_df
    
    def __filter_sensor_data__(self, df:pd.DataFrame, sensor:str, min:int=20, max:int=30) -> pd.DataFrame:
        filtered_df:pd.DataFrame = df[['timestamp', sensor]]
        filtered_df = filtered_df.loc[filtered_df[sensor] < max]
        filtered_df = filtered_df.loc[filtered_df[sensor] > min]
        return filtered_df

    def get_filtered_sensor_data(self) -> Response:
        sensor_df:pd.DataFrame = self.__read_data_from_csv__()
        date_filtered_df:pd.DataFrame = self.__filter_by_date__(sensor_df)
        sensor_07_filtered_df:pd.DataFrame = self.__filter_sensor_data__(date_filtered_df, sensor='sensor_07')
        sensor_47_filtered_df:pd.DataFrame = self.__filter_sensor_data__(date_filtered_df, sensor='sensor_47')
        print('sensor_07_filtered_df ->', sensor_07_filtered_df)
        print('sensor_47_filtered_df ->', sensor_47_filtered_df)
        return {"message": "ok"}, 200