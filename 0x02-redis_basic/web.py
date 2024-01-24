#!/usr/bin/env python3
"""Implementation of an expiring web cache and tracker."""
import redis
import requests
from typing import Callable
from functools import wraps


def count_requests(method: Callable) -> Callable:
    """Decorator that counts how many requests have been made."""

    @wraps(method)
    def wrapper(url):
        """Wrapper function for decorator."""
        redis.incr(f"count:{url}")
        page = redis.get(f"cached:{url}")
        if not page:
            page = method(url)
            redis.setex(f"cached:{url}", 10, page)
        return page

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Gets the HTML content of a web page."""
    return requests.get(url).text
