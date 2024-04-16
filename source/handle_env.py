import os
from dotenv import load_dotenv


def load_env_variables() -> dict:
    '''
    This function reads the parameters from the environment file
    '''
    # Loading the environment file
    load_dotenv()

    # Reading and saving the parameters from the environment file
    env_variables = {
        'client_id': os.environ.get('CLIENT_ID'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'refresh_token': os.environ.get('REFRESH_TOKEN')
    }

    # Returning the dictionary
    return env_variables
