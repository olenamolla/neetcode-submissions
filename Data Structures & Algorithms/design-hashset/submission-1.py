class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        if key in self.hash_set:
            return
        
        self.hash_set.append(key)
        

    def remove(self, key: int) -> None:
        
        if key in self.hash_set:
            self.hash_set.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hash_set
          