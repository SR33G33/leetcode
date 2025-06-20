# 1192. Critical Connections in a Network

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [a i , b i ] represents a connection between servers a i and b i .
# Any server can reach other servers directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
# Return all critical connections in the network in any order.
# Example 1: Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]] Output: [[1,3]] Explanation: [[3,1]] is also accepted.
# Example 2: Input: n = 2, connections = [[0,1]] Output: [[0,1]] Constraints: 2 <= n <= 10 5 n - 1 <= connections.length <= 10 5 0 <= a i , b i <= n - 1 a i != b i There are no repeated connections.

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        return
