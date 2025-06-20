# 1129. Shortest Path with Alternating Colors

# You are given an integer n , the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1 .
# Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
# You are given two arrays redEdges and blueEdges where: redEdges[i] = [a i , b i ] indicates that there is a directed red edge from node a i to node b i in the graph, and blueEdges[j] = [u j , v j ] indicates that there is a directed blue edge from node u j to node v j in the graph.
# Return an array answer of length n , where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
# Example 1: Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = [] Output: [0,1,-1]
# Example 2: Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]] Output: [0,1,-1] Constraints: 1 <= n <= 100 0 <= redEdges.length, blueEdges.length <= 400 redEdges[i].length == blueEdges[j].length == 2 0 <= a i , b i , u j , v j < n

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        return
