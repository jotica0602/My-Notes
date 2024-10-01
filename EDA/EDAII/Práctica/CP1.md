
# Ejercicio 7

```python
def solve(G,s):
	pi, actual = bfs(G,s)
	ans = []
	while actual != s:
		ans.insert(actual,0)
		actual = pi[actual]
	ans.insert(0,s)
	return ans
	
def bfs(G,s):
	q = [s]
	d = [oo for i in range(V(G))]
	pi = [None for i in range(V(G))]
	visited = [False for i in range(V(G))]
	visited[s] = True
	d[s] = 0
	pi[s] = s
	scl = oo # shortest cycle length
	scc = s # shortest cycle source

	while q:
		v = q.pop()
		for neighbor in v.neighbors:
			if not visited[neighbor]:
				d[neighbor] = d[v] + 1
				pi[neighbor] = v
			
			if pi[v] != s and neighbor == s:
				 scl = min(scl, d[v] + 1)
				 scc = v
	
	return pi,  scc
```



