class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))

class LinkedTuple:
    def __init__(self):
        self.items=[]

    def add(self, key, value):
        for i in range(len(self.items)):
            if self.items[i][0] == key:
                self.items[i] = (key, value)
                return
        self.items.append((key, value))

    def get(self, key):
        for k,v in self.items:
            if k == key:
                return v
        return None


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range (8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)