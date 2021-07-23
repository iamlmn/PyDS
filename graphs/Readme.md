Graph is a collection of object called as Vertices and together with relationship between them called as Edges.

Each edge in the graph joins two vertices. 
Vertices V = {A,B,C, D}
Edges E = {A -> B, A -> D, B -> C, B -> D, C -> D}


Types of Edges: 
1. Directed edges : An edge (u,v) is directed if pair (u,v) is ordered, 
    with u preceding v.
2. Undirected edges: An edge (u, v) is undirected if pair (u, v ) is not ordered.

3. Weighted edge: Cost associated with each edge. 
    Both weighted directed/ undirected graph are possible.


End Vertices: Two vertices joined by an edge. 
Adjacent vertices: Two vertices are adjacent if there is an edge between them.
Incident edge: If vertex is one of the end points.
Incoming edge: destination is the vertex
Outgoing Edge origin is the vertex.
self loop : if the two end points are same 
Parellel edges: Edge from u -> v and v -> u exists. 

Degree of vertex: number of edges to a vertex.
indegree of vertex: number of incoming edges
outdegree : number of outgoing edges. 

Sub graph:  Whose vertices and edges are a subset of another graph.

Connected components: Connected sub graphs are known as connected components.
Articulation point: Vertex whose removal results in connected components. 
Bi-connected components : components connected by two edges, removing an edge wont lead to seperate components.
Strongly connected graphs : all the vertices are reachable from any vertex.

    