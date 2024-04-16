import requests
from source.handle_env import load_env_variables

AUTH_ENDPOINT = "https://www.strava.com/oauth/token"


def get_token():

    env_params = load_env_variables()

    # Preparing the parameters to get access
    params = {
        'client_id': env_params['client_id'],
        'client_secret': env_params['client_secret'],
        'refresh_token': env_params['refresh_token'],
        'grant_type': 'refresh_token',
        'f': 'json'
    }

    # Getting the access token
    response = requests.post(AUTH_ENDPOINT, data=params, verify=False)
    access_token = response.json()['access_token']

    return access_token

