class Node:
    def __init__(self, val=None):
        self.prev = None
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class DoublyLinkedList:
    def __init__(self):
        self.header = Node()
        self.tail = Node()
        self.tail.prev = self.header
        self.header.next = self.tail
        self.size = 0

    def __repr__(self):
        return str(self.get_items())

    def __getitem__(self, item):
        index = 0
        current_node = self.header.next
        while current_node:
            if index == item:
                return current_node
            current_node = current_node.next
            index += 1
        return None

    def add_right(self, val):
        node = Node(val)
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def add_left(self, val):
        node = Node(val)
        first_node = self.header.next
        self.header.next = node
        node.prev = self.header
        node.next = first_node
        first_node.prev = node
        self.size += 1

    def del_head(self):
        if self.size == 0:
            return 0
        self.header.next = self.header.next.next
        self.size -= 1
        return 1

    def del_tail(self):
        if self.size == 0:
            return 0
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return 1

    def is_empty(self):
        return self.size == 0

    def search(self, kw):
        index = 0
        current_node = self.header.next
        while current_node:
            if current_node.val == kw:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def insert(self, pos, val):
        if not (0 <= pos <= self.size):
            return None
        if pos == 0:
            self.add_left(val)
            return
        if pos == self.size:
            self.add_right(val)
            return
        index = 0
        current_node = self.header.next
        node = Node(val)
        while current_node:
            if pos == index:
                prev_node = current_node.prev
                prev_node.next = node
                node.prev = prev_node
                node.next = current_node
                current_node.prev = node
                self.size += 1
                break
            current_node = current_node.next
            index += 1

    def get_items(self):
        res = []
        current_node = self.header
        while current_node:
            res.append(current_node.val)
            current_node = current_node.next

        return res
