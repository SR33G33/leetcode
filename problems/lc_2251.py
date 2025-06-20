# 2251. Number of Flowers in Full Bloom

# You are given a 0-indexed 2D integer array flowers , where flowers[i] = [start i , end i ] means the i th flower will be in full bloom from start i to end i ( inclusive ).
# You are also given a 0-indexed integer array people of size n , where people[i] is the time that the i th person will arrive to see the flowers.
# Return an integer array answer of size n , where answer[i] is the number of flowers that are in full bloom when the i th person arrives.
# Example 1: Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11] Output: [1,2,2,2] Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
# Example 2: Input: flowers = [[1,10],[3,3]], people = [3,3,2] Output: [2,2,1] Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
# Constraints: 1 <= flowers.length <= 5 * 10 4 flowers[i].length == 2 1 <= start i <= end i <= 10 9 1 <= people.length <= 5 * 10 4 1 <= people[i] <= 10 9

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        return
