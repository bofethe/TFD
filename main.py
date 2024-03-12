import requests
import pandas as pd

# get initial dataframe
callurl = 'https://ncapps.tampagov.net/callsforservice/TFR/Json'
df = pd.read_json(callurl)

# function to also get vehicle that responded
def get_info(incident):
    url = f'https://ncapps.tampagov.net/callsforservice/TFR/GetAllEquipments?incidentNumber={incident}'
    infodic = requests.get(url).json()['data']
    equipment = [infodic[i]['vehicle_id'] for i in range(len(infodic))]
    return equipment

# Add vehicle to dataframe. Not very code effecient due to API limitations
df['Vehicle'] = df['Incident'].apply(get_info)