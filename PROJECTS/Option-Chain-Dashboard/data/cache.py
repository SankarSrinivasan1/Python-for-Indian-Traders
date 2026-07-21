"""
cache.py
---------

Simple in-memory cache with automatic expiry.

Used to avoid making repeated NSE API requests within a
short period of time.

Author:
Sankar Srinivasan
"""

from datetime import datetime, timedelta
from threading import Lock


class Cache:
    """
    Simple TTL (Time To Live) cache.
    """

    def __init__(self):
        self._cache = {}
        self._lock = Lock()

    def set(self, key, value, ttl=30):
        """
        Store an object.

        Parameters
        ----------
        key : str
            Cache key

        value : any
            Object to cache

        ttl : int
            Time to live in seconds
        """

        expiry = datetime.now() + timedelta(seconds=ttl)

        with self._lock:
            self._cache[key] = {
                "value": value,
                "expiry": expiry
            }

    def get(self, key):
        """
        Retrieve cached object.

        Returns None if missing or expired.
        """

        with self._lock:

            if key not in self._cache:
                return None

            item = self._cache[key]

            if datetime.now() >= item["expiry"]:
                del self._cache[key]
                return None

            return item["value"]

    def exists(self, key):
        """
        Check whether a valid cache exists.
        """

        return self.get(key) is not None

    def remove(self, key):
        """
        Remove one cache entry.
        """

        with self._lock:
            self._cache.pop(key, None)

    def clear(self):
        """
        Remove all cache entries.
        """

        with self._lock:
            self._cache.clear()

    def cleanup(self):
        """
        Remove expired cache items.
        """

        now = datetime.now()

        with self._lock:

            expired = [
                key
                for key, value in self._cache.items()
                if value["expiry"] <= now
            ]

            for key in expired:
                del self._cache[key]

    def size(self):
        """
        Number of valid cache items.
        """

        self.cleanup()

        return len(self._cache)

    def keys(self):
        """
        List valid cache keys.
        """

        self.cleanup()

        return list(self._cache.keys())


# ---------------------------------------------------------
# Singleton cache instance
# ---------------------------------------------------------

cache = Cache()


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":

    cache.set("NIFTY", {"price": 25150}, ttl=10)

    print("Exists:", cache.exists("NIFTY"))

    print("Data:", cache.get("NIFTY"))

    print("Keys:", cache.keys())

    print("Size:", cache.size())

    cache.remove("NIFTY")

    print("After remove:", cache.exists("NIFTY"))
