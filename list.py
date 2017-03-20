from my_exceptions import EmptyNodeException


class LinkedList(object):
    """Linked list implementation"""

    def __init__(self, nodes=None):
        self._root = None
        # If nodes passed, add them while constructing
        if nodes:
            self.add_nodes(nodes)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    def add_node(self, new_node):
        """
        Adds new node to list
        :param new_node: element to be added
        :type Node
        :return:
        """
        try:
            if new_node is None:
                raise EmptyNodeException("Error: Node is None. Skipped.")

            print "Adding node '{}'".format(new_node.data)
            if not self.root:
                self.root = new_node
                return True

            cur_node = self.root

            while cur_node:
                # Run through existing list and add nodes
                if new_node.data < cur_node.data and cur_node == self.root:
                    # If new node is lower than current and the current is root element
                    return self._insert_as_root(new_node)
                elif new_node.data == cur_node.data:
                    # If new node is equals to current
                    return self._insert_in_the_middle(cur_node, new_node)
                elif new_node.data > cur_node.data:
                    # If new node is greater than current
                    if cur_node.has_next():
                        # If current node has next check that new node is lower than next
                        if new_node.data <= cur_node.next_node.data:
                            return self._insert_in_the_middle(cur_node, new_node)
                    else:
                        # If current node is last element in list, append the new node after it
                        return self._insert_at_the_end(cur_node, new_node)
                cur_node = cur_node.next_node
            return True
        except EmptyNodeException as e:
            print(e.message)
            return False

    def _insert_as_root(self, new_node):
        new_node.next_node = self.root
        self.root = new_node
        return True

    def _insert_in_the_middle(self, cur_node, new_node):
        old_next = cur_node.next_node
        cur_node.next_node = new_node
        new_node.next_node = old_next
        return True

    def _insert_at_the_end(self, cur_node, new_node):
        cur_node.next_node = new_node
        return True

    def add_nodes(self, new_nodes):
        """
        Adds list of nodes
        :param new_nodes: List od nodes to be added
        :type list or tuple
        :return: boolean
        """
        # New nodes may be list or tuple
        if not isinstance(new_nodes, list) and not isinstance(new_nodes, tuple):
            raise ValueError("New nodes must be of type list, but it's {}".format(type(new_nodes)))
        for node in new_nodes:
            self.add_node(node)

    def to_string(self):
        """
        Prints LinkedList to stdout
        """
        cur_node = self.root
        print "\nList Content:"
        while cur_node:
            print cur_node.data
            cur_node = cur_node.next_node

