class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        mn = []
        for n in nums1:
            mn.append(n)
        for m in nums2:
            mn.append(m)
        l = len(mn)
        print(l)
        for i in range(l):
            for j in range(i,l):
                if mn[i] > mn[j]:
                    temp = mn[i]
                    mn[i] = mn[j]
                    mn[j] = temp
        if l % 2 == 0:
            median = mn[int(l/2)] + mn[int((l/2) - 1)]
            median = median/2
        else:
            med = int((l+1)/2)
            median = mn[med-1]
        print(mn)
        return(median)
test1 = Solution()
nums1 = [1,2,4,5,8]
nums2 = [3,6,7]
median = test1.findMedianSortedArrays(nums1, nums2)
print(median)