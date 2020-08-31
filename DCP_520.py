def find_depth(tree):
    depth = 0

    while tree != '0':
        tree = tree.replace('(00)', '0')
        depth += 1

    return depth
    
def find_depth_Ntime(tree):
    max_depth = depth = 0

    for char in tree:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        max_depth = max(max_depth, depth)

    return max_depth
