#!/usr/bin/python3

"""node class"""


class Node:

    """node of a linked list"""
    def __init__(self, data, next_node=None):
        """initialize"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter"""
        return self.data

    @data.setter
    def data(self, value):
        """setter"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


"""singly linked list"""


class SinglyLinkedList:

    """initialize"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        """initialize"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
