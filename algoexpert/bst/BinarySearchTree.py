from typing import Any, Optional, Tuple


class BinarySearchTree:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left: Optional[BinarySearchTree] = left
        self.right: Optional[BinarySearchTree] = right

    def insert(self, value: int) -> None:
        side = self.left if value < self.value else self.right
        if side != None:
            side.insert(value)
        side = BinarySearchTree(value)

    def contains(self, value: int) -> bool:
        while self is not None:
            if value < self.value:
                self = self.left
            elif value > self.value:
                self = self.right
            else:
                return True
        return False

    def remove(self, value: int) -> None:
        parent_node, self = self.__find_node_to_remove(value)
        if self.left and self.right:
            self.value = self.right.__get_min_value()
            self.right.remove(self.value)
        elif parent_node is None:
            if self.left:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
            elif self.right:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            else:
                pass
        elif parent_node.left == self:
            parent_node.left = self.left if self.left else self.right
        elif parent_node.right == self:
            parent_node.right = self.left if self.left else self.right

    def __find_node_to_remove(self, value: int) -> Tuple[Any, Any]:
        parent_node = None
        while self:
            if value < self.value:
                parent_node = self
                self = self.left
            elif value > self.value:
                parent_node = self
                self = self.right
            else:
                break
        return parent_node, self
