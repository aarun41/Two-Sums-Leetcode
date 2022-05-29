from heapq import heappush, heappop
class Solution(object):

    @staticmethod
    def heapsort(list):
        """
        :type list: List[int]
        :rtype: List[int]
        """
        heap = []
        for element in list:
            heappush(heap, element)
        
        sorted = []
        for x in range(len(heap)):
            sorted.append(heappop(heap))
        return sorted

    @staticmethod
    def binarySearch(list, target):
        """
        :type list: List[int]
        :type target: int
        :rtype: int
        """
        hi = len(list)
        lo = 0
        while lo < hi:
            mid = (hi + lo) // 2
            midval = list[mid]
            if midval < target:
                lo = mid + 1
            elif midval > target:
                hi = mid
            else:
                return mid
        return -1



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newNums = Solution.heapsort(nums)

        for x in range(len(nums)//2):
            val1 = newNums[x]
            ind2 = Solution.binarySearch(newNums, target - newNums[x])
            if ind2 != -1:
                val2 = newNums[ind2]
        
        rList = [nums.index(val1), nums.index(val2)]
        return rList




        

#a quick test   
obj = Solution()
testNums = [3,2,4]
testTarget = 6
myList = obj.twoSum(testNums, testTarget)
print(myList)