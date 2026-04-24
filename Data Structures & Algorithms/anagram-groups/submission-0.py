class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            letter_count = [0] * 26
            for letter in string:
                letter_count[ord(letter) - ord("a")] += 1
            key = tuple(letter_count)
            anagram_map[key].append(string)
        return anagram_map.values()