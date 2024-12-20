class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Função recursiva para dividir e conquistar
        def findMaxSubArray(nums, left, right):
            if left == right:  # Caso base: um único elemento
                return nums[left]
            
            mid = (left + right) // 2
            
            # Encontre a soma máxima no lado esquerdo, no lado direito e cruzando o meio
            left_max = findMaxSubArray(nums, left, mid)
            right_max = findMaxSubArray(nums, mid + 1, right)
            cross_max = findCrossMax(nums, left, mid, right)
            
            # Retorne o maior entre as três opções
            return max(left_max, right_max, cross_max)
        
        # Função para encontrar a soma máxima cruzando o meio
        def findCrossMax(nums, left, mid, right):
            # Soma máxima à esquerda
            left_sum = float('-inf')
            temp_sum = 0
            for i in range(mid, left - 1, -1):
                temp_sum += nums[i]
                left_sum = max(left_sum, temp_sum)
            
            # Soma máxima à direita
            right_sum = float('-inf')
            temp_sum = 0
            for i in range(mid + 1, right + 1):
                temp_sum += nums[i]
                right_sum = max(right_sum, temp_sum)
            
            # Soma máxima cruzando o meio
            return left_sum + right_sum
        
        return findMaxSubArray(nums, 0, len(nums) - 1)
