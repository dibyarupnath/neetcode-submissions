class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}
        for item in nums:
            freq_dict[item] = freq_dict.get(item, 0) + 1
            if (freq_dict.get(item) > 1):
                return True
        return False

        