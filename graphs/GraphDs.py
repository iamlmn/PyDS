class GraphDs:
    def __init__(self, vertices):
        self._vertices = vertices
        self.adjMat = [[0 for j in range(self._vertices)] for i in range(self._vertices)]

    def insert_edge(self, u, v, x=1):
        '''
        Insert edge connection from u to v with weight x
        TC & SC : O(1)
        '''
        self.adjMat[u][v] = x
    
    def remove_edges(self, u, v):
        '''
        Resets connection edge to 0.
        TC & SC : O(1)
        '''
        self.adjMat[u][v] = 0

    def exist_edge(self, u, v):
        '''
        Returns bool if an connection from u to v exists.
        Tc, Sc : O(1)
        '''
        return self.adjMat[u][v] != 0

    def edges(self):
        '''
        Prints edge connection from two points
        TC : O(N**2), SC: O(1) 
        '''
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self.adjMat[i][j] != 0:
                    print(i, '-->', j, 'w:', self.adjMat[i][j])

            


    def vertices(self):
        '''
        Prints all vertices.
        TC: O(n), SC: O(1)
        '''
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    
    def edge_count(self):
        '''
        Returns number of edges in adj matrix.
        Tc & Sc: O(N2), O(1)
        '''
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self.adjMat[i][j] != 0:
                    count += 1

        return count

    def vertex_count(self):
        '''
        Returs num of vertices.
        SC, TC: O(1)
        '''
        return self._vertices


    def indegree(self, u):
        '''
        Returns number of incoming connections for a given node.
        Tc: O(N)
        SC: O(1)
        '''
        count = 0
        for i in range(self._vertices):
            if self.adjMat[i][u] != 0:
                count += 1

        return count
        

    def outdegree(self, v):
        '''
        Returns outwards connection count for a given point. that is edge starting from v.
        Tc: O(n), Sc : O(1)
        '''
        count=0
        for j in range(self._vertices):
            if self.adjMat[v][j] != 0:
                count += 1
        return count

    def printAdjMatrix(self):
        '''
        Prints Adj matrix
        Tc: O(mn)
        Sc: O(1)
        '''
        print(self.adjMat)


if __name__ == '__main__':
    print("Implementing Unidrected Graph.")
    print(" ----------------------------")
    Ug = GraphDs(4)
    Ug.printAdjMatrix()
    print("Vertices", Ug.vertex_count())
    print("Edges", Ug.edge_count())
    Ug.insert_edge(0,1,)
    Ug.insert_edge(1,0)
    Ug.insert_edge(0,2)
    Ug.insert_edge(2,0)
    Ug.insert_edge(1,2)
    Ug.insert_edge(2,1)
    Ug.insert_edge(2,3)
    Ug.insert_edge(3,2)
    print("After insertion")
    Ug.printAdjMatrix()
    print("Edges", Ug.edge_count())
    Ug.edges()
    print('Edge between 1 - 3 exists? : ', Ug.exist_edge(1,3))
    print('Edge between 1 - 2 exists? : ', Ug.exist_edge(1,2))
    print("In-Degree", Ug.indegree(2))
    print("Out-Degree", Ug.indegree(2))
    Ug.remove_edges(1,2)
    print('Edge between 1 - 2 exists? : ', Ug.exist_edge(1,2))
    print(" -------------------------------------------")


    print("Implementing Unidrected Weighted Graph.")
    print(" ----------------------------")
    Uwg = GraphDs(4)
    Uwg.printAdjMatrix()
    print("Vertices", Uwg.vertex_count())
    print("Edges", Uwg.edge_count())
    Uwg.insert_edge(0,1, 26)
    Uwg.insert_edge(1,0, 26)
    Uwg.insert_edge(0,2, 16)
    Uwg.insert_edge(2,0, 16)
    Uwg.insert_edge(1,2, 12)
    Uwg.insert_edge(2,1, 12)
    Uwg.insert_edge(2,3, 8)
    Uwg.insert_edge(3,2, 8)
    print("After insertion")
    Uwg.printAdjMatrix()
    print("Edges", Uwg.edge_count())
    Uwg.edges()
    print('Edge between 1 - 3 exists? : ', Uwg.exist_edge(1,3))
    print('Edge between 1 - 2 exists? : ', Uwg.exist_edge(1,2))
    print("In-Degree", Uwg.indegree(2))
    print("Out-Degree", Uwg.indegree(2))
    Uwg.remove_edges(1,2)
    print('Edge between 1 - 2 exists? : ', Uwg.exist_edge(1,2))
    print(" -------------------------------------------")


    print("Implementing Directed Graph.")
    print(" ----------------------------")
    dg = GraphDs(4)
    dg.printAdjMatrix()
    print("Vertices", dg.vertex_count())
    print("Edges", dg.edge_count())
    dg.insert_edge(0,1)
    # dg.insert_edge(1,0, 26)
    dg.insert_edge(0,2)
    # dg.insert_edge(2,0, 16)
    dg.insert_edge(1,2)
    # dg.insert_edge(2,1, 12)
    dg.insert_edge(2,3)
    # dg.insert_edge(3,2, 8)
    print("After insertion")
    dg.printAdjMatrix()
    print("Edges", dg.edge_count())
    dg.edges()
    print('Edge between 1 - 3 exists? : ', dg.exist_edge(1,3))
    print('Edge between 1 - 2 exists? : ', dg.exist_edge(1,2))
    print('Edge between 2 - 1 exists? : ', dg.exist_edge(2, 1))
    print("In-Degree", dg.indegree(2))
    print("Out-Degree", dg.outdegree(2))
    dg.remove_edges(1,2)
    print('Edge between 1 - 2 exists? : ', dg.exist_edge(1,2))
    print(" -------------------------------------------")


    print("Implementing Directed Weighted Graph.")
    print(" ----------------------------")
    dwg = GraphDs(4)
    dwg.printAdjMatrix()
    print("Vertices", dwg.vertex_count())
    print("Edges", dwg.edge_count())
    dwg.insert_edge(0,1, 26)
    dwg.insert_edge(0,2, 16)
    dwg.insert_edge(1,2, 12)
    dwg.insert_edge(2,3, 8)
    print("After insertion")
    dwg.printAdjMatrix()
    print("Edges", dwg.edge_count())
    dwg.edges()
    print('Edge between 1 - 3 exists? : ', dwg.exist_edge(1,3))
    print('Edge between 1 - 2 exists? : ', dwg.exist_edge(1,2))
    print('Edge between 2 - 1 exists? : ', dwg.exist_edge(2, 1))
    print("In-Degree", dwg.indegree(2))
    print("Out-Degree", dwg.outdegree(2))
    dwg.remove_edges(1,2)
    print('Edge between 1 - 2 exists? : ', dwg.exist_edge(1,2))
    print(" -------------------------------------------")

