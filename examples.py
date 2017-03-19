from list import LinkedList
from node import Node

my_list = LinkedList()
for value in range(1, 20, 3):
    my_list.add_node(Node(value))
my_list.to_string()

my_list.add_nodes([Node(0), Node(5), Node(21)])
my_list.to_string()
