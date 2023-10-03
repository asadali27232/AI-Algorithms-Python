# %% [markdown]
# # LAB 04: BFS and DFS for Graphs
# 

# %% [markdown]
# ## Task 1: Implement Node Class
# 
# Write class Node that has the following attributes:
# 
# - state
# - parent
# - action
# - totalcost
# 

# %%
class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost

# %% [markdown]
# ## Task 2: Implemnet Graphs using Node Class
# 
# Create different graphs using the Node class. Use dictionaries to store the graph nodes. The keys of the dictionaries are the names of the nodes and the values are the Node objects.
# 

# %% [markdown]
# Graph 1:

# %%
graph1 = {
    "A": Node("A", None, ["B", "C", "C"], None),
    "B": Node("B", None, ["D", "A"], None),
    "C": Node("C", None, ["A", "F", "G"], None),
    "D": Node("D", None, ["B", "E"], None),
    "E": Node("E", None, ["D", "A"], None),
    "G": Node("G", None, ["C"], None),
    "F": Node("F", None, ["C"], None),
}


# %% [markdown]
# Graph 2:

# %%
graph2 = {
    "S" : Node("S", None, ["d", "e", "p"], None),
    "p" : Node("p", None, ["q"], None),
    "q" : Node("q", None, [], None),
    "r" : Node("r", None, ["f"], None),
    "a" : Node("a", None, [], None),
    "b" : Node("b", None, ["a"], None),
    "c" : Node("c", None, ["a"], None),
    "d" : Node("d", None, ["b", "c"], None),
    "e" : Node("e", None, ["h", "r"], None),
    "f" : Node("f", None, ["G"], None),
    "h" : Node("h", None, ["p", "q"], None),
    "G" : Node("G", None, [], None),
}

# %% [markdown]
# Graph 3:

# %%
romania = {
    "Arad": Node("Arad", None, ["Zerind", "Sibiu", "Timisoara"], None),
    "Zerind": Node("Zerind", None, ["Arad", "Oradea"], None),
    "Oradea": Node("Oradea", None, ["Zerind", "Sibiu"], None),
    "Sibiu": Node("Sibiu", None, ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"], None),
    "Timisoara": Node("Timisoara", None, ["Arad", "Lugoj"], None),
    "Lugoj": Node("Lugoj", None, ["Timisoara", "Mehadia"], None),
    "Mehadia": Node("Mehadia", None, ["Lugoj", "Drobeta"], None),
    "Drobeta": Node("Drobeta", None, ["Mehadia", "Craiova"], None),
    "Craiova": Node("Craiova", None, ["Drobeta", "Rimnicu Vilcea", "Pitesti"], None),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, ["Sibiu", "Craiova", "Pitesti"], None),
    "Fagaras": Node("Fagaras", None, ["Sibiu", "Bucharest"], None),
    "Pitesti": Node("Pitesti", None, ["Rimnicu Vilcea", "Craiova", "Bucharest"], None),
    "Bucharest": Node("Bucharest", None, ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"], None),
    "Giurgiu": Node("Giurgiu", None, ["Bucharest"], None),
    "Urziceni": Node("Urziceni", None, ["Bucharest", "Hirsova", "Vaslui"], None),
    "Hirsova": Node("Hirsova", None, ["Urziceni", "Eforie"], None),
    "Eforie": Node("Eforie", None, ["Hirsova"], None),
    "Vaslui": Node("Vaslui", None, ["Urziceni", "Iasi"], None),
    "Iasi": Node("Iasi", None, ["Vaslui", "Neamt"], None),
    "Neamt": Node("Neamt", None, ["Iasi"], None),
}


# %% [markdown]
# ## Task 3: Implementing BFS
# 
# Implement BFS algorithm for the graphs created in Task 2. The algorithm should take the graph and the starting node as input and return the path from the starting node to the goal node. The path should be a list of node names.

# %%
def BFS(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    path = []
    while queue:
        current = queue.pop(0)
        path.append(current)
        if current == goal:
            return path
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return path

# %% [markdown]
# Other Implementations of BFS:
# 

# %%
def BFS2(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)

    while queue:
        current = queue.pop(0)
        if current == goal:
            return actionSequence(graph, start, goal)  # Change to start here
        for neighbor in graph[current].actions:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current


def actionSequence(graph, start, goal):
    solution = [goal]
    current = goal
    while current != start:
        currentParent = graph[current].parent
        solution.append(currentParent)
        current = currentParent
    solution.reverse()
    return solution

# %% [markdown]
# ## Task 4: Testing BFS
# 
# Test BFS algorithm with the graphs created in Task 2. Print the path returned by the algorithm.

# %% [markdown]
# Graph 1:

# %%
print(BFS(graph1, "D", "F"))
print(BFS2(graph1, "D", "F"))
print(actionSequence(graph1, "D", "F"))

# %% [markdown]
# Graph 2:

# %%
print(BFS(graph2, "S", "G"))
print(BFS2(graph2, "S", "G"))
print(actionSequence(graph2, "S", "G"))

# %% [markdown]
# Graph 3:

# %%
print(BFS(romania, "Arad", "Bucharest"))
print(BFS2(romania, "Arad", "Bucharest"))
print(actionSequence(romania, "Arad", "Bucharest"))

# %% [markdown]
# ## Task 5: Implementing DFS
# 
# Implement DFS algorithm for the graphs created in Task 2. The algorithm should take the graph and the starting node as input and return the path from the starting node to the goal node. The path should be a list of node names.

# %%
def DFS(graph, start, goal):
    stack = []
    visited = []
    stack.append(start)
    visited.append(start)
    path = []

    while stack:
        current = stack.pop()
        path.append(current)

        if current == goal:
            return path

        for neighbor in graph[current].actions:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)
                graph[neighbor].parent = current

    return path

# %% [markdown]
# ## Task 6: Testing DFS
# 
# Test DFS algorithm with the graphs created in Task 2. Print the path returned by the algorithm.

# %%
print(DFS(graph1, "D", "F"))
print(DFS(graph2, "S", "G"))
print(DFS(romania, "Arad", "Bucharest"))


