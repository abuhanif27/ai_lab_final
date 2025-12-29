from collections import deque

bus_graph = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "F"],
    "D": ["A", "E"],
    "E": ["D", "F", "G"],
    "F": ["C", "E"],
    "G": ["E"]
}

def two_color_schedule(graph):
    color = {}  # node -> 0 or 1

    for start in graph:
        if start in color:
            continue

        # assign first node color 0
        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()

            for v in graph[u]:
                if v not in color:
                    # give opposite color to neighbor
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    # if neighbor has same color → NOT possible with 2 colors
                    return None

    return color

color = two_color_schedule(bus_graph)

slot1 = sorted([n for n, c in color.items() if c == 0])
slot2 = sorted([n for n, c in color.items() if c == 1])

print("Adjacency List:", bus_graph)
print("Time Slot 1:", slot1)
print("Time Slot 2:", slot2)
print("Minimum time slots required:", 2)
