class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next.next.val)
print(node1.next.next.next.val)

