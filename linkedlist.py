class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<ListNode {repr(self.value)} -> {str(self.next)}>"


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return f'''ListNode {repr(self.head.value if self.head else None)} -> {str(self.head.next if self.head else None)}'''

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(str(current_node.value), end="")

            current_node = current_node.next


class Stack(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if self.head.next:
            popped_node = self.head
            self.head = self.head.next

            return popped_node

    def push(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        return self.head

    def peek(self):
        return self.head


class Queue(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = ListNode(value)

        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        dequeue_node = self.head

        self.head = dequeue_node.next

        return dequeue_node

    def front(self):
        return self.head


stack = Stack()
queue = Queue()

stack.push(1)
queue.enqueue(1)

stack.push(2)
queue.enqueue(2)

stack.push(3)
queue.enqueue(3)

stack.pop()
queue.dequeue()

print(stack)
print(queue)

'''
Given three values return a new linkedlist containing these values
Wrap values in ListNode Class
Input Values -> integer

'''


def solution(a, b, c):
    node_a = ListNode(a)
    node_b = ListNode(b)
    node_c = ListNode(c)

    node_a.next = node_b
    node_b.next = node_c

    return node_a
