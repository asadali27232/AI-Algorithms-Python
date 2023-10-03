# %% [markdown]
# # LAB 05: 
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

# %%
romania = {
    "Arad": Node("Arad", None, [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)], 0),
    "Zerind": Node("Zerind", None, [("Arad", 75), ("Oradea", 71)], 0),
    "Oradea": Node("Oradea", None, [("Zerind", 71), ("Sibiu", 151)], 0),
    "Sibiu": Node("Sibiu", None, [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)], 0),
    "Timisoara": Node("Timisoara", None, [("Arad", 118), ("Lugoj", 111)], 0),
    "Lugoj": Node("Lugoj", None, [("Timisoara", 111), ("Mehadia", 70)], 0),
    "Mehadia": Node("Mehadia", None, [("Lugoj", 70), ("Drobeta", 75)], 0),
    "Drobeta": Node("Drobeta", None, [("Mehadia", 75), ("Craiova", 120)], 0),
    "Craiova": Node("Craiova", None, [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)], 0),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)], 0),
    "Fagaras": Node("Fagaras", None, [("Sibiu", 99), ("Bucharest", 211)], 0),
    "Pitesti": Node("Pitesti", None, [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)], 0),
    "Bucharest": Node("Bucharest", None, [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)], 0),
    "Giurgiu": Node("Giurgiu", None, [("Bucharest", 90)], 0),
    "Urziceni": Node("Urziceni", None, [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)], 0),
    "Hirsova": Node("Hirsova", None, [("Urziceni", 98), ("Eforie", 86)], 0),
    "Eforie": Node("Eforie", None, [("Hirsova", 86)], 0),
    "Vaslui": Node("Vaslui", None, [("Urziceni", 142), ("Iasi", 92)], 0),
    "Iasi": Node("Iasi", None, [("Vaslui", 92), ("Neamt", 87)], 0),
    "Neamt": Node("Neamt", None, [("Iasi", 87)], 0),
}


# %% [markdown]
# ## Task 3: Implement Graph as Tree
# 
# Write a function that takes a graph and a start node and returns the tree resulted from the graph search algorithm. The function should return the root node of the tree.

# %%
from anytree import Node, RenderTree

def BFS_tree_search(graph, start):
    queue = [(start, None)]  # (node, parent)
    visited = set()
    search_tree = {start: None}  # Initialize with start node and no parent

    while queue:
        current, parent = queue.pop(0)

        if current not in visited:
            visited.add(current)

            for neighbor, _ in graph[current].actions:
                if neighbor not in visited:
                    queue.append((neighbor, current))
                    if neighbor not in search_tree:
                        search_tree[neighbor] = current  # Set the parent of the neighbor

    return search_tree

# Usage example:
start_node = "Arad"  # Replace with the desired start node

# Run the BFS search and create the search tree
search_tree = BFS_tree_search(romania, start_node)

# Create the tree representation from the search tree
def create_tree_representation(tree, current_node):
    if current_node in tree:
        node = Node(current_node)
        for neighbor, parent in tree.items():
            if parent == current_node:
                child = create_tree_representation(tree, neighbor)
                child.parent = node
        return node

# Create the tree representation
tree_representation = create_tree_representation(search_tree, start_node)

# Print the tree representation
for pre, fill, node in RenderTree(tree_representation):
    print(f"{pre}{node.name}")


# %% [markdown]
# ## Task 4: UCS
# 
# Write a function that takes a graph and a start node and returns the tree resulted from the graph search algorithm. The function should return the root node of the tree.

# %% [markdown]
# **Action Sequence Function:**
# 
# Write a function that takes a node and returns the sequence of actions that leads to that node from a source node.

# %%
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
# **Find Min from Queue:**
# 
# Write a function that takes a queue and returns the node with the minimum total cost.

# %%
def find_min(frontier):
    min = frontier[0]
    for node in frontier:
        if node.totalcost < min.totalcost:
            min = node
    return min

# %% [markdown]
# **UCS Function:**

# %%
def UCS(graph, start, goal):
    
    
    return None

# %% [markdown]
# ## Task 5: Test UCS on Romania Map

# %%
print(UCS(romania, "Arad", "Bucharest"))


