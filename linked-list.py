class LinkedList:
    def __init__(self):

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def interrogate(self):
        print("Node contains {}. Next node is {}.".format(self.data, self.next_node))

n1 = Node(2)
n2 = Node(5)
n2.next_node = n1

n1.interrogate()
n2.interrogate()