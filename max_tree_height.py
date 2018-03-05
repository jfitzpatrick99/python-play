

class Node:
  def __init__(self, left, right, data=None):
    self._left = left
    self._right = right
    self._data = data


  def left(self):
    return self._left


  def right(self):
    return self._right


  def data(self):
    return self._data


def max_height(node):
  if node is None:
    return 0

  left_height = max_height(node.left()) + 1
  right_height = max_height(node.right()) + 1

  return max(left_height, right_height)


def main():
  tree = Node(None, Node(None, None))

  print(max_height(tree))


if __name__ == "__main__":
  main()
