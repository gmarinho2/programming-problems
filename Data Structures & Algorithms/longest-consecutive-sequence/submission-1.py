class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        nums = set(nums)
        for num in nums:
            freq_map[num] = 1

        for num in nums:
            if freq_map[num - 1] == 0:
                freq_map[num] = 2
        
        longest = 0
        for num in nums: 
            sequence = 1
            if freq_map[num] == 2:
                next_num = num + 1
                while freq_map[next_num] == 1:
                    sequence += 1
                    next_num += 1
            if longest < sequence:
                longest = sequence
        return longest               

                
        
        
        