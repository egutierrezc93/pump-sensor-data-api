# PUMP SENSOR DATA API

## Setup

### Prepare your environment

You will need to add the sensor.csv file in `./resources/sensor.csv` to this project to work.
The sensor.csv file can be downloaded from https://www.kaggle.com/datasets/nphantawee/pump-sensor-data/download?datasetVersionNumber=1

------------------------------------------------------------------------------------------

### Start the application

1. First install the required python packages
   `pip install -r requirements.txt`
2. Start the flask server
   `flask run`

------------------------------------------------------------------------------------------

## API endpoints documentation


### API home/health check endpoint

<details>
 <summary><code>GET</code> <code><b>/api/</b></code> <code>(Hello World! response endpoint for health check)</code></summary>

 ##### Responses

> | http code   | content-type          | response                      |
> |-------------|-----------------------|-------------------------------|
> | `200`       | `application/json`    | `{"message": "Hello World!"}` |

</details>


### Get filtered data from sensors

<details>
 <summary><code>GET</code> <code><b>/api/sensor-data/</b></code> <code>(get filtered data from sensors)</code></summary>

 ##### Description
 Sensor Data GET endpoint

   In this endpoint the dataset is loaded, filtered and filtered data is send in the response
   as a Json

   Filter criteria
   - Only data of april 2018
   - Only 07 and 47 sensors data
   - Only sensor measurements > 20 and < 30
 ##### Endpoint Responses

 > | http code   | content-type          | response                                 |
 > |-------------|-----------------------|------------------------------------------|
 > | `200`       | `application/json`    | `json object `                           |
 > | `500`       | `application/json`    |` {"message": "Internal Server Error"}`   |
 
 ##### Example Response
 ```json
 [
   {
      "date": "2018-04-19",
      "machine_status": "RECOVERING",
      "measure": 21.12992,
      "sensor": "sensor_07",
      "time": "09:09:00"
   },
   ...
 ]
 ```
</details>

### Get filtered data from sensors

<details>
 <summary><code>POST</code> <code><b>/api/sensor-data/</b></code> <code>(convert the request sensor data json to a pandas dataframe and print in console)</code></summary>

 ##### Description
 Sensor Data POST endpoint

   In this endpoint a json with sensor data is recieved in the same format of the GET endpoint, the json sensor data is converted to a pandas Dataframe and printed in console

##### Example Body
 ```json
 [
   {
      "date": "2018-04-19",
      "machine_status": "RECOVERING",
      "measure": 21.12992,
      "sensor": "sensor_07",
      "time": "09:09:00"
   },
   ...
 ]
 ```
 
 
 ##### Responses

 > | http code   | content-type          | response                                 |
 > |-------------|-----------------------|------------------------------------------|
 > | `200`       | `application/json`    | `{"message": "ok"} `                           |
 > | `500`       | `application/json`    |` {"message": "Internal Server Error"}`   |
 
</details>