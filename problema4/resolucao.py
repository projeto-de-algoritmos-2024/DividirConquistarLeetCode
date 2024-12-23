class Solution(object):
    def countSmaller(self, nums):
        
        offset = 10**4  
        size = 2 * 10**4 + 1  
        bit = [0] * (size + 1)

        def update(index, value):
            while index < len(bit):
                bit[index] += value
                index += index & -index

        def query(index):
            sum_ = 0
            while index > 0:
                sum_ += bit[index]
                index -= index & -index
            return sum_

        counts = []
        for num in reversed(nums):
            # Query the number of elements smaller than the current num
            counts.append(query(num + offset))
            # Update the BIT with the current num
            update(num + offset + 1, 1)

        return counts[::-1]
