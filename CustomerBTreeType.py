class CustomerBTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class CustomerBTreeType:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = CustomerBTreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data['account_number'] < node.data['account_number']:
            if node.left is None:
                node.left = CustomerBTreeNode(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = CustomerBTreeNode(data)
            else:
                self._insert(data, node.right)

    def search(self, account_number):
        return self._search(account_number, self.root)

    def _search(self, account_number, node):
        if node is None:
            return None
        elif account_number == node.data['account_number']:
            return node.data
        elif account_number < node.data['account_number']:
            return self._search(account_number, node.left)
        else:
            return self._search(account_number, node.right)
