import requests

ACTIVITY_ENDPOINT = 'https://www.strava.com/api/v3/athlete/activities'


def get_activity_data(access_token, params) -> dict:

    # Preparing headers
    headers = {'Authorization': f'Bearer {access_token}'}

    # Getting the data and storing it in a json file
    response = requests.get(ACTIVITY_ENDPOINT, headers=headers, params=params)
    activity_data = response.json

    return activity_data