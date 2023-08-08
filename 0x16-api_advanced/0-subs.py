#/usr/bin/python3
""" number of subsribers in an api """
import requests

def number_of_subscribers(subreddit):
    """ number of subsribers in a Reddit API """
    headers = {'User-Agent': 'CustomUserAgent'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except (requests.RequestException, KeyError):
        return 0
