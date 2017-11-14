"""
@author: Peng

@problem_description:    
    Given an integer, write an algorithm to convert it to hexadecimal.
    For negative integer, two's complement method is used.
    
    Note:
        All letters in hexadecimal (a-f) must be in lowercase.
        The hexadecimal string must not contain extra leading 0s. 
        If the number is zero, it is represented by a single zero character '0'; 
        otherwise, the first character in the hexadecimal string will not be the zero character.
        
        The given number is guaranteed to fit within the range of a 32-bit signed integer. 
        You must not use any method provided by the library which converts/formats the number to hex directly.

    Example 1:
        Input: 26
        Output: "1a"
    Example 2:
        Input: -1
        Output: "ffffffff"
"""

class Solution(object):
    
    # solution 1
    def toHex_1(self, num):
        """
        :thought: based on short division
        
        :type num: int, the number to be converted
        :rtype: str, result after converting (form as string)
        """
        if num == 0: return '0'
        
        digit = '0123456789abcdef'  # mapping
        res = ''
        for _ in range(8):
            n = num & 15  # mod (num % 16)
            c = digit[n]
            res = c + res  # inverted sequence
            num >>= 4  # div (num / 16)
        res = res.lstrip('0')  # drop 0 in left    
        return res
        
# test code
if __name__ == '__main__':
    s = Solution()
    num = 10
    print('hexadecimal of 100 is: ' + s.toHex_1(num));
    
    

