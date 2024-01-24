#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called."""

    @warps(method)
    def wrapper(self, *args, **kwargs):
        """Decorator to count how many times a method is called."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs & outputs for a particular function."""

    @warps(method)
    def wrapper(self, *args, **kwargs):
        """Create input and output list keys using the qualified name."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        output = method(*args, **kwargs)
        self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


class Cache:
    def __init__(self) -> None:
        """Create a Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the input data in Redis and returns the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, float]]] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieves data from Redis based on the key."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, None]:
        """Retrieves data from Redis as a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, bytes, None]:
        """Retrieves data from Redis as an integer."""
        return self.get(key, fn=int)
