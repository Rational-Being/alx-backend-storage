#!/usr/bin/env python3
"""

"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """

    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """

        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """

    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """

        """
        first = "".join([method.__qualname__, ":inputs"])
        second = "".join([method.__qualname__, ":outputs"])
        self._redis.rpush(first, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(second, str(out))
        return out
    return wrapper




class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        """

        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """

        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, key:str) -> str:
        """

        """
        #value = self.redis.get(key)
        return self.redis.get(key).decode("utf-8")

    def get_int(self: bytes) -> int:
        """

        """
        return int.from_bytes(self, sys.byteorder)
