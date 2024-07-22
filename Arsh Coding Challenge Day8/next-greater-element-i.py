class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
        result = []
        for num in nums1:
            found = False
            ind = nums2.index(num)
            for j in range(ind + 1, len(nums2)):
                if nums2[j] > num:
                    result.append(nums2[j])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result
