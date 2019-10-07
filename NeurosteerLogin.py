import requests
import os


def login():
    userName = (os.environ["Neurosteer_user"])
    password = (os.environ["Neurosteer_pass"])
    url = "https://api.neurosteer.com/signin"
    r = requests.post("https://api.neurosteer.com/signin", data={'Content-type': 'application/x-www-form-urlencoded','email': userName, 'password': password})
    a = r.json()['url']
    start_of_token = a.find('access_token=')+len('access_token=')
    end_of_token = a.find('&user_data=')
    accessToken = a[start_of_token:end_of_token]

    start_of_bluetooth = a.find('bluetooth":"') + len('bluetooth":"')
    end_of_bluetooth = a.find('","email":')
    sensorID = a[start_of_bluetooth:end_of_bluetooth]

    return [accessToken, sensorID]



def logEvent(accessToken, sensorID, text):
    path = '/api/v1/sensors/'+sensorID+'/latest/events'
    url = 'https://api.neurosteer.com'+path
    data = {'Content-type':'application/x-www-form-urlencoded',}
    headers = {'path':path, 'authorization':'Bearer '+accessToken}
    data['description'] = text
    r = requests.post(url=url, json=data, headers = headers)
    print(r)
