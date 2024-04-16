from source.authorize import get_token
from source.get_data import get_activity_data

import pandas as pd
from datetime import datetime
import json

ACTIVITIES_PER_PAGE = 200
PAGE_NUMBER = 1
PARAMS = {
    'per_page': ACTIVITIES_PER_PAGE,
    'page': PAGE_NUMBER
}

def main():
    token = get_token()
    data = get_activity_data(token, params=PARAMS)
    df = pd.json_normalize(data)
    timestamp = datetime.now().strftime('%d%m%Y')
    filepath = f'data/{timestamp}_activitydata.csv'
    df.to_csv(filepath, index=False)


if __name__ == '__main__':
    main()