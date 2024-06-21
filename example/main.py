from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import iot_api_client as iot
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration
import iot_api_client.apis.tags.things_v2_api as thingApi
import iot_api_client.apis.tags.properties_v2_api as propertiesApi
import iot_api_client.apis.tags.series_v2_api as seriesApi

import csv
from time import sleep

HOST = "https://api2.arduino.cc/iot"
TOKEN_URL = "https://api2.arduino.cc/iot/v1/clients/token"

client_id="<client-id>" # get a valid one from your Arduino account
client_secret="<client-secret-id>" # get a valid one from your Arduino account
org_id="<organization id - optional>"
extract_from="2024-06-03T00:00:00Z"
extract_to="2024-06-06T00:00:00Z"
filename="dump.csv"

def get_token():
    oauth_client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=oauth_client)
    token = oauth.fetch_token(
        token_url=TOKEN_URL,
        client_id=client_id,
        client_secret=client_secret,
        include_client_id=True,
        audience=HOST,
        headers={"X-Organization":org_id}
    )
    return token


def init_client(token):
    client_config = Configuration(HOST)
    client_config.access_token = token.get("access_token")
    if org_id!="":
        client = iot.ApiClient(client_config,header_name="X-Organization",header_value=org_id)
    else :
        client = iot.ApiClient(client_config)
    return client



def dump_property_data(series_api,thing_name,prop_name,thing_id,prop_id):
    sleep(1)
    print(f"Extracting property {thing_name}.{prop_name}")
    body={
        'resp_version':1,
        'requests': [ {'q': "property."+prop_id,'from':extract_from,'to':extract_to} ]
    }
    timeseries=series_api.series_v2_batch_query_raw(body)  
    
    if timeseries.response.status==200:
        data = timeseries.body['responses']
        for s in data:
            times = s['times']
            values = s['values']
            i=0
            while i<len(times):
                writer.writerow([thing_name,prop_name,times[i],values[i]])
                i=i+1
    else:
       print(f"Unable to extract data for property {prop_id}")
    

def get_things_and_props():
    token = get_token()
    client = init_client(token)
    things_api = thingApi.ThingsV2Api(client)
    properties_api = propertiesApi.PropertiesV2Api(client)
    series_api = seriesApi.SeriesV2Api(client)
    todolist=[]  #use this to track extractions to do    
    try:
        things = things_api.things_v2_list()
        
        if things.response.status==200:
            for thing in things.body: 
                sleep(5)
                tname=thing["name"]
                print(f"Found thing: {tname}")
                todo={}
                todo["thing_id"]=thing["id"]
                todo["thing_name"]=tname
                properties=properties_api.properties_v2_list(path_params={'id': thing["id"]})  
                for property in properties.body:
                    id = property["id"]
                    name = property["name"]
                    ptype = property["type"]
                    value = property["last_value"]
                    print(f"Property: {name}::{ptype}={value}")
                    if ptype=="FLOAT" or ptype=="INT":
                        todo["prop_id"]=id
                        todo["prop_name"]=name
                        todolist.append(todo.copy())
        else:
            print("IoT API returned status "+things.response.status)
    except ApiException as e:
        print("Exception: {}".format(e))

    while len(todolist)!=0:
        todo = todolist.pop()
        try:
            dump_property_data(series_api,todo["thing_name"],todo["prop_name"],todo["thing_id"],todo["prop_id"])
        except ApiException as e:
            print("Exception: {}".format(e))

#################

with open(filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["thing_name","variable","timestamp","value"])
    get_things_and_props()
