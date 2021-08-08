# Binary Tree Node
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Implentation of BFS
# Complexity - O(N) - time complexity, O(N) - space complexity
def BFS(root):
    """
    Performs Breadth First Search on binary tree (root). Prints the values of node
    in this implementation.
    """
    queue = []                           # queue to hold the nodes
    queue.append(root)                   # enqueue root of tree
    while queue:
        print(queue[0].val, end=' ')     # touch the node
        if queue[0].left:                # enqueue the children of current node
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue.pop(0)                     # dequeue node from queue




def main():
    # create a binary tree for testing 
    root = BinaryTreeNode(1, BinaryTreeNode(3, BinaryTreeNode(1), BinaryTreeNode(2)), BinaryTreeNode(2, None, BinaryTreeNode(3)))
    BFS(root)


if __name__ == '__main__':
    main()

