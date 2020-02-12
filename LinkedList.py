# Linked List class contains a Node object
from Node import Node


class LinkedList(object):

    # Function to initialize head
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_head(self):
        if not self.head:
            return None
        return self.head.data

    def get_all_data(self):
        temp = self.head
        rt = []
        while temp:
            rt.append(temp.data)
            temp = temp.next
        return rt

    def print_list(self):
        values = self.get_all_data()
        for i in values:
            print(i)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):

        if self.head is None:
            return False

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp.data == key:
            self.head = temp.next
            temp = None
            return True

        prev = temp
        temp = temp.next
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

            # if key was not present in linked list
        if temp is None:
            return False

            # Unlink the node from linked list
        prev.next = temp.next

        temp = None
        return True
