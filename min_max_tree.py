from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Node:
    name: str
    children: List["Node"] = field(default_factory=list)
    value: Optional[int] = None  # if leaf node, value is set

def minimax(node: Node, is_max: bool) -> int:
    # If this is a leaf, return its value
    if node.value is not None:
        return node.value

    # Otherwise, get minimax values of children
    child_values = [minimax(child, not is_max) for child in node.children]

    # MAX chooses maximum, MIN chooses minimum
    return max(child_values) if is_max else min(child_values)

def show_tree(node: Node, is_max: bool, indent=""):
    val = minimax(node, is_max)
    role = "MAX" if is_max else "MIN"
    print(f"{indent}{node.name} ({role}) = {val}")
    for child in node.children:
        show_tree(child, not is_max, indent + "  ")

def leaf(x):
    return Node(name=str(x), value=x)

# ----- Build tree exactly like your picture -----

# Left MIN child of root
L_max_13 = Node("13", [leaf(4), leaf(13)])            # MAX
L_min_5  = Node("5",  [leaf(5), leaf(10)])            # MIN
L_max_11 = Node("11", [L_min_5, leaf(11)])            # MAX
L_leaf16 = leaf(16)
Left_MIN = Node("Left(11)", [L_max_13, L_max_11, L_leaf16])  # MIN

# Middle MIN child of root
M_min_1  = Node("1", [leaf(1), leaf(8)])              # MIN
M_min_6  = Node("6", [leaf(6), leaf(12)])             # MIN
M_max_9  = Node("9", [M_min_1, leaf(9), M_min_6])     # MAX
Mid_MIN  = Node("Middle(9)", [M_max_9, leaf(12)])     # MIN

# Right MIN child of root
R_min_2  = Node("2", [leaf(2), leaf(5), leaf(7)])     # MIN
R_max_10 = Node("10", [leaf(10), leaf(8), R_min_2])   # MAX
R_max_7  = Node("7", [leaf(7), leaf(4)])              # MAX
Right_MIN= Node("Right(7)", [R_max_10, R_max_7])      # MIN

# Root MAX
Root = Node("ROOT", [Left_MIN, Mid_MIN, Right_MIN])   # MAX

# Print all values
show_tree(Root, True)
print("\nFinal minimax value at Root =", minimax(Root, True))
