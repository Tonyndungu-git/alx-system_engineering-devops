#!/usr/bin/python3
"""
using a recursive function to get a list
of hot articles.
"""
import requests

def recurse(subreddit, hot_list=None):
    """ titles of all hot articles for a given subreddit """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'CustomUserAgent'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            hot_posts = data['data']['children']
            for post in hot_posts:
                post_title = post['data']['title']
                hot_list.append(post_title)

            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list=hot_list)

        else:
            return None

    except requests.RequestException as e:
        print("An error occurred:", e)

    return hot_list
