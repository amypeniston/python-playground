class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_data(self, new_data):
        new_node = Node(new_data, self.head)
        self.head = new_node

    def delete_data(self, data_to_delete):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and not found:
            if current_node.data == data_to_delete:
                if previous_node == None:
                    self.head = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        if found:
            print("Data ({}) deleted.".format(data_to_delete))
        else:
            print("Delete Error. Data ({}) not found.".format(data_to_delete))

    def find_data(self, data_to_find):
        current_node = self.head
        counter = 1
        found = False
        while current_node and not found:
            if current_node.data == data_to_find:
                found = True
            else:
                current_node = current_node.next_node
                counter += 1
        if found:
            print("Data ({}) found at position {}.".format(data_to_find, counter))
        else:
            print("Data ({}) not found.".format(data_to_find))

    def print_list(self):
        print("---- Printing List ----")
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    
l = LinkedList()

l.add_data(8)
l.add_data(3)
l.add_data(5)
l.add_data(1)

l.print_list()

l.find_data(3)
l.find_data(22)

l.delete_data(1)
l.delete_data(9)

l.print_list()