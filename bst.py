import node
import utils

root = node.Node(201, node.Node(100, node.Node(20, None, None), node.Node(110, None, None)), node.Node(300, node.Node(205, None, None), node.Node(305, None, None)))

n = utils.find(root, 205)
if n == None:
    print("205 not found")
else:
    print("205 found!")

n = utils.find(root, 206)
if n == None:
    print("206 not found")
else:
    print("206 found!")
