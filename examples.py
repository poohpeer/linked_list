from list import LinkedList
from node import Node

my_list = LinkedList()
print "\nAdding new nodes"
for value in range(1, 20, 3):
    my_list.add_node(Node(value))
my_list.to_string()

print "\nAdding new nodes"
my_list.add_nodes([Node(5), None, Node(21), Node(0)])
my_list.to_string()
