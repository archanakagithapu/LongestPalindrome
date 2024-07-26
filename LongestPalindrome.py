'''Given a string s which consists of lowercase or uppercase letters,
return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd",
whose length is 7.'''

s = input()
length = 0
odd_counts = 0
chars = list(s)  
for char in chars:
    count = 0
    for c in s:
        if c == char:
            count += 1
    if count % 2 == 0:
        length += count
    else:
        length += count - 1
        odd_counts += 1
if odd_counts > 0:
    length += 1
print(length)
