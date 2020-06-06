import redis
import json
import traceback
import time

class redis_server():

    def __init__(self):
        self.wait = 0
        self.connect_redisServer()

    def connect_redisServer(self):

        try:
            self.r_server = redis.Redis('localhost', port=6379, db=0)
            self.check_connection()
        except redis.RedisError as e:
            print("Exception occurred while connecting with redis on 6379 port error is :-",e)

    def check_connection(self):

        try:
            print(self.wait)
            self.r_server.client_list()
        except redis.RedisError:
            if redis.ConnectionError:
                if self.wait < 3:
                    self.wait += 1
                    time.sleep(5)
                    self.connect_redisServer()
                else:
                    print("Connection error occurred while connection to redis")
            else:
                print("Error occurred in check_connection redis error is :-",redis.RedisError)

    def set_data(self, *args, **kwargs):
        """
        set value against the given key
        """
        key = args[0]
        value = args[1]
        print("*WARN* set data", key)
        print("*WARN* set data", value)
        self.r_server.set(key, json.dumps(value))
        #self.r_server.set(key, value)
        return True

    def get_data(self, *args, **kwargs):
        """
        get value against the given key
        """
        key = args[0]
        print("*WARN* redisget data", key)
        return self.r_server.get(key)

    def set_list(self, key, value):
        if not self.r_server.lpushx(key, value):
            self.r_server.lpush(key, value)

    def get_list(self, key):
        return self.r_server.lrange(key, 0, -1)

    def set_hash(self, name, key, value):
        self.r_server.hset(name, key, value)

    def get_hash(self, name, key):
        return self.r_server.hget(name, key)

    def get_all_hash(self, name):
        return self.r_server.hgetall(name)

    def del_hash(self, name, key):
        return self.r_server.hdel(name, key)

    def rm_list(self, key, value, count=0):
        return self.r_server.lrem(key, count, value)

    def del_data(self, key):
        return self.r_server.delete(key)

    def flush(self):
        return self.r_server.flushall()


if __name__ == "__main__":
    r=redis_server()
    #r.set_data("name1", "brijesh")
    r.set_hash("user", "name", "brijesh")
    r.set_hash("user", "age", "25")
    print(r.del_hash("user", "name"))
    print(r.get_all_hash("user"))
    r.flush()
    #print(r.get_list("name"))
    #r.rm_list("name", "chaudhary")
    #r.del_data("name1")
