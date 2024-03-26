import requests
from datetime import date

pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = 'abcdefggege'
USERNAME = 'sameer77'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'minutes',
    'type': 'float',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = date.today()
today = str(today)
today = today.replace('-','')

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}'
pixel_config = {
    'date': today,
    'quantity': '45',
}

response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
