# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

from itertools import count


No_chars = 500
str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")

def find_anagram(word, anagram):
    count1 = [0] * No_chars
    count2 = [0] * No_chars

    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    if len(str1) != len(str2):
        return 0
    for i in range(No_chars):
        if count1[i] != count2[2]:
            return 0
    return  1
    
if(find_anagram(str1, str2)):
    print("they are anagrams of each other")
else: 
    print("they are not anagrams")
