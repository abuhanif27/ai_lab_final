graph = {
    "Desktop": ["Semester_6"],
    "Semester_6": ["AI"],
    "AI": ["Notes", "Lab"],   # left-to-right order
    "Notes": [],
    "Lab": ["DFS_Report.pdf"],
    "DFS_Report.pdf": []
}

def depth_limited_dfs(graph, current, target, depth_left, visit_order, on_path):
    """
    DFS but with a limit:
    - depth_left tells how many more steps we are allowed to go down.
    - on_path prevents infinite loops (cycle safety).
    """
    visit_order.append(current)

    # Found it!
    if current == target:
        return [current]  # path from here to target

    # If no depth left, stop exploring further
    if depth_left == 0:
        return None

    on_path.add(current)

    for nxt in graph.get(current, []):
        if nxt not in on_path:
            result_path = depth_limited_dfs(
                graph, nxt, target, depth_left - 1, visit_order, on_path
            )
            if result_path is not None:
                return [current] + result_path

    on_path.remove(current)
    return None


def iddfs(graph, start, target, max_depth):
    """
    Try depth = 0, then 1, then 2 ... until max_depth.
    """
    for depth in range(max_depth + 1):
        visit_order_this_round = []
        path = depth_limited_dfs(
            graph, start, target, depth, visit_order_this_round, set()
        )

        print(f"Depth limit = {depth} | Visited: {' -> '.join(visit_order_this_round)}")

        if path is not None:
            return True, path, depth

    return False, [], None


if __name__ == "__main__":
    start = "Desktop"
    target = "Notes"   # <-- IMPORTANT: graph has "Notes", not "Note"
    max_depth = len(graph)  # safe limit for this small graph

    found, path, depth_found = iddfs(graph, start, target, max_depth)

    print("\nFound?", found)
    if found:
        print("Found at depth:", depth_found)
        print("Path:", " / ".join(path))
