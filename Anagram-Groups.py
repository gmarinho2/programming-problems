def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) #hashmap de listas
        for word in strs:
            letras = [0] * 26
            for letter in word:
                letras[ord("a") - ord(letter)] += 1
            hash_key = tuple(letras)
            hashmap[hash_key].append(word)
        return hashmap.values()

#QUESTION:
#Given an array of strings strs, group all anagrams together into sublists. 
#You may return the output in any order.
#An anagram is a string that contains the exact same characters as another string, 
#but the order of the characters can be different.