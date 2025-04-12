from collections import defaultdict, deque

def load_connections(file_path):
    graph = defaultdict(set)
    with open(file_path, 'r') as file:
        for line in file:
            if ',' not in line:
                continue
            city1, city2 = line.strip().split(',')
            city1 = city1.strip()
            city2 = city2.strip()
            graph[city1].add(city2)
            graph[city2].add(city1)
    return graph

def are_connected(graph, city1, city2):
    if city1 not in graph or city2 not in graph:
        return False
    visited = set()
    queue = deque([city1])
    while queue:
        current = queue.popleft()
        if current == city2:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
if _name=="main_":
    file_path = ("connections.txt")
    city1 = input("Enter source city: ").strip()
    city2 = input("Enter destination city: ").strip()

graph = load_connections ("connections.txt")

if are_connected(graph, city1, city2):
        print("YES")
else:
        print("NO")