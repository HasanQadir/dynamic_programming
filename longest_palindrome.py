def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    list_str = []
    result = ''
    for i in range(len(s)-1, 0, -1):
        list_str.append(s[:i])
        print(list_str)
        for item in list_str:
            _str = item
            if _str[0:] == _str[::-1]:
                if len(_str) >= len(result):
                    result = _str
    return result

def main():
    _str = str(input("Enter string: "))
    result = longestPalindrome(_str)
    print("Longest Palindrome:", result)

if __name__ == "__main__":
    main()
