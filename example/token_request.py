# Base repository: https://github.com/arduino/iot-client-py
# This script generates the token needed to access to the Arduino IoT Cloud



from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# paste within the brackets the Client ID obtained from Arduino IoT Cloud 
YOUR_CLIENT_ID = "" 
# paste within the brackets the Secret ID obtained from Arduino IoT Cloud 
YOUR_CLIENT_SECRET = ""

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