#!/usr/bin/env python3
"""

"""

import redis
import requests
from functools import wraps

rs = redis.Redis()

def wrap_request(method):
    """

    """
    @wraps(method)
    def wrapper(url):

        cached_resp = rs.get("cached:" + url)
        if cached_resp:
            return cached_resp.decode("utf-8")

        # rs.incr(f"count:{url}")
        # rs.set(f"cached:{url}", method(url))
        # rs.expire(f"cached:{url}", 10)
        rs.setex(f"cached:{url}", 10, method(url))

        return method(url)
    return wrapper

@wrap_request
def get_page(url: str) -> str:
    """

    """
    result = requests.get(url)
    return result.text
