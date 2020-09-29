def dfs(root):
    if root == None:
        return
    print(root.value)
    root.visited = True
    for child in root.children:
        if not child.visited:
            dfs(child)