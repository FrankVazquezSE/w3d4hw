#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1

#for loop
#if statement


#ex.1
#input: s = "leetcode"
#Output:0

#ex.2
#input: s = "loveleetcode"
#Output: 2

#ex.3
#input: s = "aabb"
#Output: -1


def non_repeat_char(s):
    for letter in s:
        if s.count(letter) == 1:
            return s.index(letter)
    return -1
        
print(non_repeat_char("loveleetcode"))