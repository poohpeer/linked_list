class LinkedList(object):

    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.getter
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    def add_node(self, new_node):
        if new_node is None:
            raise ValueError("Node is None")

        if self.root is None:
            self.root = new_node
            return True

        cur_node = self.root

        while cur_node:
            if new_node.data <= cur_node.data:
                # If new node gt current node, replace it
                new_node.next_node = cur_node
                if cur_node == self.root:
                    # If current was root, set new to be root
                    self.root = new_node
                    return True
                else:
                    return True
            if cur_node.has_next():
                cur_node = cur_node.next_node
            else:
                cur_node.next_node = new_node
                cur_node = None
        return True

    def add_nodes(self, new_nodes):
        if not isinstance(new_nodes, list):
            raise ValueError("New nodes must be of type list, but it's {}".format(type(new_nodes)))
        for node in new_nodes:
            self.add_node(node)

    def to_string(self):
        cur_node = self.root
        while cur_node:
            print cur_node.data
            cur_node = cur_node.next_node

