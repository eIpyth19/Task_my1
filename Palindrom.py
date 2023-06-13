def isPalindrome(str_p, register = True):
    if register:
        str_p = str_p.lower()
    return str_p == str_p[::-1]

print(isPalindrome("Adfda", False))