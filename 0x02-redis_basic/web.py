#!/usr/bin/env python3
"""Implementation of an expiring web cache and tracker."""
import redis
import requests
import time
from typing import Callable
from functools import wraps

redis_ = redis.StrictRedis()


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
        redis_.incr(f"count:{url}")
        cache = redis_.get(f"cached:{url}")
        if not cache:
            cache = method(url)
            redis_.setex(f"cached:{url}", 10, cache)
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
    max_retries = 3
    for attempt in range(max_retries):
        try:
            req = requests.get(url)
            return req.text
        except requests.exceptions.ConnectionError as e:
            print(f"Error accessing URL: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in 2 seconds (attempt {attempt + 2}/{max_retries})...")
                time.sleep(2)
            else:
                print("Max retries exceeded. Unable to access the URL.")
                return "Error: Unable to access the URL"


slow_url = "https://www.ilovepdf."
print(get_page(slow_url))
print(redis_.get(f"count:{slow_url}"))
