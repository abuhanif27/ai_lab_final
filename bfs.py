from collections import deque

graph = {
    "Desktop": ["Semester_6"],
    "Semester_6": ["AI"],
    "AI": ["Notes", "Lab"],
    "Notes": [],
    "Lab": ["DFS_Report.pdf"],
    "DFS_Report.pdf": []
}

def bfs(graph, start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        if current == target:
            # build path by walking back using parent
            path = []
            node = target
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return True, order, path

        for nxt in graph.get(current, []):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                queue.append(nxt)

    return False, order, []


if __name__ == "__main__":
    start = "Desktop"
    target = "DFS_Report.pdf"

    found, order, path = bfs(graph, start, target)

    print("BFS Visit Order:", " -> ".join(order))
    print("Found?", found)
    print("Path:", " / ".join(path))
