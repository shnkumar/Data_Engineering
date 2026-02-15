"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.Docstring for D15_feb
"""
from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
            len_full_list=len(arr)+k
            print(len_full_list)
            full_list=[x for x in range(1,len_full_list+1)]
            
            # print(len(full_list),full_list)
            missing_element=[]
            ptr_target=0
            for i in range(len(full_list)):
                if full_list[i] not in arr:
                        missing_element=full_list[i]
                        ptr_target+=1
                if ptr_target == k :        
                  return missing_element



obj = Solution()
print(obj.findKthPositive([2,3,4,7,11],5))
