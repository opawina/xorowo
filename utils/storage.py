from random import randint

from kivy.storage.jsonstore import JsonStore


class Storage(object):
    store = JsonStore('store.json')

    def get_all(self):
        # TODO 2 not needed yet
        print(self.store.keys())
        return self.store.keys()

    def get_random(self):
        count = self.store.count()
        if count <= 0:
            return None
        key = randint(1, self.store.count())
        return self.store.get(str(key))

    def put(self, value):
        self.store.put(str(self.store.count() + 1), val=value)

    def del_one(self, key):
        self.store.delete(key)

    # or guess the key/entry for a part of the key
    # for item in store.find(name='Gabriel'):