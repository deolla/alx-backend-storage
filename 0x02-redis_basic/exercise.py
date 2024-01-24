#!/usr/bin/env python3
"""Writing strings to Redis."""
import redis
import uuid


class Cache():
    """Create a Cache class"""
    def __init__(cls):
        cls._redis = redis.Redis()
        cls._redis.flushdb()

    def store(cls, data):
        """Returns a string"""
        random_key = str(uuid.uuid4())
        cls._redis.set(random_key, data)
        return random_key
