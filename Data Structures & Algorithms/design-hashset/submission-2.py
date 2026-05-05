class MyHashSet:

    def __init__(self):
        self.num_buckets = 9973
        self.data = [ [] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket = self.data[self._hash(key)]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.data[self._hash(key)]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.data[self._hash(key)]

        return key in bucket
    # def __init__(self):
    #     self.hash_set = []

    # def add(self, key: int) -> None:
    #     if key in self.hash_set:
    #         return
        
    #     self.hash_set.append(key)
        

    # def remove(self, key: int) -> None:
        
    #     if key in self.hash_set:
    #         self.hash_set.remove(key)
        

    # def contains(self, key: int) -> bool:
    #     return key in self.hash_set
          