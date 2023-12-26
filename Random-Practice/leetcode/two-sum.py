# leetcode: Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        frist_indx = 0
        last_index = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    # print(i, j)
                    frist_indx = i
                    last_index = j
                    return [i, j]
                    
            
        
        
        return [frist_indx, last_index]
    
    
nums = [2,7,11,15]
target = 13
sumOB = Solution()
sumOB.twoSum(nums, target)

