# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: # type: ignore
#         result = []
#         for num in nums1:
#             found = False
#             ind = nums2.index(num)
#             for j in range(ind + 1, len(nums2)):
#                 if nums2[j] > num:
#                     result.append(nums2[j])
#                     found = True
#                     break
#             if not found:
#                 result.append(-1)
#         return result
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]
