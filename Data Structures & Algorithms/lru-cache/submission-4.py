class Node:
    def __init__(self, next = None, prev = None ,val = 0, key = -1) -> None:
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.begin = Node()
        self.end = Node()
        self.begin.next = self.end
        self.end.prev = self.begin
        self.map = {}

    def insert(self, node) -> None:
        node.next = self.end
        node.prev = self.end.prev
        
        self.end.prev.next = node
        self.end.prev = node

    def remove(self, node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if self.size < 1 or key not in self.map:
            return -1

        n = self.map[key]
        r = n.val

        self.remove(n)
        self.insert(n)

        return r

    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity:
            if key in self.map:
                n = self.map[key]
                n.val = value
                self.remove(n)
                self.insert(n)
            else:
                n = Node(val=value,key=key)
                self.map[key] = n
                
                self.insert(n)
                self.size += 1
        else:
            if key in self.map:
                n = self.map[key]
                n.val = value
                self.remove(n)
                self.insert(n)
            else:
                delNode = self.begin.next

                self.remove(delNode)
                del self.map[delNode.key]
                
                n = Node(val=value,key=key)
                self.map[key] = n
                self.insert(n)

                
                

        

        
