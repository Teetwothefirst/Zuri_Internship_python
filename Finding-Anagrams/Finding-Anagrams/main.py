# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #First Collect Users input:
    user_input1 = str(input("Enter your first Anagram check word: "))
    user_input1 = str(input("Enter your Second Anagram check word: "))
    
    if (sorted(word) == sorted(anagram)):
        return True
    else: 
        return False

    print(find_anagram("pat","tap"))
find_anagram("tap","pat")

