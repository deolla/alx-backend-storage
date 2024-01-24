#!/usr/bin/env python3
"""Implement a get_page function"""

import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Count the number of requests"""

    @wraps(method)
    def wrapper(url):
        """Wrapper function for decorator"""
        r.incr(f"count:{url}")
        caches = r.get(f"cached:{url}")
        if caches:
            return caches.decode("utf-8")
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and returns it"""
    req = requests.get(url)
    return req.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
