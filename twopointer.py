#In the two pinter approach/algorithm we initialize two pointers 
#and they move their positions relatively and do comparision depending on the problem
#The pointers are usually described as Left[L] and Right[R] till they meet each other

#This can be impletented in this problem: sorted squares

class Solution(object):
    def sortedSquares(self, nums):
        #Initializing the pointers
        left = 0
        right = len(nums) -1# the last index
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):#Abs value because -x * -x = +x2
                result.append(nums[left]**2)
                left += 1 
            else:
                result.append(nums[right] ** 2)
                right += 1 

        result.reverse()
        
        return result
