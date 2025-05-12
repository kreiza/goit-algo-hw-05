class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        for idx, (k, _) in enumerate(self.table[h]):
            if k == key:
                self.table[h][idx] = (key, value)
                return
        self.table[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

    def delete(self, key):
        h = self._hash(key)
        for idx, (k, _) in enumerate(self.table[h]):
            if k == key:
                del self.table[h][idx]
                print(f"[✓] Ключ '{key}' успішно видалено.")
                return True
        print(f"[!] Ключ '{key}' не знайдено.")
        return False


if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Dmytro")
    ht.insert("age", 22)
    print(ht.get("name"))
    ht.delete("name")
    print(ht.get("name"))
