from list import LinkedList
from node import Node

my_list = LinkedList([Node(2),Node(4)])
print "\nNew list created"
my_list.to_string()

print "\nAdding new nodes"
my_list.add_nodes([Node(5), None, Node(21), Node(0), Node(0), Node(0)])
my_list.to_string()

print "\nAdding new nodes"
my_list.add_nodes((Node(0), Node(2), Node(20), Node(-1)))
my_list.to_string()
