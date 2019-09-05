# Arduino iot-api Python client

## Requirements

* Python 3.7+

## Installation

You can install the package directly from Github (you may need to run `pip` with
`sudo`):

```sh
pip install git+https://github.com/Arduino/iot-api-client-py.git
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
token_url = "https://login.oniudra.cc/oauth/token"

oauth = OAuth2Session(client=oauth_client)
token = oauth.fetch_token(
    token_url=token_url,
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    audience="https://api.arduino.cc",
)

print(token.get("access_token"))
```

Once you get a token, you can create an instance of the iot-api client:

```python
import iot_api_client
from iot_api_client.rest import ApiException

# configure and instance the API client
client_config = Configuration(host="http://api-dev.arduino.cc/iot")
client_config.access_token = YOUR_ACCESS_TOKEN
client = iot.ApiClient(client_config)

# as an example, interact with the devices API
devices_api = iot.DevicesV2Api(client)

try:
    resp = devices_api.devices_v2_list()
    print(resp)
except iot.ApiException as e:
    print("Got an exception: {}".format(e))
```

For a working example, see [the example folder](./example) in this repo.
