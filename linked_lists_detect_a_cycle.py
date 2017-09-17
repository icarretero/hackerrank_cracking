"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    current_node = head
    nodes_traversed = {}
    while current_node is not None:
        current_node_id = id(current_node)
        if nodes_traversed.get(current_node_id):
            return 1
        nodes_traversed[current_node_id] = True
        current_node = current_node.next
    return 0
