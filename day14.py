"""Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.
Cases for atoi() conversion:
Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231. """
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        result *= sign
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result
