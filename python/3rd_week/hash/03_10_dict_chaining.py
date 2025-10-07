class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

        return

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):  # LinkedTuple 로 초기화
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)

        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)

        return self.items[index].get(key)


linked_dict = LinkedDict()

linked_dict.put("77", "값")
linked_dict.put("333", "새로운 값")

print(linked_dict.get("77"))
print(linked_dict.get("333"))
