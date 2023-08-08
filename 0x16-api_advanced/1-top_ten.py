#!/usr/bin/python3
""" the titles of the first 10 hot posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    headers = {'User-Agent': 'CustomUserAgent'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            top_10_posts = data['data']['children'][:10]
            for post in top_10_posts:
                post_title = post['data']['title']
                print(post_title)
        else:
            print("None")

    except requests.RequestException as e:
        print("An error occurred:", e)
