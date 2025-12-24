# In the two pointer approach/algorithm we initialize two pointers
# and they move their positions relatively and do comparison depending on the problem
# The pointers are usually described as Left [L] and Right [R] till they meet each other

# This approach is implemented here for the problem: Sorted Squares

class Solution(object):
    def sortedSquares(self, nums):
        # Initializing the left pointer at the start of the array
        left = 0
        
        # Initializing the right pointer at the end of the array
        right = len(nums) - 1
        
        # This list will store the squared values in sorted order
        result = []

        # Loop until both pointers cross each other
        while left <= right:
            
            # Compare absolute values because squaring removes the sign
            if abs(nums[left]) > abs(nums[right]):
                
                # Square the left value and add it to the result
                result.append(nums[left] ** 2)
                
                # Move the left pointer to the right
                left += 1
            
            else:
                # Square the right value and add it to the result
                result.append(nums[right] ** 2)
                
                # Move the right pointer to the left
                right -= 1

        # Reverse the result because we inserted larger squares first
        result.reverse()
        
        # Return the final sorted squared array
        return result
