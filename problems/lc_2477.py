# 2477. Minimum Fuel Cost to Report to the Capital

# There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads.
# The capital city is city 0 .
# You are given a 2D integer array roads where roads[i] = [a i , b i ] denotes that there exists a bidirectional road connecting cities a i and b i .
# There is a meeting for the representatives of each city.
# The meeting is in the capital city.
# There is a car in each city.
# You are given an integer seats that indicates the number of seats in each car.
# A representative can use the car in their city to travel or change the car and ride with another representative.
# The cost of traveling between two cities is one liter of fuel.
# Return the minimum number of liters of fuel to reach the capital city .
# Example 1: Input: roads = [[0,1],[0,2],[0,3]], seats = 5 Output: 3 Explanation: - Representative 1 goes directly to the capital with 1 liter of fuel.
# - Representative 2 goes directly to the capital with 1 liter of fuel.
# - Representative 3 goes directly to the capital with 1 liter of fuel.
# It costs 3 liters of fuel at minimum.
# It can be proven that 3 is the minimum number of liters of fuel needed.
# Example 2: Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2 Output: 7 Explanation: - Representative 2 goes directly to city 3 with 1 liter of fuel.
# - Representative 2 and representative 3 go together to city 1 with 1 liter of fuel.
# - Representative 2 and representative 3 go together to the capital with 1 liter of fuel.
# - Representative 1 goes directly to the capital with 1 liter of fuel.
# - Representative 5 goes directly to the capital with 1 liter of fuel.
# - Representative 6 goes directly to city 4 with 1 liter of fuel.
# - Representative 4 and representative 6 go together to the capital with 1 liter of fuel.
# It costs 7 liters of fuel at minimum.
# It can be proven that 7 is the minimum number of liters of fuel needed.
# Example 3: Input: roads = [], seats = 1 Output: 0 Explanation: No representatives need to travel to the capital city.
# Constraints: 1 <= n <= 10 5 roads.length == n - 1 roads[i].length == 2 0 <= a i , b i < n a i != b i roads represents a valid tree. 1 <= seats <= 10 5

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        return
