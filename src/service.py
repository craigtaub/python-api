import requests

url = 'http://www.sportsbase.com/api/clubs?page=1'

def make_request():
    headers = {'Authorization': 'token="gCrjVTvNJUrumYeqHvwf7C8KMBxTqPCN"'}
    response = requests.get(url, headers=headers)
    print('API get 1st id:', response.json()["clubs"][0]['_id'])