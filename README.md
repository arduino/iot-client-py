# Arduino iot-api Python client

## Requirements

* Python 3.7+

## Installation

You can install the package directly from Github (you may need to run `pip` with
`sudo`):

```sh
pip install arduino-iot-client
```

## Getting Started

### Authentication

The client requires a valid access token, you can use `requests-oauthlib` to get
one, to install the library do:

```sh
pip install requests-oauthlib
```

After installing the library you can use this Python code to get a token:

```python
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

oauth_client = BackendApplicationClient(client_id=YOUR_CLIENT_ID)
token_url = "https://api2.arduino.cc/iot/v1/clients/token"

oauth = OAuth2Session(client=oauth_client)
token = oauth.fetch_token(
    token_url=token_url,
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    include_client_id=True,
    audience="https://api2.arduino.cc/iot",
)

print(token.get("access_token"))
```

Once you get a token, you can create an instance of the iot-api client:

```python
import iot_api_client as iot
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration

# configure and instance the API client
client_config = Configuration(host="https://api2.arduino.cc/iot")
client_config.access_token = YOUR_ACCESS_TOKEN
client = iot.ApiClient(client_config)

# as an example, interact with the devices API
devices_api = iot.DevicesV2Api(client)

try:
    resp = devices_api.devices_v2_list()
    print(resp)
except ApiException as e:
    print("Got an exception: {}".format(e))
```

For a working example, see [the example folder](https://github.com/arduino/iot-client-py/tree/master/example/main.py) in this repo.

## How to get Arduino IoT Cloud Client Credentials

**NOTE:** Client Credentials are an Arduino IoT Cloud Maker Plan feature. Form more informations check the [Arduino Store](https://store.arduino.cc/digital/create).

You can generate Arduino IoT Cloud Client Credentials in the `ARDUINO API` section in the [IoT Cloud things dashobard](https://create.arduino.cc/iot/things):

### Step 1

![IoT Cloud Site](https://github.com/arduino/iot-client-js/blob/master/img/selection_1.png?raw=true)

### Step 2

![IoT Cloud Site](https://github.com/arduino/iot-client-js/blob/master/img/selection_2.png?raw=true)

### Step 3

![IoT Cloud Site](https://github.com/arduino/iot-client-js/blob/master/img/selection_3.png?raw=true)