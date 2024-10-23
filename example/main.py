from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import iot_api_client as iot
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration
from iot_api_client.api import ThingsV2Api, PropertiesV2Api, SeriesV2Api
from iot_api_client.models import *

import csv
from time import sleep

HOST = "https://api2.arduino.cc"
TOKEN_URL = "https://api2.arduino.cc/iot/v1/clients/token"

client_id="<client-id>" # get a valid one from your Arduino account
client_secret="<client-secret-id>" # get a valid one from your Arduino account

org_id="<organization-id>" # (Optional) get a valid one from your Arduino account 
extract_from="2024-10-03T00:00:00Z"
extract_to="2024-10-06T00:00:00Z"
filename="dump.csv"

def get_token():
    oauth_client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=oauth_client)
    token = oauth.fetch_token(
        token_url=TOKEN_URL,
        client_id=client_id,
        client_secret=client_secret,
        include_client_id=True,
        audience="https://api2.arduino.cc/iot",
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


def dump_property_data(client,thing_name,prop_name,thing_id,prop_id):
    sleep(1)
    print(f"Extracting property {thing_name}.{prop_name}")
    series_api = SeriesV2Api(client)
    propertyRequest = BatchQueryRawRequestMediaV1(q="property."+prop_id, var_from=extract_from, to=extract_to)
    seriesRequest = BatchQueryRawRequestsMediaV1(resp_version=1, requests=[propertyRequest])
    timeseries=series_api.series_v2_batch_query_raw(seriesRequest)  
    
    try:
        for s in timeseries.responses:
            i=0
            while i<len(s.times):
                writer.writerow([thing_name,prop_name,s.times[i],s.values[i]])
                i=i+1

    except ApiException as e:
        print("Exception n series extraction: {}".format(e))


def get_things_and_props():
    token = get_token()
    client = init_client(token)
    things_api = ThingsV2Api(client)
    properties_api = PropertiesV2Api(client)
    todolist=[]  #use this to track extractions to do    
    
    try:
        things = things_api.things_v2_list()
        for thing in things:
            sleep(1)
            tname=thing.name
            print(f"Found thing: {tname}")
            todo={}
            todo["thing_id"]=thing.id
            todo["thing_name"]=tname
            properties=properties_api.properties_v2_list(id=thing.id, show_deleted=False)  
            for property in properties:
                name = property.name
                ptype = property.type
                value = property.last_value
                print(f"Property: {name}::{ptype}={value}")
                if ptype=="FLOAT" or ptype=="INT":
                    todo["prop_id"]=property.id
                    todo["prop_name"]=name
                    todolist.append(todo.copy())

    except ApiException as e:
        print("Exception: {}".format(e))

    while len(todolist)!=0:
        todo = todolist.pop()
        try:
            dump_property_data(client, todo["thing_name"], todo["prop_name"], todo["thing_id"], todo["prop_id"])
        except ApiException as e:
            print("Exception: {}".format(e))

#################

with open(filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["thing_name","variable","timestamp","value"])
    get_things_and_props()
