#!/usr/bin/env python3
"""Implementation of an expiring web cache and tracker."""
import redis
import requests
from typing import Callable
from functools import wraps


redis = redis.Redis()


def count_sessions(method: Callable) -> Callable:
    """
    Decorator that counts how many requests have been made.
    Args:
        method (Callable): [description]
    Returns:
        Callable: [description]
    """

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function for decorator.
        Args:
            url (str): [description]
        Returns:
            str: [description]
        """
        redis.incr(f"count:{url}")
        cache = redis.get(f"cached:{url}")
        if not cache:
            cache = method(url)
            redis.setex(f"cached:{url}", 10, cache)
        return cache

    return wrapper


@count_sessions
def get_page(url: str) -> str:
    """
    Gets the HTML content of a web page.
    Args:
        url (str): [description]
    Returns:
        str: [description]
    """
    req = requests.get(url)
    return req.text


url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))  # Fetches from URL
# print(get_page(url))
# print(get_page(url))
