def encode(self, strs: List[str]) -> str:
    new_string = ""
    for string in strs:
        new_string += str(len(string)) + "#" + string
    return new_string

def decode(self, s: str) -> List[str]:
    string_list = []
    i = 0
    while i < len(s):
        counter = i
        size = 0
        while s[counter] != "#":
            counter += 1
        fim = counter + int(s[i:counter]) + 1
        i = counter + 1
        string = s[i:fim]
        i = fim
        string_list.append(string)
    return string_list

#QUESTION:
#Design an algorithm to encode a list of strings to a single string. 
#The encoded string is then decoded back to the original list of strings.
#implement encode and decode