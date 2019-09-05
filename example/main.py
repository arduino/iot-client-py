import iot_api_client as iot

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


CLIENT_ID = ""  # get a valid one from your Arduino Create account
CLIENT_SECRET = ""  # get a valid one from your Arduino Create account


if __name__ == "__main__":
    # Setup the OAuth2 session that'll be used to request the server an access token
    oauth_client = BackendApplicationClient(client_id=CLIENT_ID)
    token_url = "https://login.oniudra.cc/oauth/token"
    oauth = OAuth2Session(client=oauth_client)

    # This will fire an actual HTTP call to the server to exchange client_id and
    # client_secret with a fresh access token
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        audience="https://api.arduino.cc",
    )

    # If we get here we got the token, print its expiration time
    print("Got a token, expires in {} seconds".format(token.get("expires_in")))

    # Now we setup the iot-api Python client, first of all create a
    # configuration object. The access token goes in the config object.
    client_config = iot.Configuration(host="http://api-dev.arduino.cc/iot")
    client_config.debug = True
    client_config.access_token = token.get("access_token")

    # Create the iot-api Python client with the given configuration
    client = iot.ApiClient(client_config)

    # Each API model has its own wrapper, here we want to interact with
    # devices, so we create a DevicesV2Api object
    devices = iot.DevicesV2Api(client)

    # Get a list of devices, catching the specific exception
    try:
        resp = devices.devices_v2_list()
        print("Response from server:")
        print(resp)
    except iot.ApiException as e:
        print("An exception occurred: {}".format(e))
