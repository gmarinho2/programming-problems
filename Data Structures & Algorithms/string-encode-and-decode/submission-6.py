class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            new_string += string + "//"
        print(new_string)
        return new_string

    def decode(self, s: str) -> List[str]:
        i = 0
        string_list = []
        word = ""
        while i < len(s):
            if s[i] == "/" and s[i+1] == "/":
                string_list.append(word)
                word = ""
                i += 2
            else:
                word += s[i]
                i+=1
            
        return string_list
