graph = {
    "Desktop": ["Semester_6"],
    "Semester_6": ["AI"],
    "AI": ["Notes", "Lab"],  # left-to-right same as picture
    "Notes": [],
    "Lab": ["DFS_Report.pdf"],
    "DFS_Report.pdf": []
}


def dfs(graph, start, target, parent, visited, order):
    visited.add(start)
    order.append(start)

    if start == target:
        return True

    for nxt in graph.get(start, []):
        if nxt not in visited:
            parent[nxt] = start
            if dfs(graph, nxt, target, parent, visited, order):
                return True

    return False


if __name__ == "__main__":
    start_Node = "Desktop"
    target_node = "DFS_Report.pdf"

    order = []
    visited = set()

    parent = {start_Node: None}

    found = dfs(graph, start_Node, target_node, parent, visited, order)

    path = []

    if found:
        start_Node = target_node
        while start_Node is not None:
            path.append(start_Node)
            start_Node = parent[start_Node]
        path.reverse()

    print("DFS Traversal: " + " -> ".join(order))
    print("We Found The Target" if found == True else "We Not Found The Target")
    print("Path: "+"/".join(path))
