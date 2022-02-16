#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)\
              AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/51.0.2704.103 Safari/537.36'}
    request = requests.get(url, allow_redirects=False, headers=header)
    if request.status_code != 200:
        print(None)
    else:
        children = request.json()['data']['children']
        for child in children:
            print(child['data']['title'])
