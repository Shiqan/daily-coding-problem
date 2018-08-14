#!/usr/bin/env python
""" Problem 16 daily-coding-problem.com """
import abc
import redis

class Log:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def record(self, i: int) -> int:
        pass

    @abc.abstractmethod
    def get_last(self, i: int) -> int:
        pass

class RedisLog(Log):
    def __init__(self, host, port):
        self.r = redis.StrictRedis(host=host, port=port, db=0)
        super.__init__()

    def record(self, order_id: int):
        last_keys = self.r.get("last_keys")
        last_keys.append(order_id)
        self.r.set(last_keys)
        return self.r.set(order_id, order_id)

    def get_last(self, i: int):
        last_keys = self.r.get("last_keys")
        return last_keys[-i:]

class EcommerceAPI:
    def __init__(self, log: Log):
        self.log = log

    def record(self, order_id: int):
        return self.log.record(order_id)

    def get_last(self, i: int):
        return self.log.get_last(i)


if __name__ == "__main__":
    log = RedisLog('localhost', 6379)
    api = EcommerceAPI(log)

    api.record(1)
    api.get_last(1)
