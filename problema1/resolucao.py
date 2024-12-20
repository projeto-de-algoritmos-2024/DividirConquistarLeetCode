class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            # Partition nums1 and nums2
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # Boundary values
            maxLeft1 = float('-inf') if i == 0 else nums1[i-1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j-1]
            minRight2 = float('inf') if j == n else nums2[j]

            # Check valid partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Median calculation
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                high = i - 1  # Move left
            else:
                low = i + 1  # Move right
