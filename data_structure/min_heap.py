class MinHeap:

    def __init__(self):
        self.items = [0]
        self.current_size = 0
        self.Root = 1

    def _parent(self, pos: int):
        return pos // 2

    def _left(self, pos: int):
        return (2 * pos)

    def _right(self, pos: int):
        return (2 * pos) + 1

    def getMin():
        if not self.items:
            return None
        return self.items[self.Root]
    
    def _swap(self, i: int, j: int):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def remove(self):
        root = self.items[self.Root]
        self.items[self.Root] = self.items[self.current_size]
        self.items.pop()
        self.current_size -= 1
        self._heapify(self.Root)
        return root

    def _heapify(self, i: int):
        _min = i
        left = self._left(i)
        right = self._right(i)
        print(i, left, right)
        if left <= self.current_size and self.items[left] < self.items[_min]:
            _min = left
        if right <= self.current_size and self.items[right] < self.items[_min]:
            _min = right
        if _min != i:
            self._swap(_min, i)
            self._heapify(_min)

    def insert(self, k: int):
        self.items.append(k)
        self.current_size += 1
        current = self.current_size
        while (self.items[current] < self.items[self._parent(current)]):
            if current == 0:
                break
            self._swap(current, self._parent(current))
            current = self._parent(current)
