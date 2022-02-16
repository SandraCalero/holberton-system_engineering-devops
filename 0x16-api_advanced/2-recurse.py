#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing the titles of all hot
articles for a given subreddit. If no results are found for the given
subreddit, the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)\
              AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/51.0.2704.103 Safari/537.36'}
    request = requests.get(url, allow_redirects=False, headers=header)
    if request.status_code != 200:
        return None
    else:
        data = request.json()['data']
        after = data['after']
        for child in data['children']:
            hot_list.append(child['data']['title'])
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
