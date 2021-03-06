# from platform import node
# from typing import Dict, List

# class Graph:
#     """
#     Graph
#     """
#     def __init__(self, directed: bool=False) -> None:
#         self.directed = directed
#         self.adj_mat: Dict[str, List] = {}

#     def _add_node(self, node_name: str) -> None:
#         assert node_name not in self.adj_mat, f"{node_name} exist"
#         assert isinstance(node_name, str), f"{node_name} not string"
#         self.adj_mat[node_name] = []


#     def add_nodes(self, *nodes):
#         for elm in nodes:
#             if isinstance(elm, str):
#                 self._add_node(elm)
#             elif isinstance(elm, list):
#                 for node in elm:
#                     self._add_node(node)
    
#     def add_edge(self, node_a: str, node_b: str) -> None:
#         """
#         if graph is directed we have an edge from first argument to second argument
#         """
#         if node_a not in self.adj_mat or node_b not in self.adj_mat:
#             raise Exception("khak tu saret!!!")
#         if self.directed:
#             self.adj_mat[node_a].append(node_b)
#         else:
#             self.adj_mat[node_a].append(node_b)
#             self.adj_mat[node_b].append(node_a)

#     def __str__(self) -> str:
#         return str(self.adj_mat)


# g1 = Graph()
# g1.add_nodes("a")
# g1.add_nodes("b")
# g1.add_nodes("c")
# g1.add_nodes("d")
# g1.add_nodes("e")
# g1.add_nodes("f")
# g1.add_nodes("g")
# g1.add_nodes("h")
# g1.add_nodes("k")

# g1.add_edge("a", "b")
# g1.add_edge("a", "c")
# g1.add_edge("c", "e")
# g1.add_edge("f", "g")
# g1.add_edge("k", "a")
# g1.add_edge("h", "a")
# g1.add_edge("f", "b")

# print(g1)




class Node:
    def __init__(self, data = None, is_free = True) -> None:
        self.data = data
        self.next = None
        self.is_free = is_free

    def make_free(self):
        self.is_free = True

    def make_occupy(self):
        self.is_free = False




class LinkedList:
    def __init__(self) -> None:
        self.root = None #root: first node

    def add_node(self, node):
        if self.root is None:
            self.root = node

    def add_begin(self, node : Node):
        if not node.is_free:
            raise Exception 
        if not self.root:
            self.root = node
            node.make_occupy()
        else:
            node.next = self.root
            self.root = node
            node.make_occupy()
        
    def __str__(self) -> str:
        pass``

node1 = Node('ashkan')
node2 = Node(123)
node3 = Node(['adsffasf', 12345])

l = LinkedList()
l.add_begin(node1)
l.add_begin(node2)
l.add_begin(node3)

print(l)