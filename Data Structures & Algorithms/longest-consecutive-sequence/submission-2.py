class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                sequence = 1
                next_num = num + 1
                while next_num in nums:
                    sequence += 1
                    next_num += 1
                if sequence > longest:
                    longest = sequence
        return longest