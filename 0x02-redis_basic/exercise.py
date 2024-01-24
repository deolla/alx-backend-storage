#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def call_history(method: Callable) -> Callable:
        """Store the history of inputs & outputs for a particular function."""
        def wrapper(*args, **kwargs):
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"

            redis_client.rpush(inputs_key, repr(args))
            output = method(*args, **kwargs)
            redis_client.rpush(outputs_key, str(output))
            return output
        return wrapper
