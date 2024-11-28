#Majority Element II
"""You are given an array of integer arr[] where each number represents a vote to a candidate.
Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
Note: The answer should be returned in an increasing format. """
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        if not arr:
            return []
        # Initialize two potential candidates and their counts
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        # First pass to find potential candidates
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        # Second pass to confirm the candidates
        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        # Collect the results
        result = []
        n = len(arr)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return sorted(result)
