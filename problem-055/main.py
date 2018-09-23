#!/usr/bin/env python
""" Problem 55 daily-coding-problem.com """
import random
import string
import abc


class Storage:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set(self, url: str, short: str) -> str:
        pass

    @abc.abstractmethod
    def get(self, short: str) -> str:
        pass


class DictStorage(Storage):
    def __init__(self):
        self.mapping = {}
        self.reversed_mapping = {}

    def set(self, url, short):
        self.mapping[short] = url
        self.reversed_mapping[url] = short

    def get(self, short):
        if short in self.mapping:
            return self.mapping[short]


class UrlShortener:
    def __init__(self, storage: Storage, size=6):
        self.storage = storage
        self.size = size

    def shorten(self, url):
        if self.storage.get(url):
            return self.storage.get(url)

        short = ''.join(random.choices(string.ascii_lowercase + string.digits, k=self.size))
        self.storage.set(url, short)
        return short

    def restore(self, short):
        return self.storage.get(short)


if __name__ == "__main__":
    storage = DictStorage()
    url_shortener = UrlShortener(storage)
    assert "http://www.google.com" == url_shortener.restore(url_shortener.shorten("http://www.google.com"))
