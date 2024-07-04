from collections import defaultdict
from collections import deque

# define graph


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to be implemented
    def BFS(self, s):
        queue = []
        ans=""
        visited = [False] * (len(self.graph)+4)
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            ans=ans+str(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return ans

# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u, v)
f.close()
with open('output.txt', 'wt') as gp:
    tmp2 = g.BFS(1)
    gp.write(' '.join([str(it) for it in tmp2]))

# g.BFS(0)
#fromgeekforgeek