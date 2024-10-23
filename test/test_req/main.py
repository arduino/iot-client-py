import os

import iot_api_client
from iot_api_client.rest import ApiException
import  iot_api_client.apis.tags.devices_v2_api as DevicesV2

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

CLIENT_ID = os.getenv("CLIENT_ID")  # get a valid one from your Arduino Create account
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # get a valid one from your Arduino Create account


if __name__ == "__main__":
    # Setup the OAuth2 session that'll be used to request the server an access token
    oauth_client = BackendApplicationClient(client_id=CLIENT_ID)
    token_url = "https://api2.arduino.cc/iot/v1/clients/token"
    oauth = OAuth2Session(client=oauth_client)

    # This will fire an actual HTTP call to the server to exchange client_id and
    # client_secret with a fresh access token
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        include_client_id=True,
        audience="https://api2.arduino.cc/iot",
    )

    # If we get here we got the token, print its expiration time
    print("Got a token, expires in {} seconds".format(token.get("expires_in")))

    # Now we setup the iot-api Python client, first of all create a
    # configuration object. The access token goes in the config object.
    client_config = iot_api_client.Configuration(host = "https://api2.arduino.cc")
    # client_config.debug = True
    client_config.access_token = token.get("access_token")

    # Create the iot-api Python client with the given configuration
    api_client = iot_api_client.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    api_instance = DevicesV2.DevicesV2Api(api_client)

    # Get a list of devices, catching the specific exception
    try:
        resp = api_instance.devices_v2_list()
        print("Response from server:")
        print(resp)
    except ApiException as e:
        print("An exception occurred: {}".format(e))
