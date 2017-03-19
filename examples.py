from list import LinkedList
from node import Node

print "\nCreating LinkedList from python list"
my_list = LinkedList([Node(2), None, Node(0), Node(0),Node(4)])
my_list.to_string()

print "\nAdding single node"
my_list.add_node(Node(5))
my_list.to_string()

print "\nAdding nodes from python tuple"
my_list.add_nodes((Node(0), Node(20), Node(-1)))
my_list.to_string()
