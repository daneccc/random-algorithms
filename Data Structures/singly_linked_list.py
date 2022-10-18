# Implementation of class-based singly linked list in python

"""
Visual representation for singly linked list

    Node(A)----next--> Node(B) ----next--> Node(C) ----next--> Node(D) ----> None
      ^
    head
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nodes: list = None):
        self.head = None
        # This allows creating a linked list with some data
        if nodes is not None:
            node = Node(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(val=elem)
                node = node.next

    def __iter__(self):
        """This allows us to 'traverse' the linked list"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def len(self):
        """Requires traversing the linked list: O(n)"""
        count = 0
        for _ in self:
            count += 1
        return count

    def __repr__(self):
        """This allows us to print the linked list in a nice way to console
        i.e:  A -> B -> None
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def get(self, target_index):
        """Get value of node at a specific index, requires traversing the list O(n)"""
        if self.head is None:
            raise Exception("List is empty")

        if target_index > self.len():
            raise Exception("Target index out of range")

        for index, node in enumerate(self):
            if index == target_index:
                return node.val

    def add_to_beginning(self, node: Node):
        """insert a new node at the beginning: O(1)"""
        node.next = self.head
        self.head = node

    def add_to_end(self, node: Node):
        """insert a new node at the end, requires traversing the whole linked list: O(1)"""
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_val, new_node: Node):
        """insert a node `after` a specific existing node, requires traversing the linked list
        to find the target node val to find the point at which insertion needs to happen
        ~O(n)
        """
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.val == target_node_val:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with value '%s' not found" % target_node_val)

    def add_before(self, target_node_val, new_node: Node):
        """insert a node `before` a specific existing node, requires traversing the linked list
        to find the target node val to find the point at which insertion needs to happen
        ~O(n)
        """
        if self.head is None:
            raise Exception("List is empty")

        if self.head.val == target_node_val:
            # If the attempt is to add a node before the current head, this makes the new node
            # the new head, can re_use self.add_to_beginning for this
            return self.add_to_beginning(Node(target_node_val))

        prev_node = self.head
        for node in self:
            if node.val == target_node_val:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with value '%s' not found" % target_node_val)

    def remove_specific_node(self, target_node_val):
        """remove any target node by providing its value. Requires traversing the linked list
        This is done by basically breaking the links to the target node
        ~O(n)
        """
        if self.head is None:
            raise Exception("List is empty, nothing to remove")

        if self.head.val == target_node_val:
            # If the target value is the head node, just make the next node the new head
            # This breaks the link to target node, therefore removing it
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.val == target_node_val:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node with value '%s' not found" % target_node_val)


llist = LinkedList(["a", "b", "c", "d"])
print(f"Starting head: {llist.head.val}")
print(llist)

# Get value of node at specified index
print(llist.get(2))


# Add to beginning and print llist, this changes head
llist.add_to_beginning(Node("0"))
print(llist)

# Add to end and print llist
llist.add_to_end(Node("e"))
print(llist)

# Add after a specific node and print llist
llist.add_after("b", Node("k"))
print(llist)

# Add before a specific node and print llist
llist.add_before("d", Node("k"))
print(llist)

# Remove a node from the llist
llist.remove_specific_node("c")
print(llist)

print(f"Final head: {llist.head.val}")
