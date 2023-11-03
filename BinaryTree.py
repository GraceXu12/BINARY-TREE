class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class Tree():
    def insert_node(self, current, node_value):

      if current == None:
            return Node(node_value)
      else:
            if node_value < current.value:
                current.left_child = self.insert_node(current.left_child, node_value)
            elif node_value > current.value:
                current.right_child = self.insert_node(current.right_child, node_value)
            balance_factor = self.balanced(current)
            if balance_factor > 1:
                if node_value > current.left_child.value:
                    current.left_child = self.left_rotate(current.left_child)
                    current = self.right_rotate(current)
                else:
                    current = self.right_rotate(current)
            elif balance_factor < -1:
                if node_value < current.right_child.value:
                    current.right_child = self.right_rotate(current.right_child)
                    current = self.left_rotate(current)
                else:
                    current = self.left_rotate(current)
            return current

    def left_rotate(self, z):
        y = z.right_child
        t = y.left_child
        y.left_child = z
        z.right_child = t
        return y

    def right_rotate(self,z):

        y = z.left_child
        t = y.right_child
        y.right_child = z
        z.left_child = t
        return y


    def depth(self, current):
        if current == None:
            return 0
        return max(self.depth(current.left_child), self.depth(current.right_child))+1

    def balanced(self, current):
        depth_right = self.depth(current.right_child)
        depth_left = self.depth(current.left_child)
        depth_difference = depth_left - depth_right
        return depth_difference

    def print1(self, current,i):
        i = i+1
        space = i * "    "
        if current == None:
            return 0
        elif i == 0:
            print("root")
            print(current.value)
        if current.left_child and current.right_child:
            print(f"{space} L = {current.left_child.value}")
            self.print1(current.left_child, i)
            print(f"{space} R = {current.right_child.value}")
            self.print1(current.right_child,i)
        elif current.right_child == None and current.left_child:
            print(f"{space} L = {current.left_child.value}")
            self.print1(current.left_child,i)
        elif current.left_child == None and current.right_child:
            print(f"{space} R = {current.right_child.value}")
            self.print1(current.right_child,i)

tree = Tree()
root = None

while True:
    print("  ")
    num = float(input("Input num = "))
    root = tree.insert_node(root, num)
    print("  ")
    tree.print1(root,-1)





