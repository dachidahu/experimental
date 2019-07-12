
import collections

class Node(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None

#doublelinkedlist + hashmap
class LRU(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.d = {}
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1

        node = self.d[key]
        self._remove(key)
        self._add(node)
        return node.v

    def _add(self, node):

        prev = self.tail.prev
        node.next = self.tail
        node.prev = prev
        prev.next = node
        self.tail.prev = node
        self.d[node.k] = node

    def _remove(self, key):
        if key not in self.d:
            return
        node = self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.d[key]

    def put(self, key, val):
        self._remove(key)
        if len(self.d) >= self.cap:
            self._remove(self.head.next.k)
        node = Node(key, val)
        self._add(node)

class LRU2:
    def __init__(self, capacity):
        self.cnt = collections.defaultdict(int)
        self.cap = capacity
        self.q = collections.deque()
        self.d = {}

    def get(self, key):
        if key not in self.d:
            return -1
        self.cnt[key] += 1
        self.q.append(key)
        return self.d[key]

    def put(self, key, val):
        self.cnt[key] = 1
        self.q.append(key)
        self.d[key] = val
        while len(self.d) > self.cap:
            k = self.q.popleft()
            self.cnt[k] -= 1
            if self.cnt[k] == 0:
                del self.cnt[k]
                del self.d[k]




