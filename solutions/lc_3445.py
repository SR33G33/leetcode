# 3445. Maximum Difference Between Even and Odd Frequency II

# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:
# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.
# Note that subs can contain more than 2 distinct characters.

class Solution(object):

    def countChar(self, odd_freq, even_freq, char):
        if(char in even_freq.keys()):
            odd_freq[char] = even_freq[char] + 1
            del even_freq[char]
            odd_freq = dict(sorted(odd_freq.items(), key=lambda item: item[1]))
        elif (char in odd_freq.keys()):
            even_freq[char] = odd_freq[char] + 1
            del odd_freq[char]
            even_freq = dict(sorted(even_freq.items(), key=lambda item: item[1]))
        else: 
            odd_freq[char] = 1
            odd_freq = dict(sorted(odd_freq.items(), key=lambda item: item[1]))
        # print(odd_freq)
        # print(even_freq)
        return odd_freq, even_freq



    def removeChar(self, odd_freq, even_freq, char):
        # print(f"Remove {char}")
        if(char in even_freq.keys()):
            # print(f"From Even")
            odd_freq[char] = even_freq[char] - 1
            if(odd_freq[char] == 0): del odd_freq[char]
            del even_freq[char]
            odd_freq = dict(sorted(odd_freq.items(), key=lambda item: item[1]))
        elif (char in odd_freq.keys()):
            # print(f"From Odd")
            even_freq[char] = odd_freq[char] - 1
            if(even_freq[char] == 0): del even_freq[char]
            del odd_freq[char]
            even_freq = dict(sorted(even_freq.items(), key=lambda item: item[1]))

        return odd_freq, even_freq
        # print(odd_freq)
        # print(even_freq)


    def getMaxDiff(self, odd_freq, even_freq):
        if not odd_freq or not even_freq:
            return float('-inf')  # To allow max() to work correctly
        max_odd = max(odd_freq.values())
        min_even = min(even_freq.values())
        return max_odd - min_even


    def maxDifference(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        curr_max_diff = None
        origK = k
        for k in range(origK, len(s) + 1):
            # print(f"K = {k}")
            odd_freq = {}
            even_freq = {}
            subs = s[0:k]
            # print (subs)
                    
            for char in subs:
                odd_freq, even_freq = self.countChar(odd_freq, even_freq, char)
                # print(odd_freq)
                # print(even_freq)

            if(curr_max_diff == None or curr_max_diff == 0): curr_max_diff = self.getMaxDiff(odd_freq, even_freq)
            elif((self.getMaxDiff(odd_freq, even_freq)) >= (curr_max_diff)): curr_max_diff = self.getMaxDiff(odd_freq, even_freq)    

            # print(s[0:k])
            # print(odd_freq)
            # print(even_freq)


            if(k == len(s)): return curr_max_diff
            
            for i in range(1 , len(s) - k + 1):
                odd_freq, even_freq = self.removeChar(odd_freq, even_freq, s[i-1])
                odd_freq, even_freq = self.countChar(odd_freq, even_freq, s[i+k-1])
                # print(s[i:k+i])
                # print(odd_freq)
                # print(even_freq)

                if(curr_max_diff == None or curr_max_diff == 0): curr_max_diff = self.getMaxDiff(odd_freq, even_freq)
                elif((self.getMaxDiff(odd_freq, even_freq)) >= (curr_max_diff)): curr_max_diff = self.getMaxDiff(odd_freq, even_freq)      

                # print(odd_freq)
                # print(even_freq)
            # print(f"Max for K = {k}: {curr_max_diff}")
        return curr_max_diff





sol = Solution()
print(sol.maxDifference("12233", 4))

sol = Solution()

print(sol.maxDifference("1122211", 3))

sol = Solution()

print(sol.maxDifference("110", 3))

sol = Solution()

print(sol.maxDifference("2222130", 2))

sol = Solution()

print(sol.maxDifference("11131340", 8))
