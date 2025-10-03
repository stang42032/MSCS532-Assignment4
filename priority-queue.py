class PriorityQueue:
    def __init__(self):
        self.heap = []  # underlying list to store heap elements

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        # Fix heap property going upwards
        while i > 0 and self.heap[self._parent(i)][0] < self.heap[i][0]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        # Fix heap property going downwards
        largest = i
        left, right = self._left(i), self._right(i)

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def insert(self, priority, value):
        """
        Insert a new element with given priority.
        :param priority: Higher value means higher priority
        :param value: Data stored
        """
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """
        Removes and returns the element with the highest priority.
        """
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def peek(self):
        """
        Returns the element with the highest priority without removing it.
        """
        return self.heap[0] if self.heap else None

    def is_empty(self):
        """
        Check if the priority queue is empty.
        """
        return len(self.heap) == 0


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(3, "Low priority task")
    pq.insert(5, "Medium priority task")
    pq.insert(10, "High priority task")
    pq.insert(1, "Very low priority task")

    print("Top priority element:", pq.peek())  # Should print (10, "High priority task")

    while not pq.is_empty():
        print("Extracted:", pq.extract_max())
