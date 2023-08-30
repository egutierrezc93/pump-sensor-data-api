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


