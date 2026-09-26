def isPalindrome(s):
    s = s.lower()
    return s == s[::-1]

def countVowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

def freqLetters(s):
    s = s.lower()
    freq = {}
    for char in s:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

