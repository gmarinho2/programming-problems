# Solutions
My explanation for the leetcode problems I have solved.
### [Group Anagrams](https://github.com/gmarinho2/programming-problems/blob/main/Anagram-Groups.py) 
As anagrams have the same number of equal letters, for each word count how many of every letter of the alphabect it has and put that in a **vector[26]** ("a" is 0, "b" is 1 and so on). Use that as a key to a **hashmap of lists** and add this word to the specified list. Return the list of lists. 

### [Top K Elements in List](https://github.com/gmarinho2/programming-problems/blob/main/Top-K-Elements-in-List.py)
**Do a most frequent element algorithm** using one variable to be the biggest frequency (*freq*) and one to be the most frequent element. **Add the element to a list** Use an outer for loop to **iterate it k times**. The catch is: **after every iteration of the outer loop you have to remove the most frequent element from the list *freq* times**.

### [String Encode and Decode](https://github.com/gmarinho2/programming-problems/blob/main/String-Encode-and-Decode.py)
**Add the size of each string in the begging of every string, but with a marker** separating it: 4#hello or as it accepts spaces and numbers: 13#hi my name5is. **Concatenate everything in one string**: 4#hello13#hi my name5is. To decode **read until you read a marker and convert the string you read (except the marker)** to int to use it as size. **Read from marker+1 up to maker+1+size times char**(you can use slices). Add this string to a list. Repeat it until i is bigger then the size of the concatenated string.

### [Products of Array Discluding Self](https://github.com/gmarinho2/programming-problems/blob/main/Products-of-Array-Discluding-Self.py)
To solve it using O(n) without division: create two vectors that have the multiplication of every number in the array cames before and including itself. But one starts from the beggining and other from the ending of the array. Then for each position in the array you just multiply beggining[position - 1] with ending[position + 1].
