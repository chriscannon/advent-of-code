package common

// RunDFS takes a graph and root node and returns the depth-first traversal of the tree.
func RunDFS(graph map[string][]string, root string) []string {
	return dfs(graph, root, make(map[string]bool))
}

func dfs(graph map[string][]string, node string, seen map[string]bool) []string {
	seen[node] = true
	path := []string{node}
	for _, next := range graph[node] {
		if _, ok := seen[next]; !ok {
			path = append(path, dfs(graph, next, seen)...)
		}
	}
	return path
}

// RunBFS takes a graph and root node and returns the breadth-first traversal of the tree.
func RunBFS(graph map[string][]string, root string) []string {
	path := []string{root}
	seen := make(map[string]bool)
	var frontier []string

	frontier = append(frontier, root)
	seen[root] = true

	var node string
	for len(frontier) > 0 {
		// Taken from https://github.com/golang/go/wiki/SliceTricks#pop-frontshift
		node, frontier = frontier[0], frontier[1:]
		for _, next := range graph[node] {
			if _, ok := seen[next]; !ok {
				frontier = append(frontier, next)
				seen[next] = true
				path = append(path, next)
			}
		}
	}
	return path
}
