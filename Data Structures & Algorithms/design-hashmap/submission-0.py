class MyHashMap:

    def __init__(self):
        self.num_buckets = 9973
        self.data = [ [] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        bucket = self.data[self._hash(key)]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # overwrites the existing key
                return
        # runs only if we did not find the key
        bucket.append((key, value))

        

    def get(self, key: int) -> int:
        bucket = self.data[self._hash(key)]

        for k, v in bucket:
            if k == key:
                return v
        
        return -1

        
        
    def remove(self, key: int) -> None:
        bucket = self.data[self._hash(key)]
        new_bucket = []

        for k, v in bucket:
            if k != key:
                new_bucket.append((k, v))

        self.data[self._hash(key)] = new_bucket



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)