from collections import defaultdict

# define graph
class Graph:

    # Constructor
   def __init__(self):
        # default dictionary to store graph
       self.graph = defaultdict(list)

    # function to add an edge to graph
   def addEdge(self, u, v):
       self.graph[u].append(v)
       
       
    #Traversal
#    def traversal(self, v, visited):
       
#        visited.add(v)
#        print(v)
       
#        for neighbour in self.graph[v]:
#            if neighbour not in visited:
#                self.traversal(neighbour,visited)
               
               
   # function to be implemented
   def DFS(self,node):
    visited = set()
    stack = [node]
    answer=""
    while stack:
        node = stack.pop()
        if node not in visited:
            answer=answer+str(node)
            visited.add(node)
            stack.extend(self.graph[node])
    return answer
# Driver code
# g=Graph()
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(4,5)
# g.addEdge(5,6)
# g.addEdge(2,6)
# print(g.DFS())
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v)
f.close()

with open('output.txt', 'wt') as gp:
    tmp = g.DFS(1)
    gp.write(' '.join([str(it) for it in tmp]))


#from stackoverflow
