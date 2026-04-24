class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for string in strs:
            tamanho = str(len(string))
            new_string += tamanho + "#" + string
            print(new_string)
        return new_string

    def decode(self, s: str) -> List[str]:
        i = j = 0
        string_list = []
        while i < len(s):
            word = ""
            while s[j] != "#":
                j+=1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            word = s[i:j]
            i = j
            string_list.append(word)
        return string_list

