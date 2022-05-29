class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x, len(nums)):
                if nums[x] + nums[y] == target:
                    rList = [x,y]
        return rList

#a quick test   
obj = Solution()
testNums = [3,2,4]
testTarget = 6
myList = obj.twoSum(testNums, testTarget)
print(myList)