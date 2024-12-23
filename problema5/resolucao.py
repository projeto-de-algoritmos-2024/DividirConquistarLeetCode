class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def merge_sort(start, end):
            # Base case: single element
            if end - start <= 1:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid, end)
            
            # Count valid range sums in the merge step
            j = k = t = mid
            temp = []
            for left in prefix[start:mid]:
                # Extend the range [j, k) to include sums in [lower, upper]
                while j < end and prefix[j] - left < lower:
                    j += 1
                while k < end and prefix[k] - left <= upper:
                    k += 1
                count += k - j
                
                # Maintain sorted order for merging
                while t < end and prefix[t] < left:
                    temp.append(prefix[t])
                    t += 1
                temp.append(left)
            
            # Add remaining elements from the right half
            temp.extend(prefix[t:end])
            
            # Update the prefix array
            prefix[start:end] = temp
            return count
        
        # Create prefix sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        return merge_sort(0, len(prefix))
